from game.uno_game import UnoGame
import random


class UnoGameBlue(UnoGame):
    def __init__(self, players_info):
        self.random_reload_rate = 0
        super().__init__(players_info)

    def _end_turn(self, player):
        super()._end_turn(player)
        if player.is_human():
            self.random_reload_rate += 0.05
            if self.random_reload_rate > 1:
                self.random_reload_rate = 1

    def _start_turn(self, player):
        if player.is_human():
            if random.random() < self.random_reload_rate:
                self._reload_hand(player)
        super()._start_turn(player)
