from classes.rect import Rect
from utils.constants import TEXTBOX as T, SIZE_RATIO
from utils.color_conversion import rgb
from utils.fonts import get_text_surface


class TextBox(Rect):
    def __init__(
        self,
        x,
        y,
        text,
        font_size=T.FONT_SIZE,
        text_color=T.TEXT_COLOR,
        width=0,
        height=0,
        background_color=None,
        screen_size="medium",
        color_blind=False,
    ):
        self.text = text
        self.font_size = font_size * SIZE_RATIO[screen_size]
        self.text_color = rgb(text_color, color_blind)
        temp_text_surface = get_text_surface(text, font_size, self.text_color)
        self.width = max(width, temp_text_surface.get_width())
        self.height = max(height, temp_text_surface.get_height())
        self.text_surface = get_text_surface(text, self.font_size, self.text_color)
        super().__init__(
            x=x,
            y=y,
            width=self.width,
            height=self.height,
            background_color=background_color,
            screen_size=screen_size,
            color_blind=color_blind,
        )

    def draw(self, screen):
        super().draw(screen)
        screen.blit(
            self.text_surface,
            (
                self.x + (self.width - self.text_surface.get_width()) / 2,
                self.y + (self.height - self.text_surface.get_height()) / 2,
            ),
        )
