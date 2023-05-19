import unittest
from game.story_mode.uno_game_green import UnoGameGreen


class TestUnoGameGreen(unittest.TestCase):
    def setUp(self):
        self.players_info = [
            {"name": "Player 1", "is_com": False},
            {"name": "Player 2", "is_com": False},
            {"name": "Player 3", "is_com": False},
        ]

    def test_deal_cards(self):
        game = UnoGameGreen(self.players_info)
        game._start_game()
        game._create_deck()
        game._deal_cards()
        for player in game.players:
            self.assertEqual(len(player.hand), 7)

if __name__ == '__main__':
    unittest.main()
