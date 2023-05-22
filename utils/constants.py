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
    FPS = 60


# PATHS

SOUNDS_PATH = os.path.join("assets", "sounds")
IMAGES_PATH = os.path.join("assets", "images")


class SOUND:
    # SOUND
    BUTTON_CLICK = os.path.join(SOUNDS_PATH, "button_click.mp3")
    CARD_MOVE = os.path.join(SOUNDS_PATH, "card_move.mp3")
    CARD_FLIP = os.path.join(SOUNDS_PATH, "card_flip.mp3")
    ERROR = os.path.join(SOUNDS_PATH, "error.mp3")
    UNO = os.path.join(SOUNDS_PATH, "uno.mp3")
    FAILED = os.path.join(SOUNDS_PATH, "failed.mp3")
    # change path to os path


class MUSIC:
    MENU_BACKGROUND = os.path.join(SOUNDS_PATH, "sinnesloschen-beam.mp3")
    GAME_BACKGROUND = os.path.join(SOUNDS_PATH, "cool-jazz-loops-2641.mp3")
    RED_ZONE_BACKGROUND = os.path.join(SOUNDS_PATH, "japan-koto-folk-background-music-124876.mp3")
    GREEN_ZONE_BACKGROUND = os.path.join(SOUNDS_PATH, "secret-garden-mystically-chill-out-music-7489.mp3")
    YELLOW_ZONE_BACKGROUND = os.path.join(SOUNDS_PATH, "middle-east-127104.mp3")
    BLUE_ZONE_BACKGROUND = os.path.join(SOUNDS_PATH, "cinematic-landscape-118672.mp3")


class IMAGE:
    STORY_MODE = os.path.join(IMAGES_PATH, "story_mode.png")
    CROWN = os.path.join(IMAGES_PATH, "crown.png")
    RED_ZONE = os.path.join(IMAGES_PATH, "red_zone.png")
    GREEN_ZONE = os.path.join(IMAGES_PATH, "green_zone.png")
    YELLOW_ZONE = os.path.join(IMAGES_PATH, "yellow_zone.png")
    BLUE_ZONE = os.path.join(IMAGES_PATH, "blue_zone.png")


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
    TEXT_DISABLE_COLOR = "dark_gray"


class TEXTBOX:
    FONT = "Commodore-64-v6.3"
    FONT_SIZE = 60
    TEXT_COLOR = "white"
    BORDER_COLOR = "white"


class INPUTBOX:
    FONT_SIZE = 40
    TEXT_COLOR = "white"
    BORDER_COLOR = "white"
    BACKGROUND_COLOR = "black"
    WIDTH = 300
    HEIGHT = 60
    BORDER_WIDTH = 0
    HOVERED_BORDER_WIDTH = 2
    SELECTED_BORDER_WIDTH = 4

## Story mode constants

STORY_MODE_DESCRIPTION = {
    "red_zone": [
        "Match with 1 computer player",
        "On first distribution, the computer player",
        "will receive a 50% higher chance of receiving",
        "a skill card. And a combo that allows a computer",
        "player to play two or more cards (REVERSE, SKIP)",
    ],
    "green_zone": [
        "Match with 3 computer players.",
        "Distribute all cards to the same number of ",
        "players except for the first card.",
    ],
    "yellow_zone": [
        "Match with 2 computer players.",
        "Randomly changed the color of the card ",
        "that can be paid every 5 turns.",
    ],
    "blue_zone": [
        "In this area, at the end of each player's turn,",
        "the reload probability increases by a certain level.",
        "When a reload occurs, the player reloads all of his",
        "cards at the start of the turn.",
    ],
}

STORY_MODE_COMS = {
    "red_zone": [{"name": "RED KING", "is_com": True}],
    "green_zone": [
        {"name": "GREEN KING", "is_com": True},
        {"name": "GREEN QUEEN", "is_com": True},
        {"name": "GREEN JACK", "is_com": True},
    ],
    "yellow_zone": [
        {"name": "YELLOW KING", "is_com": True},
        {"name": "YELLOW QUEEN", "is_com": True},
    ],
    "blue_zone": [
        {"name": "BLUE KING", "is_com": True},
        {"name": "BLUE QUEEN", "is_com": True},
        {"name": "BLUE JACK", "is_com": True},
        {"name": "BLUE ACE", "is_com": True},
    ],
}
