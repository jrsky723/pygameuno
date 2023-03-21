from utils.constants import (
    COLOR_BLIND_FRIENDLY_COLORS_DICT,
    COLORS_DICT,
)


def darken_color(color, amount):
    return tuple([max(0, c * amount) for c in color])


def get_color_by_name(color_name, color_blind):
    if color_blind:
        return COLOR_BLIND_FRIENDLY_COLORS_DICT[color_name]
    return COLORS_DICT[color_name]


# change color(name) to rgb, by color_blind, if rgb -> rgb
def rgb(color, color_blind=False):
    if isinstance(color, str):
        color = get_color_by_name(color, color_blind)
    return color
