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
        # inner border
        border_color="white",  # inner border color
        border_width=0,
    ):
        if x == "center":
            x = (S.WIDTH_BASE - width) / 2
        if y == "center":
            y = (S.HEIGHT_BASE - height) / 2
        if x == "right":
            x = S.WIDTH_BASE - width
        if y == "bottom":
            y = S.HEIGHT_BASE - height
        self.width = width * SIZE_RATIO[screen_size]
        self.height = height * SIZE_RATIO[screen_size]
        self.x = x * SIZE_RATIO[screen_size]
        self.y = y * SIZE_RATIO[screen_size]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.background_color = (
            rgb(background_color, color_blind) if background_color else None
        )
        self.border_width = int(border_width * SIZE_RATIO[screen_size])
        self.border_color = rgb(border_color, color_blind)

    def draw(self, screen):
        if self.background_color is not None:
            pygame.draw.rect(screen, self.background_color, self.rect)
            # draw inner border
        if self.border_width > 0:
            pygame.draw.rect(
                screen,
                self.border_color,
                self.rect,
                self.border_width,
            )

    def is_on_mouse(self, pos):
        return self.rect.collidepoint(pos)

    def click(self):
        pass

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pass
