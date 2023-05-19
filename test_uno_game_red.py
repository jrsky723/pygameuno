import unittest
import random
from collections import Counter
from game.story_mode.uno_game_red import UnoGameRed

class TestUnoGameRed(unittest.TestCase):
    def setUp(self):
        self.total_trials = 1000
        self.players_info = [
            {"name": "player1", "is_com": True},
            {"name": "player2", "is_com": True},
            {"name": "player3", "is_com": False},
            {"name": "player4", "is_com": False}
        ]

    def test_card_distribution(self):
        action_card_counts = 0
        number_card_counts = 0

        for _ in range(self.total_trials):
            game = UnoGameRed(self.players_info)
            game._start_game()
            for player in game.com_players:
                for _ in range(5):
                    weight = random.randint(0, 2)
                    if weight == 0:
                        card = game.number_cards.pop(0)
                        number_card_counts += 1
                    else:
                        card = game.action_cards.pop(0)
                        action_card_counts += 1

        total_cards = action_card_counts + number_card_counts

        print(f"Out of {total_cards} cards, {action_card_counts} were action cards and {number_card_counts} were number cards.")

if __name__ == '__main__':
    unittest.main()
