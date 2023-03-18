import pygame
from utils.fonts import get_text_surface
from utils.color_conversion import darken_color
from classes.text_box import TextBox
from utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_TEXT_COLOR,
    BUTTON_COLOR,
)


class Button(TextBox):
    def __init__(
        self,
        x,
        y,
        size,
        text,
        text_color=False,
        width=False,
        height=False,
        background_color=False,
    ):
        if not text_color:
            text_color = BUTTON_TEXT_COLOR
        if not background_color:
            background_color = BUTTON_COLOR
        if not width:
            width = BUTTON_WIDTH[size]
        if not height:
            height = BUTTON_HEIGHT[size]
        super().__init__(x, y, size, text, text_color, width, height, background_color)
        self.origin_background_color = background_color
        self.darken_amount = 0.5
        self.darken_background_color = darken_color(
            self.background_color, self.darken_amount
        )

    def draw(self, screen, selected):
        if selected:
            self.background_color = self.darken_background_color
        else:
            self.background_color = self.origin_background_color
        pygame.draw.rect(screen, self.background_color, self.rect)
        screen.blit(
            self.text_surface,
            (
                self.x + (self.width - self.text_surface.get_width()) / 2,
                self.y + (self.height - self.text_surface.get_height()) / 2,
            ),
        )

    def is_on_mouse(self, pos):
        return self.rect.collidepoint(pos)

    def click(self):
        pass
