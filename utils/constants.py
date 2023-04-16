import os

SIZE_RATIO = {"small": 3 / 4, "medium": 1, "large": 5 / 4}


# Screen properties
class SCREEN:
    WIDTH_BASE = 1280
    HEIGHT_BASE = 720
    TITLE_Y = 80
    WIDTH = {"small": 960, "medium": 1280, "large": 1600}
    HEIGHT = {"small": 540, "medium": 720, "large": 900}
    SIZE = {
        "small": (WIDTH["small"], HEIGHT["small"]),
        "medium": (WIDTH["medium"], HEIGHT["medium"]),
        "large": (WIDTH["large"], HEIGHT["large"]),
    }
    BACKGROUND_COLOR = (50, 50, 50)
    FONT_SIZE = 30


# Colors
COLORS_DICT = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 50, 50),
    "green": (50, 255, 50),
    "blue": (50, 50, 255),
    "yellow": (255, 255, 50),
    "dark_gray": (50, 50, 50),
}
COLOR_BLIND_FRIENDLY_COLORS_DICT = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (216, 27, 96),
    "green": (17, 218, 197),
    "blue": (30, 136, 229),
    "yellow": (255, 193, 7),
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
    FONT_SIZE = 38
    TEXT_COLOR = "black"
    BACKGROUND_COLOR = "black"
    BACK_COLOR = "black"


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
    BORDER_COLOR = "white"


class TEXTBOX:
    FONT_SIZE = 60
    TEXT_COLOR = "white"
    BORDER_COLOR = "white"


# Directories
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
CARD_IMAGES_DIR = os.path.join(ASSETS_DIR, "card_images")
