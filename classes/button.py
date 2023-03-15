import pygame
from utils.fonts import get_text_surface
from utils.color_conversion import darken_color


class Button:
    def __init__(self, x, y, width, height, text, text_color, background_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.origin_background_color = background_color
        self.background_color = background_color
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
        text_surface = get_text_surface(self.text, "Arial", "medium", self.text_color)
        screen.blit(
            text_surface,
            (
                self.rect.x + self.rect.width / 2 - text_surface.get_width() / 2,
                self.rect.y + self.rect.height / 2 - text_surface.get_height() / 2,
            ),
        )

    def is_on_mouse(self, pos):
        return self.rect.collidepoint(pos)

    def click(self):
        pass
