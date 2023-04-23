from renders.text_box import TextBox
from utils.constants import CARD as C
from utils.color_conversion import rgb


class Card(TextBox):
    def __init__(
        self,
        x,
        y,
        card,
        screen_size,
        color_blind,
        face_up=True,
        font_size=C.FONT_SIZE,
        text_color=C.TEXT_COLOR,
        width=C.WIDTH,
        height=C.HEIGHT,
    ):
        self.card = card
        if card.get_color() == "black":
            text_color = "white"
        super().__init__(
            x,
            y,
            card.get_abb(),
            screen_size,
            color_blind,
            True,  # resize
            True,  # reposition
            width,
            height,
            font_size,
            text_color,
            card.get_color(),  # background_color
            border_width=3,
        )
        self.hovered = False
        self.face_up = face_up
        if self.face_up == False:
            self.face_down()

    def draw(self, screen):
        super().draw(screen)
        # draw border

    def update(self):
        super().update()

    def hover(self):
        self.hovered = True

    def unhover(self):
        self.hovered = False

    def flip(self):
        if self.face_up:
            self.face_down()
        else:
            self.face_up()

    def face_down(self):
        self.face_up = False
        self.background_color = rgb("black", self.color_blind)
        self.text = ""

    def face_up(self):
        self.face_up = True
        self.background_color = self.origin_background_color
        self.text = self.card.get_abb()

    def get_face_up(self):
        return self.face_up

    def get_card(self):
        return self.card

    def change_color(self, color):
        if color == "black":
            self.text_color = rgb("white")
            self.background_color = rgb("black")
        else:
            self.text_color = rgb("black")
            self.background_color = rgb(color)
        # print(self.text_color, self.background_color)
