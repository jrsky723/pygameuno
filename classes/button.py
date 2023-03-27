import pygame
from utils.fonts import get_text_surface
from utils.color_conversion import rgb
from classes.rect import Rect
from utils.constants import BUTTON as B, SIZE_RATIO


class Button(Rect):
    def __init__(
        self,
        x,
        y,
        text="",
        width=B.WIDTH,
        height=B.HEIGHT,
        font_size=B.FONT_SIZE,
        background_color=B.COLOR,
        text_color=B.TEXT_COLOR,
        screen_size="medium",
        color_blind=False,
        hover_background_color=B.HOVER_COLOR,
        hover_text_color=B.TEXT_HOVER_COLOR,
        select_background_color=B.SELECT_COLOR,
        select_text_color=B.TEXT_SELECT_COLOR,
    ):
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            background_color=background_color,
            screen_size=screen_size,
            color_blind=color_blind,
        )
        self.text = text
        self.font_size = font_size * SIZE_RATIO[screen_size]
        self.text_color = rgb(text_color, color_blind)
        temp_text_surface = get_text_surface(self.text, self.font_size, self.text_color)
        self.width = max(self.width, temp_text_surface.get_width())
        self.height = max(self.height, temp_text_surface.get_height())
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.origin_background_color = self.background_color
        self.origin_text_color = self.text_color
        self.hover_background_color = rgb(hover_background_color, color_blind)
        self.hover_text_color = rgb(hover_text_color, color_blind)
        self.select_background_color = rgb(select_background_color, color_blind)
        self.select_text_color = rgb(select_text_color, color_blind)
        self.hovered = False
        self.selected = False
        self.clicked = False

    def draw(self, screen):
        super().draw(screen)
        text_surface = get_text_surface(self.text, self.font_size, self.text_color)
        screen.blit(
            text_surface,
            (
                (
                    self.x + (self.width - text_surface.get_width()) / 2,
                    self.y + (self.height - text_surface.get_height()) / 2,
                ),
            ),
        )

    def update(self):
        super().update()
        if self.clicked:
            self.background_color = self.select_background_color
            self.text_color = self.select_text_color
        elif self.hovered:
            self.background_color = self.hover_background_color
            self.text_color = self.hover_text_color
        elif self.selected:
            self.background_color = self.select_background_color
            self.text_color = self.select_text_color
        else:
            self.background_color = self.origin_background_color
            self.text_color = self.origin_text_color

    def hover(self):
        self.hovered = True

    def unhover(self):
        self.hovered = False

    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def click(self):
        self.clicked = True

    def unclick(self):
        self.clicked = False

    def reset(self):
        self.hovered = False
        self.selected = False
        self.clicked = False
