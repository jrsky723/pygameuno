class UnoPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.is_turn = False

    def add_card(self, card):
        self.hand.append(card)

    def can_play(self, top_card):
        for c in self.hand:
            if (
                c.type == "wild"
                or c.color == top_card.color
                or c.value == top_card.value
            ):
                return True
        return False

    def play_card(self, card):
        self.hand.remove(card)

    def get_is_turn(self):
        return self.is_turn

    def set_is_turn(self, is_turn):
        self.is_turn = is_turn

    def auto_play(self, top_card):
        for card in self.hand:
            if (
                card.type == "wild"
                or card.color == top_card.color
                or card.value == top_card.value
            ):
                self.play_card(card)
                return card
        return None

    def is_human(self):
        return True
