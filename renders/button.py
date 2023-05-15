from utils.color_conversion import rgb, darken_color
from renders.text_box import TextBox
from utils.constants import BUTTON as B


class Button(TextBox):
    def __init__(
        self,
        x,
        y,
        screen_size,
        color_blind,
        text="",
        reposition=True,
        resize=True,
        width=B.WIDTH,
        height=B.HEIGHT,
        font_size=B.FONT_SIZE,
        text_color=B.TEXT_COLOR,
        background_color=B.COLOR,
        border_color=B.BORDER_COLOR,
        border_width=0,
        hover_background_color=B.HOVER_COLOR,
        hover_text_color=B.TEXT_HOVER_COLOR,
        select_background_color=B.SELECT_COLOR,
        select_text_color=B.TEXT_SELECT_COLOR,
    ):
        super().__init__(
            x,
            y,
            text,
            screen_size,
            color_blind,
            reposition,
            resize,
            width,
            height,
            font_size,
            text_color,
            background_color,
            border_color,
            border_width,
        )
        self.origin_background_color = self.background_color
        self.origin_text_color = self.text_color
        if hover_background_color == "darken":
            self.hover_background_color = darken_color(self.background_color)
        else:
            self.hover_background_color = rgb(hover_background_color, color_blind)
        self.hover_text_color = rgb(hover_text_color, color_blind)
        self.select_background_color = rgb(select_background_color, color_blind)
        self.select_text_color = rgb(select_text_color, color_blind)
        self.disable_text_color = rgb(B.TEXT_DISABLE_COLOR)
        self.hovered = False
        self.selected = False
        self.clicked = False

    def draw(self, screen):
        super().draw(screen)

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
