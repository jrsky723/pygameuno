import pygame

# Font directory
FONTS_DIR = "assets/fonts"

# Font sizes
FONT_SIZES = {"small": 20, "medium": 30, "large": 40}

# Font colors
TEXT_COLOR = (255, 255, 255)


def load_font(font_name, font_size):
    font_path = f"{FONTS_DIR}/{font_name}.ttf"
    return pygame.font.Font(font_path, font_size)


def get_text_surface(text, font_name, font_size, color=TEXT_COLOR):
    if font_size in FONT_SIZES:
        font_size = FONT_SIZES[font_size]

    font = load_font(font_name, font_size)
    return font.render(text, True, color)
