import pygame
from game.uno_game import UnoGame
from screens.screen import Screen
from renders.card import Card
from renders.text_box import TextBox
from renders.rect import Rect
from utils.color_conversion import rgb


class GameScreen(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.com_players_number = 5
        self.max_players = 6
        self.game = UnoGame(player_number=self.com_players_number + 1)
        self.player = self.game.players[0]
        self.coms = self.game.players[1:]
        self.top_card = self.game.top_card
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
        self.player_hand_surface.fill(self.background_color)
        self.board_surface.fill(self.background_color)
        for hand_surface in self.com_hand_surfaces:
            hand_surface.fill(self.background_color)

    # Draw the card_back img as many cards as the computer has. and also resize it to fit in the rectangle
    def draw_com_player(self, surface, player):
        # draw com name
        com_name = TextBox(
            text=player.name, x=10, y=13, font_size=25, **self.rect_params
        )
        com_name.draw(surface)

        C_WIDTH, C_HEIGHT = 40, 60
        C_GAP = C_WIDTH * 0.6 / (len(player.hand) / 7)  # cards length fix
        C_X, C_Y = 30, 50
        card_params = self.rect_params | {
            "width": C_WIDTH,
            "height": C_HEIGHT,
            "y": C_Y,
        }
        # card_back is a black rectangle which has white border
        for i in range(len(player.hand)):
            card_back = Rect(
                **card_params,
                x=C_X + C_GAP * i,
                background_color=rgb("black"),
                border_width=3
            )
            card_back.draw(surface)
        # draw the number of cards
        card_number = TextBox(
            text=str(len(player.hand)),
            x=250,
            y=C_Y + 10,
            font_size=40,
            **self.rect_params
        )
        card_number.draw(surface)

        # draw the number of cards

    def draw_player_hand(self, surface, player):
        # draw player name
        player_name = TextBox(
            text=player.name, x=10, y=15, font_size=30, **self.rect_params
        )
        player_name.draw(surface)

        C_WIDTH, C_HEIGHT = 80, 110
        C_GAP = C_WIDTH * 1.1 / (len(player.hand) / 7)
        C_X, C_Y = 80, 70
        card_params = self.rect_params | {
            "width": C_WIDTH,
            "height": C_HEIGHT,
            "y": C_Y,
        }
        for i, card in enumerate(player.hand):
            card_params["x"] = C_X + i * C_GAP
            card_render = Card(**card_params, color=card.color, text=card.get_abb())
            card_render.draw(surface)

    def draw_hands(self):
        self.draw_player_hand(self.player_hand_surface, self.player)
        for i, com in enumerate(self.coms):
            self.draw_com_player(self.com_hand_surfaces[i], com)

    def draw_top_card(self):
        pass

    def draw_board(self):
        self.draw_top_card()
        pass

    def draw_surface(self):
        self.screen.blit(
            self.player_hand_surface, self.player_hand_surface_const["pos"]
        )
        self.screen.blit(self.board_surface, self.board_surface_const["pos"])
        for i, com_surface in enumerate(self.com_hand_surfaces):
            self.screen.blit(
                com_surface, (self.screen_width * (3 / 4), i * (self.screen_height / 5))
            )
        # draw inner border for all surfaces
        self.add_inner_border(self.player_hand_surface, rgb("white"), 3)
        self.add_inner_border(self.board_surface, rgb("white"), 3)
        for com_surface in self.com_hand_surfaces:
            self.add_inner_border(com_surface, rgb("white"), 3)

    def add_inner_border(self, surface, color, width):
        pygame.draw.rect(
            surface,
            color,
            (0, 0, surface.get_width(), surface.get_height()),
            width,
        )

    def draw(self):
        super().draw()
        self.draw_board()
        self.draw_hands()
        self.draw_surface()
