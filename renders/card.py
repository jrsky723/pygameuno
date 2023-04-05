from renders.text_box import TextBox
from utils.constants import CARD as C, SIZE_RATIO
from utils.color_conversion import darken_color


class Card(TextBox):
    def __init__(
        self,
        x,
        y,
        text,
        color,
        font_size=C.FONT_SIZE,
        text_color=C.TEXT_COLOR,
        width=C.WIDTH,
        height=C.HEIGHT,
        screen_size="medium",
        color_blind=False,
    ):
        super().__init__(
            x=x,
            y=y,
            text=text,
            font_size=font_size,
            text_color=text_color,
            width=width,
            height=height,
            background_color=color,
            screen_size=screen_size,
            color_blind=color_blind,
        )
        self.origin_background_color = self.background_color
        self.origin_text_color = self.text_color
        self.hovered_backgound_color = darken_color(self.background_color)
        self.hovered_text_color = darken_color(self.text_color)
        self.hovered = False

    def draw(self, screen):
        super().draw(screen)

    def update(self):
        if self.hovered:
            self.background_color = self.hovered_backgound_color
            self.text_color = self.hovered_text_color
        else:
            self.background_color = self.origin_background_color
            self.text_color = self.origin_text_color
        super().update()

    def hover(self):
        self.hovered = True

    def unhover(self):
        self.hovered = False
