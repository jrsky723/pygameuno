import pygame
import pytest

from renders.card import Card


@pytest.fixture
def card():
    return Card(0, 0, "card", "medium", False)


def test_card_init(card):
    assert card.x == 0
    assert card.y == 0
    assert card.text == "C"
    assert card.font_size == 40
    assert card.text_color == (0, 0, 0)
    assert card.background_color == (255, 255, 255)
    assert card.border_color == (0, 0, 0)
    assert card.border_width == 3
    assert card.hovered == False
    assert card.face_up == True


def test_card_flip(card):
    card.face_down()
    assert card.get_face_up() == False
    assert card.text == ""
    assert card.background_color == (0, 0, 0)
    assert card.border_color == (255, 255, 255)

    card.face_up()
    assert card.get_face_up() == True
    assert card.text == "C"
    assert card.background_color == (255, 255, 255)
    assert card.border_color == (0, 0, 0)


def test_card_hover(card):
    card.hover()
    assert card.hovered == True
    assert card.border_color == (255, 255, 255)

    card.unhover()
    assert card.hovered == False
    assert card.border_color == (0, 0, 0)


def test_card_get_card(card):
    assert card.get_card() == "card"
