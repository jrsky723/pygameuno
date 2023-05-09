import pytest
from utils.color_conversion import darken_color, get_color_by_name, rgb, random_rgb
from utils.constants import COLOR_BLIND_FRIENDLY_COLORS_DICT, COLORS_DICT

def test_darken_color():
    original_color = (255, 255, 255)
    darkened_color = darken_color(original_color)
    assert darkened_color == (127.5, 127.5, 127.5)

def test_get_color_by_name():
    color_name = 'red'
    normal_color = get_color_by_name(color_name, False)
    assert normal_color == COLORS_DICT[color_name]
    color_blind_friendly_color = get_color_by_name(color_name, True)
    assert color_blind_friendly_color == COLOR_BLIND_FRIENDLY_COLORS_DICT[color_name]

def test_rgb():
    color_name = 'blue'
    normal_color = rgb(color_name, False)
    assert normal_color == COLORS_DICT[color_name]
    color_blind_friendly_color = rgb(color_name, True)
    assert color_blind_friendly_color == COLOR_BLIND_FRIENDLY_COLORS_DICT[color_name]

    color_tuple = (255, 0, 0)
    assert rgb(color_tuple) == color_tuple

def test_random_rgb():
    color1 = random_rgb()
    color2 = random_rgb()
    assert isinstance(color1, tuple)
    assert len(color1) == 3
    assert color1 != color2