import pygame
from game.uno_game import UnoGame
from screens.screen import Screen
from screens.menus.end_menu_screen import EndMenuScreen
from renders.card import Card
from renders.text_box import TextBox
from renders.button import Button
from renders.rect import Rect
from utils.timer import Timer
from utils.color_conversion import rgb
from animations.move_animation import MoveAnimation
from utils.constants import SCREEN as S, SIZE_RATIO as SR, SOUND, MUSIC
import copy


class GameScreen(Screen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        pygame.mixer.music.load(MUSIC.GAME_BACKGROUND)
        pygame.mixer.music.play(-1)
        self.com_players_number = 3
        self.max_players = 6
        self.game = UnoGame(human_number=1, com_number=self.com_players_number)
        self.my_player = self.game.get_player()
        self.coms = self.game.get_com_players()
        self.surfaces = []
        self.my_hand_surface = None
        self.board_surface = None
        self.com_hand_surfaces = []
        self.board_surface_const = {
            "pos": (0, 0),
            "size": (self.screen_width * (3 / 4), self.screen_height * (7 / 10)),
        }
        self.my_hand_surface_const = {
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
            "my_hand": (0, S.HEIGHT_BASE * (7 / 10)),
            "com_hand": (S.WIDTH_BASE * (3 / 4), 0),
            "com_hand_gap": (S.HEIGHT_BASE / 5),
        }

        # Board
        self.uno_button = None
        self.deck_render = None

        self.card_renders = []
        self.animation_card_renders = []
        # TODO: for player input cards only
        #  hover, click
        self.my_hand_card_renders = []
        self.create_surfaces()
        self.create_board()

        # handling turns
        self.turn_started = False
        self.turn_timer = Timer()
        self.my_turn_time, self.com_turn_time = 20, 2

        # handling game event
        # TODO: show direction in screen
        self.direction = self.game.get_direction()
        self.animations = []

        # sound
        self.sound = {
            "card_move": pygame.mixer.Sound(SOUND.CARD_MOVE),
            "card_flip": pygame.mixer.Sound(SOUND.CARD_FLIP),
            "card_error": pygame.mixer.Sound(SOUND.CARD_ERROR),
        }
        for sound in self.sound.values():
            sound.set_volume(self.sound_effects_volume)

        # card_selection
        self.hovered_card_render = None
        self.hovered_card_render_idx = None

    # region Create functions

    def create_surfaces(self):
        self.my_hand_surface = pygame.Surface(self.my_hand_surface_const["size"])
        self.board_surface = pygame.Surface(self.board_surface_const["size"])
        for _ in range(self.max_players - 1):
            self.com_hand_surfaces.append(
                pygame.Surface(self.com_hand_surface_const["size"])
            )
        self.surfaces = [
            self.my_hand_surface,
            self.board_surface,
        ] + self.com_hand_surfaces

    def create_hand_cards(self, screen_pos, player, is_me):
        x, y = screen_pos
        player_hand = player.get_hand()
        if is_me:
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
            "face_up": is_me,
            "font_size": FONT_SIZE,
        } | self.rect_params

        for i, card in enumerate(player_hand):
            card_params["x"] = C_X + i * C_GAP
            card_render = Card(
                **card_params,
                card=card,
            )
            self.card_renders.append(card_render)
            if is_me:
                self.my_hand_card_renders.append(card_render)

        next_card_pos = (C_X + (len(player_hand)) * C_GAP, C_Y)
        next_card_pos_repositioned = tuple(
            x * SR[self.screen_size] for x in next_card_pos
        )
        player.set_next_card_pos(next_card_pos_repositioned)

    def create_card_renders(self):
        self.card_renders, self.my_hand_card_renders = [], []
        # My hand
        self.create_hand_cards(self.pos["my_hand"], self.my_player, True)
        # com hands
        for i, com in enumerate(self.coms):
            self.create_hand_cards(
                (
                    self.pos["com_hand"][0],
                    self.pos["com_hand"][1] + i * self.pos["com_hand_gap"],
                ),
                com,
                False,
            )
        # top discard card
        if self.game.top_discard_card() is not None:
            top_discard_card_render = Card(
                x=self.pos["discard"][0],
                y=self.pos["discard"][1],
                width=80,
                height=110,
                face_up=True,
                card=self.game.top_discard_card(),
                **self.rect_params,
            )
            self.card_renders.append(top_discard_card_render)

    # endregion

    # region Draw functions

    ## Draw player functions

    def draw_players(self):
        self.draw_player(self.my_hand_surface, self.my_player, is_me=True)
        for i, com in enumerate(self.coms):
            self.draw_player(self.com_hand_surfaces[i], com, is_me=False)

    def draw_player(self, surface, player, is_me):
        FONT_SIZE = 35 if is_me else 20
        text_params = {"font_size": FONT_SIZE, "reposition": False} | self.rect_params
        self.draw_player_name(surface, player.name, text_params)
        self.draw_player_card_number(surface, len(player.hand), text_params)
        if player.is_turn:
            self.draw_turn_timer(surface, text_params)
        pass

    def draw_player_name(self, surface, player_name, text_params):
        S_HEIGHT = surface.get_height()
        player_name_text = TextBox(
            text=player_name, x=13, y=S_HEIGHT * 0.1, **text_params
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

    ## Create board functions
    def create_top_discard_card_color(self):
        self.top_discard_card_color = Rect(
            x=650,
            y=200,
            width=50,
            height=50,
            background_color="dark_gray",
            border_width=3,
            **self.rect_params,
        )

    def create_uno_button(self):
        self.uno_button = Button(
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

    def create_deck_render(self):
        self.deck_render = Rect(
            x=self.pos["deck"][0],
            y=self.pos["deck"][1],
            width=80,
            height=110,
            background_color="black",
            border_width=3,
            **self.rect_params,
        )

    def create_board(self):
        self.create_uno_button()
        self.create_deck_render()

    def draw_board(self):
        self.draw_top_discard_card_color(self.board_surface, self.game.get_top_color())
        self.uno_button.draw(self.board_surface)
        self.deck_render.draw(self.board_surface)

    def draw_top_discard_card_color(self, surface, color):
        rect_render = Rect(
            x=650,
            y=200,
            width=50,
            height=50,
            background_color=color if color is not None else "dark_gray",
            border_width=3,
            **self.rect_params,
        )
        rect_render.draw(surface)

    def draw_surfaces(self):
        # blit surfaces
        self.screen.blit(self.my_hand_surface, self.my_hand_surface_const["pos"])
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
        if self.hovered_card_render is not None:
            self.hovered_card_render.draw(self.screen)

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
        if self.animations:
            self.turn_timer.pause()
            return
        super().process_events()
        self.turn_timer.resume()
        if self.game.get_game_event_infos():
            self.process_game_events()
        # handle player turn timer
        if self.turn_timer.is_finished():
            self.game.turn_time_out()
            self.end_turn()

    def process_game_events(self):
        for event_info in self.game.get_game_event_infos():
            if event_info["type"] == "player_win":
                self.game_over()
        self.game.set_game_event_infos([])

    def start_game(self):
        self.game.start_game()
        self.my_turn()

    def my_turn(self):
        self.turn_timer.set_timer(self.my_turn_time)
        self.turn_timer.start()

    def com_turn(self):
        self.turn_timer.set_timer(self.com_turn_time)
        self.turn_timer.start()

    def end_turn(self):
        self.game.next_turn()
        if self.game.get_current_player() == self.my_player:
            self.my_turn()
        else:
            self.com_turn()

    # endregion
    def main_loop(self):
        self.create_card_renders()
        super().main_loop()

    def run(self):
        try:
            self.start_game()
        except Exception as e:
            print(e)
        super().run()

    def update(self):
        super().update()
        self.update_animations_finished()
        self.add_game_animations()
        for card_render in self.card_renders:
            card_render.update()

    def update_animations_finished(self):
        animations = []
        for i, animation in enumerate(self.animations):
            if i != 0:
                animation.set_start_time(self.animations[i - 1].get_start_time())
            if animation.__class__.__name__ == "MoveAnimation":
                if animation.move_info["type"] == "card_move":
                    self.card_move_animation_update(animation)
            animation.update()
            if animation.is_delay_finished() and not animation.get_sound_played():
                self.play_animation_sound(animation)
            if animation.is_finished():
                self.game.update_by_animtaion_info(animation.move_info)
            else:
                animations.append(animation)
        self.animations = animations

    def card_move_animation_update(self, animation):
        info = animation.move_info
        animation.set_dest_pos(self.find_dest_pos(info["dest"]))

    def add_game_animations(self):
        for info in self.game.get_animation_infos():
            if info["type"] == "card_move":
                src_pos = self.find_card_pos(info["card"])
                dest_pos = self.find_dest_pos(info["dest"])
                obj = self.find_card_render(info["card"])
                self.animations.append(
                    MoveAnimation(
                        obj=obj,
                        src_pos=src_pos,
                        dest_pos=dest_pos,
                        duration=info["duration"],
                        delay=info["delay"],
                        move_info=info,
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
            return self.update_pos(self.pos["deck"])
        elif dest == "discard":
            return self.update_pos(self.pos["discard"])
        elif dest.startswith("player"):
            if dest == "player_0":
                return self.my_player.get_next_card_pos()
            else:
                return self.coms[int(dest[-1]) - 1].get_next_card_pos()

    def update_pos(self, pos):
        result = tuple(x * SR[self.screen_size] for x in pos)
        return result

    def game_over(self):
        self.running = False
        end_menu_screen = EndMenuScreen(
            self.screen, self.clock, self.options, self.game.get_winner()
        )
        end_menu_screen.run()

    # Sound
    def play_animation_sound(self, animation):
        animation.set_sound_played(True)
        # CHECK ANIMATION CLASS NAME
        if animation.__class__.__name__ == "MoveAnimation":
            self.sound["card_move"].play()

    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            self.find_hoverd_card(pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_click(event)

    def find_hoverd_card(self, pos):
        for i, card_render in enumerate(self.my_hand_card_renders):
            if card_render.is_on_mouse(pos):
                self.hovered_card_render = card_render
                self.hovered_card_render_idx = i
            else:
                self.card_unhover(i)
        if self.hovered_card_render:
            self.hovered_card_render.hover()

    def card_unhover(self, idx):
        if self.hovered_card_render_idx == idx:
            self.hovered_card_render = None
            self.hovered_card_render_idx = None

    def handle_mouse_click(self, event):
        if self.hovered_card_render:
            self.card_clicked(self.hovered_card_render)
        if self.deck_render.is_on_mouse(event.pos):
            self.deck_clicked()

    def card_clicked(self, card_render):
        try:
            if self.game.get_current_player() == self.my_player:
                played = self.game.play_card(self.my_player, card_render.card)
                if played:
                    self.hovered_card_render = None
                    self.end_turn()
                    self.sound["card_flip"].play()
                else:
                    self.sound["card_error"].play()
                # self.my_hand_card_renders.remove(card_render)

        except Exception as e:
            print(e)

    def deck_clicked(self):
        try:
            if self.game.get_current_player() == self.my_player:
                self.game.draw_card(self.my_player)
                self.end_turn()
                self.sound["card_flip"].play()
        except Exception as e:
            print(e)
