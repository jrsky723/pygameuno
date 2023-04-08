from renders.text_box import TextBox
from utils.constants import CARD as C
from utils.color_conversion import darken_color


class Card(TextBox):
    def __init__(
        self,
        x,
        y,
        text,
        color,
        screen_size,
        color_blind,
        font_size=C.FONT_SIZE,
        text_color=C.TEXT_COLOR,
        width=C.WIDTH,
        height=C.HEIGHT,
    ):
        if color == "black":
            text_color = "white"
        super().__init__(
            x,
            y,
            text,
            screen_size,
            color_blind,
            True,  # resize
            True,  # reposition
            width,
            height,
            font_size,
            text_color,
            color,  # background_color
            border_width=3,
        )
        self.origin_background_color = self.background_color
        self.origin_text_color = self.text_color
        self.hovered_backgound_color = darken_color(self.background_color)
        self.hovered_text_color = darken_color(self.text_color)
        self.hovered = False

    def draw(self, screen):
        super().draw(screen)
        # draw border

    def update(self):
        super().update()
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
