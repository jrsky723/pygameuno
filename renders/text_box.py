from renders.rect import Rect
from utils.constants import TEXTBOX as T, SIZE_RATIO
from utils.color_conversion import rgb
from utils.fonts import get_text_surface


class TextBox(Rect):
    def __init__(
        self,
        x,
        y,
        text,
        screen_size,
        color_blind,
        reposition=True,
        resize=True,
        width=0,
        height=0,
        font_size=T.FONT_SIZE,
        text_color=T.TEXT_COLOR,
        background_color=None,
        border_color=T.BORDER_COLOR,
        border_width=0,
    ):
        self.text_color = rgb(text_color, color_blind)
        temp_text_surface = get_text_surface(text, font_size, self.text_color)
        width = max(width, temp_text_surface.get_width())
        height = max(height, temp_text_surface.get_height())
        super().__init__(
            x,
            y,
            width,
            height,
            screen_size,
            color_blind,
            reposition,
            resize,
            background_color,
            border_color,
            border_width,
        )
        self.text = text
        self.font_size = font_size * SIZE_RATIO[screen_size] if resize else font_size
        self.text_surface = get_text_surface(self.text, self.font_size, self.text_color)
        self.visible = True

    def draw(self, screen):
        if self.visible == False:
            return
        super().draw(screen)
        screen.blit(
            self.text_surface,
            (
                (
                    self.x + (self.width - self.text_surface.get_width()) / 2,
                    self.y + (self.height - self.text_surface.get_height()) / 2,
                )
            ),
        )

    def update(self):
        super().update()
        self.text_surface = get_text_surface(self.text, self.font_size, self.text_color)

    def set_text(self, text):
        self.text = text
        self.update()

    def get_text(self):
        return self.text

    def set_visible(self, visible):
        self.visible = visible
