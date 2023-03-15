import os

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (40, 40, 40)
TEXT_COLOR = WHITE

# Card properties
CARD_WIDTH = 70
CARD_HEIGHT = 100
CARD_SIZE = (CARD_WIDTH, CARD_HEIGHT)
CARD_CENTER = (CARD_WIDTH // 2, CARD_HEIGHT // 2)

# Button properties
BUTTON_COLOR = BLUE
BUTTON_HOVER_COLOR = GREEN

# Directories
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
CARD_IMAGES_DIR = os.path.join(ASSETS_DIR, "card_images")
