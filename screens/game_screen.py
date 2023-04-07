import pygame
from game.uno_game import UnoGame
from screens.screen import Screen
from renders.card import Card
from renders.text_box import TextBox
from renders.button import Button
from renders.rect import Rect
from utils.color_conversion import rgb
from utils.timer import Timer


class GameScreen(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.com_players_number = 5
        self.max_players = 6
        self.game = UnoGame(player_number=self.com_players_number + 1)
        self.timer = Timer()
        self.player = self.game.get_player()
        self.coms = self.game.get_com_players()
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
        self.surfaces = []
        self.create_surfaces()

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

    ## Draw player functions

    def draw_players(self):
        self.draw_player(self.player_hand_surface, self.player, is_player=True)
        for i, com in enumerate(self.coms):
            self.draw_player(self.com_hand_surfaces[i], com, is_player=False)

    def draw_player(self, surface, player, is_player):
        if is_player:
            FONT_SIZE = 35
            C_WIDTH, C_HEIGHT, C_X, C_Y = 80, 110, 80, 70
            C_GAP = C_WIDTH * 1.1 / (len(player.hand) / 7)  # cards length fix
        else:
            FONT_SIZE = 20
            C_WIDTH, C_HEIGHT, C_X, C_Y = 40, 60, 30, 50
            C_GAP = C_WIDTH * 0.6 / (len(player.hand) / 7)
        card_params = {
            "width": C_WIDTH,
            "height": C_HEIGHT,
            "y": C_Y,
        }
        self.draw_player_name(surface, player.name, FONT_SIZE)
        self.draw_player_hand(surface, player.hand, is_player, card_params, C_X, C_GAP)
        self.draw_player_card_number(surface, len(player.hand), FONT_SIZE)
        if player.is_turn:
            self.draw_timer(surface, FONT_SIZE)
        pass

    def draw_player_name(self, surface, player_name, font_size):
        S_WIDTH, S_HEIGHT = surface.get_width(), surface.get_height()
        player_name_text = TextBox(
            text=player_name,
            x=10,
            y=13,
            font_size=font_size,
            **self.rect_params,
        )
        player_name_text.draw(surface)

    def draw_player_hand(
        self, surface, player_hand, is_player, card_params, C_X, C_GAP
    ):
        for i, card in enumerate(player_hand):
            card_params["x"] = C_X + i * C_GAP
            if is_player:
                card_render = Card(
                    **card_params, color=card.get_color(), text=card.get_abb()
                )
            else:
                card_render = Rect(
                    **card_params, background_color=rgb("black"), border_width=3
                )
            card_render.draw(surface)

    def draw_player_card_number(self, surface, card_number, font_size):
        S_WIDTH, S_HEIGHT = surface.get_width(), surface.get_height()
        card_number_text = TextBox(
            text=f"[{card_number}]",
            x=S_WIDTH * 0.8,
            y=13,
            font_size=font_size,
            **self.rect_params,
        )
        card_number_text.draw(surface)

    def draw_timer(self, surface, font_size):
        S_WIDTH, S_HEIGHT = surface.get_width(), surface.get_height()
        timer_text = TextBox(
            text=f"{1+int(self.timer.get_remaining_time())}",
            x=S_WIDTH * 0.8,
            y=S_HEIGHT * 0.4,
            font_size=font_size,
            **self.rect_params,
        )
        timer_text.draw(surface)

    ## Draw board functions

    def draw_board(self):
        # draw deck
        self.draw_deck(self.board_surface)
        self.draw_top_card(self.board_surface, self.game.get_top_card())
        self.draw_top_card_color(self.board_surface, self.game.get_top_card())
        self.draw_uno_button(self.board_surface)

    def draw_deck(self, surface):
        # draw card back
        C_WIDTH, C_HEIGHT, C_X, C_Y = 80, 110, 300, 200
        rect_render = Rect(
            x=C_X,
            y=C_Y,
            width=C_WIDTH,
            height=C_HEIGHT,
            background_color=rgb("black"),
            border_width=3,
        )
        rect_render.draw(surface)

        pass

    def draw_top_card(self, surface, top_card):
        C_WIDTH, C_HEIGHT, C_X, C_Y = 80, 110, 500, 200
        card_params = {
            "width": C_WIDTH,
            "height": C_HEIGHT,
            "x": C_X,
            "y": C_Y,
        }
        card_render = Card(
            **card_params,
            color=top_card.get_color(),
            text=top_card.get_abb(),
        )
        card_render.draw(surface)

    def draw_top_card_color(self, surface, top_card):
        rect_render = Rect(
            x=650,
            y=200,
            width=50,
            height=50,
            background_color=rgb(top_card.get_color()),
            border_width=3,
        )
        rect_render.draw(surface)
        pass

    def draw_uno_button(self, surface):
        uno_button = Button(
            x=650,
            y=270,
            width=70,
            height=40,
            background_color=rgb("white"),
            text="UNO",
            font_size=20,
            text_color=rgb("black"),
        )
        uno_button.draw(surface)
        pass

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

    def draw(self):
        super().draw()
        self.draw_surfaces()
        self.draw_board()
        self.draw_players()

    def process_events(self):
        super().process_events()
        # handle player turn timer
        if self.timer.is_finished():
            self.next_turn()

    def next_turn(self):
        self.game.next_turn()
        self.timer.reset()
        self.timer.start()

    def start_game(self):
        self.game.start_game()
        self.player_turn()

    def player_turn(self):
        self.timer.set_timer(10)
        self.timer.start()

    def main_loop(self):
        self.start_game()
        super().main_loop()
