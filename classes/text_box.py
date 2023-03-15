import pygame
from utils.fonts import get_text_surface

class TextBox:
    def __init__(self, x, y, width, height, text, text_color, background_color=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def draw(self, screen):
        if self.background_color:
            pygame.draw.rect(screen, self.background_color, self.rect)
        text_surface = get_text_surface(self.text, "Arial", "medium", self.text_color)
        screen.blit(
            text_surface,
            (
                self.rect.x + self.rect.width / 2 - text_surface.get_width() / 2,
                self.rect.y + self.rect.height / 2 - text_surface.get_height() / 2,
            ),
        )