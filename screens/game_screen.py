import pygame
from game.uno_game import UnoGame
from screens.screen import Screen
from renders.card import Card
from renders.text_box import TextBox
from renders.button import Button
from renders.rect import Rect
from utils.timer import Timer
from utils.color_conversion import rgb
from animations.move_animation import MoveAnimation
import copy


class GameScreen(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.com_players_number = 3
        self.max_players = 6
        self.game = UnoGame(human_number=1, com_number=self.com_players_number)
        self.player = self.game.get_player()
        self.coms = self.game.get_com_players()
        self.surfaces = []
        self.player_hand_surface = None
        self.board_surface = None
        self.com_hand_surfaces = []
        self.board_surface_const = {
            "pos": (0, 0),
            "size": (self.screen_width * (3 / 4), self.screen_height * (7 / 10)),
        }
        self.player_hand_surface_const = {
            "pos": (0, self.screen_height * (7 / 10)),
            "size": (self.screen_width * (3 / 4), self.screen_height * (3 / 10)),
        }
        self.com_hand_surface_const = {
            "pos": (self.screen_width * (3 / 4), 0),
            "size": (self.screen_width / 4, self.screen_height / 5),
            "gap": (self.screen_height / 5),
        }
        self.pos = {
            "discard": (500, 200),
            "deck": (300, 200),
        }
        self.deck_render = Rect(
            x=self.pos["deck"][0],
            y=self.pos["deck"][1],
            width=80,
            height=110,
            background_color="black",
            border_width=3,
            **self.rect_params,
        )
        self.card_renders = []
        self.animation_card_renders = []
        self.create_surfaces()

        # handling turns
        self.turn_started = False
        self.turn_timer = Timer()
        self.player_turn_time, self.com_turn_time = 3, 3
        self.turn_ended = False

        # handling game event
        # TODO: show direction in screen
        self.direction = self.game.get_direction()
        self.animations = []

    # region Create functions

    def create_surfaces(self):
        self.player_hand_surface = pygame.Surface(
            self.player_hand_surface_const["size"]
        )
        self.board_surface = pygame.Surface(self.board_surface_const["size"])
        for _ in range(self.max_players - 1):
            self.com_hand_surfaces.append(
                pygame.Surface(self.com_hand_surface_const["size"])
            )
        self.surfaces = [
            self.player_hand_surface,
            self.board_surface,
        ] + self.com_hand_surfaces

    def create_hand_cards(self, screen_pos, player, is_player):
        x, y = screen_pos
        player_hand = player.get_hand()
        if is_player:
            C_WIDTH, C_HEIGHT, C_X, C_Y = 80, 110, x + 80, y + 70
            if len(player_hand) > 7:
                C_GAP = C_WIDTH * 1.1 / (len(player_hand) / 7)
            else:
                C_GAP = C_WIDTH * 1.1
            FONT_SIZE = 38
        else:
            C_WIDTH, C_HEIGHT, C_X, C_Y = 40, 60, x + 30, y + 50
            if len(player_hand) > 7:
                C_GAP = C_WIDTH * 0.6 / (len(player_hand) / 7)
            else:
                C_GAP = C_WIDTH * 0.6
            FONT_SIZE = 20
        card_params = {
            "width": C_WIDTH,
            "height": C_HEIGHT,
            "y": C_Y,
            "face_up": is_player,
            "font_size": FONT_SIZE,
        } | self.rect_params
        for i, card in enumerate(player_hand):
            card_params["x"] = C_X + i * C_GAP
            card_render = Card(
                **card_params,
                card=card,
            )
            self.card_renders.append(card_render)
        player.set_next_card_pos((C_X + (len(player_hand)) * C_GAP, C_Y))

    def create_card_renders(self):
        self.card_renders = []
        # player hand
        self.create_hand_cards(self.player_hand_surface_const["pos"], self.player, True)
        # com hands
        for i, com in enumerate(self.coms):
            self.create_hand_cards(
                (
                    self.com_hand_surface_const["pos"][0],
                    self.com_hand_surface_const["pos"][1]
                    + i * self.com_hand_surface_const["gap"],
                ),
                com,
                False,
            )
        # top discard card
        if self.game.get_top_discard_card() is not None:
            top_discard_card_render = Card(
                x=self.pos["discard"][0],
                y=self.pos["discard"][1],
                width=80,
                height=110,
                face_up=True,
                card=self.game.get_top_discard_card(),
                **self.rect_params,
            )
            self.card_renders.append(top_discard_card_render)

    # endregion

    # region Draw functions

    ## Draw player functions

    def draw_players(self):
        self.draw_player(self.player_hand_surface, self.player, is_player=True)
        for i, com in enumerate(self.coms):
            self.draw_player(self.com_hand_surfaces[i], com, is_player=False)

    def draw_player(self, surface, player, is_player):
        if is_player:
            FONT_SIZE = 35
        else:
            FONT_SIZE = 20
        text_params = {
            "font_size": FONT_SIZE,
            "reposition": False,
        } | self.rect_params
        self.draw_player_name(surface, player.name, text_params)
        self.draw_player_card_number(surface, len(player.hand), text_params)
        if player.is_turn:
            self.draw_turn_timer(surface, text_params)
        pass

    def draw_player_name(self, surface, player_name, text_params):
        S_HEIGHT = surface.get_height()
        player_name_text = TextBox(
            text=player_name,
            x=13,
            y=S_HEIGHT * 0.1,
            **text_params,
        )
        player_name_text.draw(surface)

    def draw_player_card_number(self, surface, card_number, text_params):
        S_WIDTH, S_HEIGHT = surface.get_width(), surface.get_height()
        card_number_text = TextBox(
            text=f"[{card_number}]",
            x=S_WIDTH * 0.8,
            y=S_HEIGHT * 0.1,
            **text_params,
        )
        card_number_text.draw(surface)

    def draw_turn_timer(self, surface, text_params):
        S_WIDTH, S_HEIGHT = surface.get_width(), surface.get_height()
        timer_text = TextBox(
            text=f"{1+int(self.turn_timer.get_remaining_time())}",
            x=S_WIDTH * 0.8,
            y=S_HEIGHT * 0.4,
            **text_params,
        )
        timer_text.draw(surface)

    ## Draw board functions

    def draw_board(self):
        self.draw_top_discard_card_color(
            self.board_surface, self.game.get_top_discard_card()
        )
        self.draw_uno_button(self.board_surface)
        self.draw_deck(self.board_surface)

    def draw_top_discard_card(self, surface, top_discard_card):
        C_WIDTH, C_HEIGHT, C_X, C_Y = 80, 110, 500, 200
        card_params = {
            "width": C_WIDTH,
            "height": C_HEIGHT,
            "x": C_X,
            "y": C_Y,
            **self.rect_params,
        }
        card_render = Card(
            **card_params,
            card=top_discard_card,
        )
        card_render.draw(surface)

    def draw_top_discard_card_color(self, surface, top_discard_card):
        rect_render = Rect(
            x=650,
            y=200,
            width=50,
            height=50,
            background_color=top_discard_card.get_color()
            if top_discard_card is not None
            else "dark_gray",
            border_width=3,
            **self.rect_params,
        )
        rect_render.draw(surface)
        pass

    def draw_uno_button(self, surface):
        uno_button = Button(
            x=650,
            y=270,
            width=70,
            height=40,
            background_color="white",
            text="UNO",
            font_size=20,
            text_color="black",
            **self.rect_params,
        )
        uno_button.draw(surface)
        pass

    def draw_deck(self, surface):
        self.deck_render.draw(surface)

    def draw_surfaces(self):
        # blit surfaces
        self.screen.blit(
            self.player_hand_surface, self.player_hand_surface_const["pos"]
        )
        self.screen.blit(self.board_surface, self.board_surface_const["pos"])
        for i, com_surface in enumerate(self.com_hand_surfaces):
            self.screen.blit(
                com_surface,
                (
                    self.com_hand_surface_const["pos"][0],
                    i * self.com_hand_surface_const["gap"],
                ),
            )
        # fill surfaces & add inner border
        for surface in self.surfaces:
            surface.fill(self.background_color)
            self.add_inner_border(surface, rgb("white"), 3)

    def add_inner_border(self, surface, color, width):
        pygame.draw.rect(
            surface,
            color,
            (0, 0, surface.get_width(), surface.get_height()),
            width,
        )

    def draw_card_renders(self):
        for card_render in self.card_renders:
            card_render.draw(self.screen)

    def draw_animations(self):
        for animation in self.animations:
            animation.draw(self.screen)

    def draw(self):
        super().draw()
        self.draw_surfaces()
        self.draw_board()
        self.draw_players()
        self.draw_card_renders()
        self.draw_animations()

    # endregion

    # region Events
    def process_events(self):
        super().process_events()
        if self.animations:
            self.turn_timer.pause()
            return
        else:
            self.turn_timer.resume()
        # handle player turn timer
        if self.turn_timer.is_finished():
            self.game.turn_time_out()
            self.turn_ended = True
        if self.turn_ended:
            self.end_turn()

    def start_game(self):
        self.game.start_game()
        self.player_turn()

    def player_turn(self):
        self.turn_timer.set_timer(self.player_turn_time)
        self.turn_timer.start()

    def com_turn(self):
        self.turn_timer.set_timer(self.com_turn_time)
        self.turn_timer.start()

    def end_turn(self):
        self.game.next_turn()
        if self.game.get_current_player() == self.player:
            self.player_turn()
        else:
            self.com_turn()
        self.turn_ended = False

    # endregion

    def main_loop(self):
        self.start_game()
        super().main_loop()

    def update(self):
        super().update()
        self.update_animations_finished()
        self.add_game_animations()
        self.create_card_renders()
        for card_render in self.card_renders:
            card_render.update()

    def update_animations_finished(self):
        animations = []
        for animation in self.animations:
            if animation.move_info["type"] == "card_move":
                self.card_move_animation_update(animation)
            animation.update()
            if animation.is_finished():
                self.game.update_by_animtaion_info(animation.move_info)
            else:
                animations.append(animation)
        self.animations = animations

    def card_move_animation_update(self, animation):
        info = animation.move_info
        animation.set_dest_pos(self.find_dest_pos(info["dest"]))

    def add_game_animations(self):
        for i, info in enumerate(self.game.get_animation_infos()):
            if info["type"] == "card_move":
                src_pos = self.find_card_pos(info["card"])
                dest_pos = self.find_dest_pos(info["dest"])
                obj = self.find_card_render(info["card"])
                self.animations.append(
                    MoveAnimation(
                        obj=obj,
                        src_pos=src_pos,
                        dest_pos=dest_pos,
                        duration=0.4,
                        move_info=info,
                        delay=i * 0.1,
                    )
                )
        self.game.set_animation_infos([])

    def find_card_render(self, card):
        for card_render in self.card_renders:
            if card_render.card == card:
                return card_render
        deck_render_copy = copy.deepcopy(self.deck_render)
        self.animation_card_renders.append(deck_render_copy)
        return deck_render_copy

    def find_card_pos(self, card):
        card_render = self.find_card_render(card)
        return (card_render.x, card_render.y)

    def find_dest_pos(self, dest):
        if dest == "deck":
            return self.pos["deck"]
        elif dest == "discard":
            return self.pos["discard"]
        elif dest.startswith("player"):
            if dest == "player_0":
                return self.player.get_next_card_pos()
            else:
                return self.coms[int(dest[-1]) - 1].get_next_card_pos()
