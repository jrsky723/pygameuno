import pygame
from game.uno_game import UnoGame
from screens.screen import Screen
from renders.rect import Rect
from utils.constants import SCREEN as S
from utils.color_conversion import rgb


class GameScreen(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.computer_players = 1
        self.game = UnoGame(player_number=self.computer_players + 1)

    def draw(self):
        super().draw()
