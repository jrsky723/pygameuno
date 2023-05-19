from game.uno_constants import CARD_ABBREVIATIONS


class UnoCard:
    def __init__(
        self,
        type,
        color,
        value,
    ):
        self.type = type
        self.color = color
        self.value = value
        self.initial_weight = 0

    def __str__(self):
        return f"{self.color} {self.value}"

    def get_abb(self):
        abb = ""
        if self.type == "number":
            abb = self.value
        else:
            abb = CARD_ABBREVIATIONS[self.value]
        return abb

    def get_color(self):
        return self.color
