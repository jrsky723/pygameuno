class UnoPlayer:
    id_counter = 0

    def __init__(self, name):
        self.name = name
        self.id = UnoPlayer.id_counter
        UnoPlayer.id_counter += 1
        self.hand = []
        self.is_turn = False
        self.next_card_pos = (0, 0)

    def set_next_card_pos(self, pos):
        self.next_card_pos = pos

    def get_next_card_pos(self):
        return self.next_card_pos

    def get_id(self):
        return self.id

    def get_hand(self):
        return self.hand

    def add_card(self, card):
        self.hand.append(card)
        
    # Returns TRUE/FALSE by checking if there is a card that can be played
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
