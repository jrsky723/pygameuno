import os

SIZE_RATIO = {"small": 3 / 4, "medium": 1, "large": 5 / 4}


# Screen properties
class SCREEN:
    WIDTH_BASE = 1280
    HEIGHT_BASE = 720
    SIZE = (1280, 720)
    TITLE_Y = 80
    WIDTH = {
        "small": WIDTH_BASE * SIZE_RATIO["small"],
        "medium": WIDTH_BASE * SIZE_RATIO["medium"],
        "large": WIDTH_BASE * SIZE_RATIO["large"],
    }
    HEIGHT = {
        "small": HEIGHT_BASE * SIZE_RATIO["small"],
        "medium": HEIGHT_BASE * SIZE_RATIO["medium"],
        "large": HEIGHT_BASE * SIZE_RATIO["large"],
    }
    BACKGROUND_COLOR = (30, 30, 30)
    FONT_SIZE = 30


# Colors
COLORS_DICT = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "dark_gray": (40, 40, 40),
}
COLOR_BLIND_FRIENDLY_COLORS_DICT = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "dark_gray": (40, 40, 40),
}

COLORS = COLORS_DICT.keys()
COLOR_BLIND_FRIENDLY_COLORS = COLOR_BLIND_FRIENDLY_COLORS_DICT.keys()

# Font properties
FONT_SIZE_BASE = 10
FONT_SIZES = {
    "small": FONT_SIZE_BASE * SIZE_RATIO["small"],
    "medium": FONT_SIZE_BASE * SIZE_RATIO["medium"],
    "large": FONT_SIZE_BASE * SIZE_RATIO["large"],
}


# Card properties
class CARD:
    WIDTH = 100
    HEIGHT = 150


# Button properties
class BUTTON:
    WIDTH = 180
    HEIGHT = 60
    FONT_SIZE = 40
    COLOR = "black"
    HOVER_COLOR = "green"
    SELECT_COLOR = "red"
    TEXT_COLOR = "green"
    TEXT_HOVER_COLOR = "black"
    TEXT_SELECT_COLOR = "white"


class TEXTBOX:
    FONT_SIZE = 60
    TEXT_COLOR = "white"


# Directories
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
CARD_IMAGES_DIR = os.path.join(ASSETS_DIR, "card_images")
