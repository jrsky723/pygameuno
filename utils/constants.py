import os

SIZE_RATIO = {"small": 3, "medium": 4, "large": 5}

# Screen properties
SCREEN_WIDTH_BASE = 320
SCREEN_HEIGHT_BASE = 180
SCREEN_WIDTH = {
    "small": SCREEN_WIDTH_BASE * SIZE_RATIO["small"],
    "medium": SCREEN_WIDTH_BASE * SIZE_RATIO["medium"],
    "large": SCREEN_WIDTH_BASE * SIZE_RATIO["large"],
}
SCREEN_HEIGHT = {
    "small": SCREEN_HEIGHT_BASE * SIZE_RATIO["small"],
    "medium": SCREEN_HEIGHT_BASE * SIZE_RATIO["medium"],
    "large": SCREEN_HEIGHT_BASE * SIZE_RATIO["large"],
}

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GRAY = (40, 40, 40)

# Default colors
BACKGROUND_COLOR = DARK_GRAY
TEXT_COLOR = WHITE

# Font properties
FONT_SIZE_BASE = 10
FONT_SIZES = {
    "small": FONT_SIZE_BASE * SIZE_RATIO["small"],
    "medium": FONT_SIZE_BASE * SIZE_RATIO["medium"],
    "large": FONT_SIZE_BASE * SIZE_RATIO["large"],
}

# Card properties
CARD_WIDTH_BASE = 30
CARD_HEIGHT_BASE = 40
CARD_WIDTH = {
    "small": CARD_WIDTH_BASE * SIZE_RATIO["small"],
    "medium": CARD_WIDTH_BASE * SIZE_RATIO["medium"],
    "large": CARD_WIDTH_BASE * SIZE_RATIO["large"],
}
CARD_HEIGHT = {
    "small": CARD_HEIGHT_BASE * SIZE_RATIO["small"],
    "medium": CARD_HEIGHT_BASE * SIZE_RATIO["medium"],
    "large": CARD_HEIGHT_BASE * SIZE_RATIO["large"],
}

CARD_COLOR = WHITE
CARD_HOVER_COLOR = YELLOW


# Button properties
BUTTON_WIDTH_BASE = 50
BUTTON_HEIGHT_BASE = 15
BUTTON_WIDTH = {
    "small": BUTTON_WIDTH_BASE * SIZE_RATIO["small"],
    "medium": BUTTON_WIDTH_BASE * SIZE_RATIO["medium"],
    "large": BUTTON_WIDTH_BASE * SIZE_RATIO["large"],
}
BUTTON_HEIGHT = {
    "small": BUTTON_HEIGHT_BASE * SIZE_RATIO["small"],
    "medium": BUTTON_HEIGHT_BASE * SIZE_RATIO["medium"],
    "large": BUTTON_HEIGHT_BASE * SIZE_RATIO["large"],
}
BUTTON_TEXT_COLOR = WHITE
BUTTON_COLOR = BLUE
BUTTON_HOVER_COLOR = GREEN

# Directories
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
CARD_IMAGES_DIR = os.path.join(ASSETS_DIR, "card_images")
