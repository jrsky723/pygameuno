import pytest
import pygame
from unittest.mock import Mock
from renders.input_box import InputBox
from utils.constants import INPUTBOX as I

pygame.init()
pygame.font.init()


def test_init():
    input_box = InputBox(0, 0, (800, 600), False)

    assert input_box.x == 0
    assert input_box.y == 0
    assert input_box.screen_size == (800, 600)
    assert input_box.color_blind == False
    assert input_box.text == ""
    assert input_box.placeholder == ""
    assert input_box.origin_border_width == I.BORDER_WIDTH
    assert input_box.hovered_border_width == I.HOVERED_BORDER_WIDTH
    assert input_box.selected_border_width == I.SELECTED_BORDER_WIDTH

def test_update():
    input_box = InputBox(0, 0, (800, 600), False, text="Test")
    input_box.update()

    assert input_box.background_color == I.BACKGROUND_COLOR
    assert input_box.text_color == I.TEXT_COLOR
    assert input_box.border_width == I.BORDER_WIDTH

    input_box.hovered = True
    input_box.update()
    assert input_box.background_color == I.BACKGROUND_COLOR
    assert input_box.text_color == I.TEXT_COLOR
    assert input_box.border_width == I.HOVERED_BORDER_WIDTH

    input_box.clicked = True
    input_box.update()
    assert input_box.background_color == I.BACKGROUND_COLOR
    assert input_box.text_color == I.TEXT_COLOR
    assert input_box.border_width == I.SELECTED_BORDER_WIDTH

def test_select():
    input_box = InputBox(0, 0, (800, 600), False, text="Test")
    input_box.select()

    assert input_box.text == ""

def test_delete():
    input_box = InputBox(0, 0, (800, 600), False, text="Test")
    input_box.delete()

    assert input_box.text == "Tes"

def test_add():
    input_box = InputBox(0, 0, (800, 600), False, text="Test")
    input_box.add("a")

    assert input_box.text == "Testa"

    input_box.add("b")
    assert input_box.text == "Testab"
