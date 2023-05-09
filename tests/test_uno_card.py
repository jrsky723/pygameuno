import pytest
from game.uno_card import UnoCard


def test_uno_card_init():
    card = UnoCard("number", "red", 5)
    assert card.type == "number"
    assert card.color == "red"
    assert card.value == 5


def test_uno_card_get_abb():
    card1 = UnoCard("number", "red", 5)
    card2 = UnoCard("special", "blue", "skip")
    assert card1.get_abb() == 5
    assert card2.get_abb() == "S"


def test_uno_card_get_color():
    card = UnoCard("special", "blue", "reverse")
    assert card.get_color() == "blue"
