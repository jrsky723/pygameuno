import pytest
from game.uno_player import UnoPlayer
from game.uno_card import UnoCard  # Assuming you have an UnoCard class in a file named uno_card.py

@pytest.fixture
def setup_players():
    UnoPlayer.init()
    player1 = UnoPlayer("Alice")
    player2 = UnoPlayer("Bob")
    return player1, player2

def test_initialization(setup_players):
    player1, _ = setup_players
    assert player1.get_name() == "Alice"
    assert player1.get_id() == 0
    assert player1.get_hand_size() == 0
    assert not player1.get_is_turn()

def test_add_card(setup_players):
    player1, _ = setup_players
    card = UnoCard("red", 5)
    player1.add_card(card)
    assert player1.get_hand_size() == 1
    assert player1.get_hand()[0] == card

def test_can_play(setup_players):
    player1, _ = setup_players
    card1 = UnoCard("red", 5)
    card2 = UnoCard("blue", 5)
    card3 = UnoCard("red", 7)
    player1.add_card(card1)
    player1.add_card(card2)
    player1.add_card(card3)

    assert player1.can_play("red", 5)
    assert player1.can_play("blue", 5)
    assert not player1.can_play("blue", 6)

def test_play_card(setup_players):
    player1, _ = setup_players
    card = UnoCard("red", 5)
    player1.add_card(card)
    player1.play_card(card)
    assert player1.get_hand_size() == 0

def test_auto_card(setup_players):
    player1, _ = setup_players
    card1 = UnoCard("red", 5)
    card2 = UnoCard("blue", 5)
    card3 = UnoCard("red", 7)
    player1.add_card(card1)
    player1.add_card(card2)
    player1.add_card(card3)

    auto_card = player1.auto_card("red", 5)
    assert auto_card == card1
    auto_card = player1.auto_card("blue", 5)
    assert auto_card == card2
    auto_card = player1.auto_card("green", 7)
    assert auto_card is None

def test_is_human(setup_players):
    player1, _ = setup_players
    assert player1.is_human()
