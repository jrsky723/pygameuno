"""
import unittest
from game.uno_card import UnoCard
from game.uno_com_player import UnoComPlayer
from game.uno_game import UnoGame
from game.uno_player import UnoPlayer


class TestUnoGame(unittest.TestCase):
    def setUp(self):
        self.game = UnoGame(human_number=1, com_number=1)

    def test_init(self):
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.player_number, 2)
        self.assertEqual(self.game.human_number, 1)
        self.assertEqual(self.game.com_number, 1)
        self.assertEqual(len(self.game.deck), 108)
        self.assertEqual(len(self.game.discard_pile), 0)
        self.assertIsNone(self.game.winner)
        self.assertFalse(self.game.game_over)
        self.assertIsNone(self.game.selected_color)
        self.assertIsNone(self.game.top_color)
        self.assertIsNone(self.game.top_value)

    def test_create_deck(self):
        deck = self.game._create_deck()
        self.assertEqual(len(deck), 104)

    def test_shuffle_deck(self):
        deck_before = self.game.deck.copy()
        self.game._shuffle_deck()
        deck_after = self.game.deck.copy()
        self.assertNotEqual(deck_before, deck_after)

    def test_deal_cards(self):
        player1 = self.game.players[0]
        player2 = self.game.players[1]
        self.assertEqual(len(player1.hand), 0)
        self.assertEqual(len(player2.hand), 0)
        self.game._deal_cards(num_cards=2)
        self.assertEqual(len(player1.hand), 0)
        self.assertEqual(len(player2.hand), 0)
        self.assertEqual(len(self.game.deck), 104)

    def test_add_players(self):
        self.game._add_players()
        self.assertEqual(len(self.game.players), 4)
        self.assertIsInstance(self.game.players[0], UnoPlayer)
        self.assertIsInstance(self.game.players[1], UnoComPlayer)

    def test_can_play_card(self):
        player = self.game.players[0]
        card1 = UnoCard(type="number", color="red", value="5")
        card2 = UnoCard(type="action", color="blue", value="reverse")
        self.game.top_color = "red"
        self.game.top_value = "5"
        self.assertTrue(self.game.can_play_card(player, card1))
        self.assertFalse(self.game.can_play_card(player, card2))

    def test_play_card(self):
        player = self.game.players[0]
        card = UnoCard(type="number", color="red", value="5")
        self.assertTrue(self.game.play_card(player, card))
        self.assertEqual(len(player.hand), 0)
        self.assertEqual(len(self.game.discard_pile), 1)
        self.assertEqual(self.game.top_color, "red")
        self.assertEqual(self.game.top_value, "5")

    def test_auto_turn(self):
        com_player = self.game.players[1]
        self.game.top_color = "red"
        self.game.top_value = "5"
        com_player.add_card(UnoCard(type="number", color="red", value="4"))
        com_player.add_card(UnoCard(type="number", color="blue", value="5"))
        com_player.add_card(UnoCard(type="action", color="blue", value="skip"))
        self.game.auto_turn(com_player)
        self.assertEqual(len(com_player.hand), 2)
        self.assertEqual(self.game.current_player_idx, 0)

    def test_draw_card(self):
        player = self.game.players[0]
        self.game.draw_card(player)
        self.assertEqual(len(player.hand), 0)
        self.assertEqual(len(self.game.deck), 107)

    def test_turn_time_out(self):
        player = self.game.players[0]
        self.game.top_color = "red"
        self.game.top_value = "5"
        player.add_card(UnoCard(type="number", color="red", value="4"))
        player.add_card(UnoCard(type="number", color="blue", value="5"))
        player.add_card(UnoCard(type="action", color="blue", value="skip"))
        self.game.turn_time_out()
        self.assertEqual(self.game.current_player_idx, 0)


    def test_handle_action_reverse(self):
        player = self.game.players[0]
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="reverse"))
        self.assertEqual(self.game.direction, -1)

    def test_handle_action_skip(self):
        player = self.game.players[0]
        self.game.current_player_idx = 0
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="skip"))
        self.assertEqual(self.game.current_player_idx, 1)

    def test_handle_action_draw2(self):
        player = self.game.players[0]
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="draw2"))
        self.assertEqual(len(self.game.players[1].hand), 2)
        self.assertEqual(self.game.current_player_idx, 1)

    def test_handle_action_draw4(self):
        player = self.game.players[0]
        self.game._handle_action(player, UnoCard(type="action", color="black", value="draw4"))
        elf.assertEqual(len(self.game.players[1].hand), 4)
        self.assertEqual(self.game.current_player_idx, 1)

    def test_handle_action_reload(self):
        player = self.game.players[0]
        player.add_card(UnoCard(type="number", color="red", value="4"))
        player.add_card(UnoCard(type="number", color="blue", value="5"))
        player.add_card(UnoCard(type="action", color="blue", value="skip"))
        self.game._handle_action(player, UnoCard(type="action", color="black", value="reload"))
        self.assertEqual(len(player.hand), 7)
        self.assertEqual(len(self.game.deck), 104)

    def test_handle_action_color_change(self):
        player = self.game.players[0]
        player.add_card(UnoCard(type="number", color="red", value="4"))
        player.add_card(UnoCard(type="number", color="blue", value="5"))
        player.add_card(UnoCard(type="action", color="blue", value="skip"))
        self.game._change_color(player)
        self.assertIsNotNone(self.game.selected_color)

    def test_handle_action_bonus(self):
        player = self.game.players[0]
        self.game.current_player_idx = 0
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="bonus"))
        self.assertEqual(self.game.current_player_idx, 0)

    def test_update_by_animtaion_info(self):
        player = self.game.players[0]
        card = UnoCard(type="number", color="red", value="5")
        self.game.add_card_move_animation(card, src="deck", dest=f"player_{player.get_id()}")
        info = self.game.animation_infos[0]
        self.game.update_by_animtaion_info(info)
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(len(self.game.deck), 104)

    def test_handle_action(self):
        player = self.game.players[0]
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="reverse"))
        self.assertEqual(self.game.direction, -1)
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="skip"))
        self.assertEqual(self.game.current_player_idx, 0)
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="draw2"))
        self.assertEqual(len(self.game.players[1].hand), 2)
        self.assertEqual(self.game.current_player_idx, 0)
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="draw4"))
        self.assertEqual(len(self.game.players[1].hand), 6)
        self.assertEqual(self.game.current_player_idx, 0)
        self.game._handle_action(player, UnoCard(type="action", color="blue", value="reload"))
        self.assertEqual(len(player.hand), 7)
        self.game._handle_action(player, UnoCard(type="action", color="black", value="color_change"))
        self.assertEqual(self.game.selected_color, "red")

    def test_next_turn(self):
        player1 = self.game.players[0]
        player2 = self.game.players[1]
        player1.set_is_turn(True)
        self.game.next_turn()
        self.assertFalse(player1.is_turn)
        self.assertTrue(player2.is_turn)

    def test_prev_turn(self):
        player1 = self.game.players[0]
        player2 = self.game.players[1]
        player1.set_is_turn(True)
        self.game.prev_turn()
        self.assertFalse(player1.is_turn)
        self.assertTrue(player2.is_turn)

    def test_is_game_over(self):
        self.assertFalse(self.game.is_game_over())
        player1 = self.game.players[0]
        player1.hand = []
        self.game.moving_card_nums = 1
        self.game.play_card(player1, UnoCard(type="number", color="red", value="5"))
        self.assertTrue(self.game.is_game_over())
        self.assertIsNotNone(self.game.winner)

    def test_get_winner(self):
        self.assertIsNone(self.game.get_winner())
        player1 = self.game.players[0]
        player1.hand = []
        self.game.moving_card_nums = 1
        self.game.play_card(player1, UnoCard(type="number", color="red", value="5"))
        self.assertIsNotNone(self.game.get_winner())

    def test_get_com_players(self):
        com_players = self.game.get_com_players()
        self.assertEqual(len(com_players), 1)
        self.assertIsInstance(com_players[0], UnoComPlayer)

    def test_get_current_player(self):
        player1 = self.game.players[0]
        player2 = self.game.players[1]
        player1.set_is_turn(True)
        self.assertEqual(self.game.get_current_player(), player1)
        player1.set_is_turn(False)
        player2.set_is_turn(True)
        self.assertEqual(self.game.get_current_player(), player2)

    def test_get_next_player(self):
        player1 = self.game.players[0]
        player2 = self.game.players[1]
        self.assertEqual(self.game.get_next_player(), player2)
        self.game.direction = -1
        self.assertEqual(self.game.get_next_player(), player1)

    def test_get_prev_player(self):
        player1 = self.game.players[0]
        player2 = self.game.players[1]
        self.assertEqual(self.game.get_prev_player(), player2)
        self.game.direction = -1
        self.assertEqual(self.game.get_prev_player(), player1)

        """

