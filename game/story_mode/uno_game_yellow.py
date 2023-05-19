from game.uno_game import UnoGame
from game.uno_constants import COLORS
import random


class UnoGameYellow(UnoGame):
    def __init__(self, players_info):
        super().__init__(players_info)

    def random_change_top_color(self):
        self.top_color = random.choice(COLORS)

    def _start_turn(self, player):
        if self.turn_count is not 0 and self.turn_count % 5 == 0:
            self.random_change_top_color()
        super()._start_turn(player)
