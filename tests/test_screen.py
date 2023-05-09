""" import pygame
import pytest

from utils.constants import SCREEN as S
from screens.screen import Screen


@pytest.fixture(scope='module')
def screen():
    pygame.init()
    return pygame.display.set_mode((S.WIDTH_BASE, S.HEIGHT_BASE))


def test_screen_init(screen):
    # Given
    clock = pygame.time.Clock()
    options = {
        "screen_size": "medium",
        "color_blind": False,
        "key_bindings": {
            "up": "up",
            "down": "down",
            "left": "left",
            "right": "right",
            "return": "return",
        },
        "sound": {
            "volume": 50,
            "music": 50,
            "effects": 50,
        },
    }

    # When
    screen_object = Screen(screen=screen, clock=clock, options=options)

    # Then
    assert screen_object.screen == screen
    assert screen_object.options == options
    assert screen_object.clock == clock
    assert screen_object.screen_size == options["screen_size"]
    assert screen_object.color_blind == options["color_blind"]
    assert screen_object.key_bindings == options["key_bindings"]
    assert screen_object.sound == options["sound"]
    assert screen_object.rect_params == {
        "screen_size": options["screen_size"],
        "color_blind": options["color_blind"],
    }
    assert screen_object.screen_width == S.WIDTH_BASE
    assert screen_object.screen_height == S.HEIGHT_BASE
    assert screen_object.background_color == (50, 50, 50)
    assert screen_object.running == True
    assert screen_object.background_music_volume == 0.25
    assert screen_object.sound_effects_volume == 0.25
"""

import pytest
import pygame
from unittest.mock import Mock
from screens.screen import Screen
from utils.constants import SCREEN as S

options = {
    "screen_size": (800, 600),
    "color_blind": False,
    "key_bindings": {"up": "w", "down": "s", "left": "a", "right": "d", "return": "return"},
    "sound": {"volume": 100, "music": 50, "effects": 50},
}

pygame.init()
screen = pygame.display.set_mode(options["screen_size"])
clock = pygame.time.Clock()


def test_init():
    test_screen = Screen(screen, clock, options)

    assert test_screen.screen_size == options["screen_size"]
    assert test_screen.color_blind == options["color_blind"]
    assert test_screen.key_bindings == options["key_bindings"]
    assert test_screen.sound == options["sound"]
    assert test_screen.background_color == S.BACKGROUND_COLOR
    assert test_screen.running == True


def test_update():
    test_screen = Screen(screen, clock, options)
    test_screen.update()

    assert test_screen.screen.get_size() == options["screen_size"]


def test_quit():
    test_screen = Screen(screen, clock, options)
    test_screen.quit = Mock()

    test_screen.quit()
    test_screen.quit.assert_called_once()