import pytest
from game.uno_game import UnoGame

# Test the initialization of UnoGame
def test_uno_game_init():
    game = UnoGame(human_number=1, com_number=1)
    assert game.human_number == 1
    assert game.com_number == 1
    assert len(game.players) == 2
    assert len(game.deck) == 108
    assert not game.game_over

# Test adding players
def test_add_players():
    game = UnoGame(human_number=2, com_number=2)
    assert len(game.players) == 4

# Test shuffling the deck
def test_shuffle_deck():
    game = UnoGame(human_number=1, com_number=1)
    original_deck = list(game.deck)
    game._shuffle_deck()
    assert game.deck != original_deck

# Test dealing cards to players
def test_deal_cards():
    game = UnoGame(human_number=1, com_number=1)
    game.start_game()
    assert len(game.players[0].hand) == 7
    assert len(game.players[1].hand) == 7
    assert len(game.deck) == 94

# Test drawing a card
def test_draw_card():
    game = UnoGame(human_number=1, com_number=1)
    game.start_game()
    game.draw_card(game.players[0])
    assert len(game.players[0].hand) == 8
    assert len(game.deck) == 93

# Test playing a valid card
def test_play_card_valid():
    game = UnoGame(human_number=1, com_number=1)
    game.start_game()
    top_card = game.top_discard_card()
    valid_card = None
    for card in game.players[0].hand:
        if game.can_play_card(game.players[0], card):
            valid_card = card
            break
    assert game.play_card(game.players[0], valid_card) == True

