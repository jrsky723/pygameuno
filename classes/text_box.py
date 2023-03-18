import pygame
from utils.fonts import get_text_surface
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, TEXT_COLOR


class TextBox:
    def __init__(
        self,
        x,
        y,
        size,
        text,
        text_color=TEXT_COLOR,
        width=False,
        height=False,
        background_color=False,
    ):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.text_color = text_color
        self.text_surface = get_text_surface(
            self.text, "Arial", self.size, self.text_color
        )
        if width:
            self.width = width
        else:
            self.width = self.text_surface.get_width()
        if height:
            self.height = height
        else:
            self.height = self.text_surface.get_height()
        if self.x == "center":
            self.x = (SCREEN_WIDTH[self.size] - self.width) / 2
        if x == "right":
            self.x = SCREEN_WIDTH[self.size] - self.width
        if y == "center":
            self.y = (SCREEN_HEIGHT[self.size] - self.height) / 2
        if self.y == "bottom":
            self.y = SCREEN_HEIGHT[self.size] - self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.background_color = background_color

    def draw(self, screen):
        if self.background_color:
            pygame.draw.rect(screen, self.background_color, self.rect)
        screen.blit(self.text_surface, self.rect)
