import pygame
from utils.constants import TEXT_COLOR, FONT_SIZES

# Font directory
FONTS_DIR = "assets/fonts"


def load_font(font_name, font_size):
    font_path = f"{FONTS_DIR}/{font_name}.ttf"
    return pygame.font.Font(font_path, font_size)


def get_text_surface(text, font_name, font_size, color=TEXT_COLOR):
    if font_size in FONT_SIZES:
        font_size = FONT_SIZES[font_size]

    font = load_font(font_name, font_size)
    return font.render(text, True, color)
