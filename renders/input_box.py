from renders.button import Button
from utils.constants import INPUTBOX as I


class InputBox(Button):
    def __init__(
        self,
        x,
        y,
        screen_size,
        color_blind,
        text="",
        reposition=True,
        resize=True,
        width=I.WIDTH,
        height=I.HEIGHT,
        font_size=I.FONT_SIZE,
        text_color=I.TEXT_COLOR,
        background_color=I.BACKGROUND_COLOR,
        border_color=I.BORDER_COLOR,
        border_width=I.BORDER_WIDTH,
    ):
        super().__init__(
            x,
            y,
            screen_size,
            color_blind,
            text,
            reposition,
            resize,
            width,
            height,
            font_size,
            text_color,
            background_color,
            border_color,
            border_width,
            hover_background_color=background_color,
            hover_text_color=text_color,
            select_background_color=background_color,
            select_text_color=text_color,
        )
        self.origin_border_width = self.border_width
        self.hovered_border_width = I.HOVERED_BORDER_WIDTH
        self.selected_border_width = I.SELECTED_BORDER_WIDTH
        self.placeholder = text

    def update(self):
        super().update()
        if self.clicked:
            self.background_color = self.select_background_color
            self.text_color = self.select_text_color
            self.border_width = self.selected_border_width
        elif self.selected:
            self.background_color = self.select_background_color
            self.text_color = self.select_text_color
            self.border_width = self.selected_border_width
        elif self.hovered:
            self.background_color = self.hover_background_color
            self.text_color = self.hover_text_color
            self.border_width = self.hovered_border_width
        else:
            self.background_color = self.origin_background_color
            self.text_color = self.origin_text_color
            self.border_width = self.origin_border_width

    def select(self):
        super().select()
        if self.text == self.placeholder:
            self.text = ""

    def unselect(self):
        super().unselect()
        self.placeholder = self.text

    def delete(self):
        if self.text != "":
            self.text = self.text[:-1]

    def add(self, char):
        # check max length with text_surface and widh
        if self.text_surface.get_width() < self.width - self.border_width * 2:
            self.text += char
