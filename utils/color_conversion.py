import random

from utils.constants import (
    COLOR_BLIND_FRIENDLY_COLORS_DICT,
    COLORS_DICT,
)


# change color by (0.5)
def darken_color(color):
    return tuple([max(0, c * 0.5) for c in color])


def get_color_by_name(color_name, color_blind):
    if color_blind:
        return COLOR_BLIND_FRIENDLY_COLORS_DICT[color_name]
    return COLORS_DICT[color_name]


# change color(name) to rgb, by color_blind, if rgb -> rgb
def rgb(color, color_blind=False):
    if isinstance(color, str):
        color = get_color_by_name(color, color_blind)
    return color


def random_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
