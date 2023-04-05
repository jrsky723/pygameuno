class Card:
    def __init__(
        self,
        type,
        color,
        value,
    ):
        self.type = type
        self.color = color
        self.value = value

    def get_abb(self):
        abb = ""
        if self.type == "number":
            abb = self.value
        else:
            abb = self.value[0:2].upper()
        return abb