# Test playing an invalid card
def test_play_card_invalid():
    game = UnoGame(human_number=1, com_number=1)
    game.start_game()
    top_card = game.top_discard_card()
    invalid_card = None
    for card in game.players[0].hand:
        if not game.can_play_card(game.players[0], card):
            invalid_card = card
            break
    assert game.play_card(game.players[0], invalid_card) == False

# Test next_turn function
def test_next_turn():
    game = UnoGame(human_number=1, com_number=1)
    game.start_game()
    current_player = game.get_current_player()
    game.next_turn()
    next_player = game.get_current_player()
    assert current_player != next_player

# Test auto_turn for computer player
def test_auto_turn():
    game = UnoGame(human_number=1, com_number=1)
    game.start_game()
    game.next_turn()  # Switch to computer player
    current_player = game.get_current_player()
    game.auto_turn(current_player)
    assert current_player.hand != 7

""" 
test_uno_game_init: 덱에 있는 카드의 수가 예상과 다릅니다. 104 대신 108이 나와야 합니다. 게임 초기화 또는 카드 생성 과정에서 문제가 발생한 것 같습니다. 덱을 생성하는 코드를 확인하고 수정해야 합니다.

test_deal_cards: 카드를 분배한 후 덱에 남아있는 카드의 수가 0이 아닌 7입니다. 카드 분배 과정에서 문제가 발생한 것 같습니다. _deal_cards 함수를 확인하고 수정해야 합니다.

test_draw_card: 카드를 뽑은 후 플레이어의 카드 수가 8이 아닌 0입니다. 카드를 뽑는 과정에서 문제가 발생한 것 같습니다. draw_card 함수를 확인하고 수정해야 합니다.

test_play_card_valid와 test_play_card_invalid: 두 테스트 케이스 모두 AttributeError: 'NoneType' object has no attribute 'color' 오류가 발생하고 있습니다. 이는 top_discard_card 함수가 None을 반환하고, 이후에 해당 카드의 color 속성에 접근하려고 시도하기 때문입니다. 게임 초기화 과정에서 덱과 버림 덱이 제대로 설정되지 않았을 수 있습니다. 초기화 과정을 확인하고 수정해야 합니다.

각 테스트 케이스의 실패 원인을 확인하고 수정하면 모든 테스트 케이스를 통과할 수 있습니다. 이를 통해 게임의 정확성과 안정성을 높일 수 있습니다.
"""