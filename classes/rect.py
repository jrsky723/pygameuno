import pygame
from utils.color_conversion import rgb
from utils.constants import SCREEN as S, SIZE_RATIO


class Rect:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        background_color=None,
        screen_size="medium",
        color_blind=False,
    ):
        screen_width, screen_height = S.SIZE
        if x == "center":
            x = (screen_width - width) / 2
        if y == "center":
            y = (screen_height - height) / 2
        self.width = width * SIZE_RATIO[screen_size]
        self.height = height * SIZE_RATIO[screen_size]
        self.x = x * SIZE_RATIO[screen_size]
        self.y = y * SIZE_RATIO[screen_size]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.background_color = (
            rgb(background_color, color_blind) if background_color else None
        )

    def draw(self, screen):
        if self.background_color is not None:
            pygame.draw.rect(screen, self.background_color, self.rect)

    def is_on_mouse(self, pos):
        return self.rect.collidepoint(pos)

    def click(self):
        pass

    def update(self):
        pass
