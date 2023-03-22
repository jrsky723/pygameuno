import pygame


# Font directory
FONTS_DIR = "assets/fonts"
FONT = "Commodore-64-v6.3"


def load_font(font_name, font_size):
    font_path = f"{FONTS_DIR}/{font_name}.ttf"
    return pygame.font.Font(font_path, int(font_size))


def get_text_surface(
    text,
    font_size,
    color,
    font_name=FONT,
):
    font = load_font(font_name, font_size)
    return font.render(text, True, color)
