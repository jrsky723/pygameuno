import pygame
import pytest
from utils.constants import BUTTON
from utils.color_conversion import rgb


from renders.button import Button
from utils.constants import SCREEN as S, BUTTON as B


@pytest.fixture
def button():
    pygame.init()
    screen = pygame.display.set_mode((S.WIDTH_BASE, S.HEIGHT_BASE))
    return Button(
        x=0,
        y=0,
        screen_size="medium",
        color_blind=False,
        text="Test Button",
        width=B.WIDTH,
        height=B.HEIGHT,
        font_size=B.FONT_SIZE,
        text_color=B.TEXT_COLOR,
        background_color=B.COLOR,
        border_color=B.BORDER_COLOR,
        border_width=0,
        hover_background_color=B.HOVER_COLOR,
        hover_text_color=B.TEXT_HOVER_COLOR,
        select_background_color=B.SELECT_COLOR,
        select_text_color=B.TEXT_SELECT_COLOR,
    )


def test_button_hover(button):
    button.hover()
    assert button.hovered == True
    assert button.background_color == rgb(BUTTON.HOVER_COLOR, button.color_blind)
    assert button.text_color == rgb(BUTTON.TEXT_HOVER_COLOR, button.color_blind)


def test_button_select(button):
    button.select()
    assert button.selected == True
    assert button.background_color == rgb(BUTTON.SELECT_COLOR, button.color_blind)
    assert button.text_color == rgb(BUTTON.TEXT_SELECT_COLOR, button.color_blind)


def test_button_click(button):
    button.click()
    assert button.clicked == True
    assert button.background_color == rgb(BUTTON.SELECT_COLOR, button.color_blind)
    assert button.text_color == rgb(BUTTON.TEXT_SELECT_COLOR, button.color_blind)




def test_button_unhover(button):
    button.hovered = True
    button.unhover()
    assert button.hovered == False
    assert button.background_color == button.origin_background_color
    assert button.text_color == button.origin_text_color




def test_button_unselect(button):
    button.selected = True
    button.unselect()
    assert button.selected == False
    assert button.background_color == button.origin_background_color
    assert button.text_color == button.origin_text_color




def test_button_unclick(button):
    button.clicked = True
    button.unclick()
    assert button.clicked == False
    assert button.background_color == button.origin_background_color
    assert button.text_color == button.origin_text_color


def test_button_reset(button):
    button.hovered = True
    button.selected = True
    button.clicked = True
    button.reset()
    assert button.hovered == False
    assert button.selected == False
    assert button.clicked == False
    assert button.background_color == button.origin_background_color
    assert button.text_color == button.origin_text_color
