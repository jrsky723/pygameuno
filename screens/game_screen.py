import pygame
from game.uno_game import UnoGame
from screens.screen import Screen
from renders.card import Card
from utils.constants import SCREEN as S, CARD as C
from utils.color_conversion import rgb, random_rgb


class GameScreen(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.com_players_number = 1
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

        self.player_hand_surface.fill(rgb("dark_gray", self.color_blind))
        self.board_surface.fill(rgb("blue", self.color_blind))
        for hand_surface in self.com_hand_surfaces:
            hand_surface.fill(random_rgb())

    def draw_hand(self, surface, hand, is_player=True):
        S_WIDTH = surface.get_width()
        S_HEIGHT = surface.get_height()
        C_WIDTH, C_HEIGHT = S_WIDTH / 13, S_HEIGHT / 3
        C_GAP = C_WIDTH * 1.1
        C_X, C_Y = C_WIDTH / 2, S_HEIGHT * 0.4
        font_size = C.FONT_SIZE if is_player else C.FONT_SIZE * 0.7
        card_params = self.rect_params | {
            "width": C_WIDTH,
            "height": C_HEIGHT,
            "font_size": font_size,
            "y": C_Y,
        }
        for i, card in enumerate(hand):
            card_params["x"] = C_X + i * C_GAP
            card_render = Card(**card_params, color=card.color, text=card.get_abb())
            card_render.draw(surface)
        pass

    def draw_hands(self):
        self.draw_hand(self.player_hand_surface, self.player.hand, is_player=True)
        for i, com in enumerate(self.coms):
            self.draw_hand(self.com_hand_surfaces[i], com.hand, is_player=False)

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
