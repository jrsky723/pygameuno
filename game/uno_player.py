class UnoPlayer:
    id_counter = 0

    def init():
        UnoPlayer.id_counter = 0

    def __init__(self, name):
        self.name = name
        self.id = UnoPlayer.id_counter
        UnoPlayer.id_counter += 1
        self.hand = []
        self.is_turn = False
        self.next_card_pos = (0, 0)
        self.is_uno = False
        self.uno_checked = False
        self.uno_failed = False

    def reset_uno_states(self):
        self.is_uno = False
        self.uno_checked = False
        self.uno_failed = False

    def set_uno_failed(self, uno_failed):
        self.uno_failed = uno_failed

    def get_uno_failed(self):
        return self.uno_failed

    def get_is_uno(self):
        return self.is_uno

    def set_is_uno(self, is_uno):
        self.is_uno = is_uno

    def set_uno_checked(self, uno_checked):
        self.uno_checked = uno_checked

    def get_uno_checked(self):
        return self.uno_checked

    def set_next_card_pos(self, pos):
        self.next_card_pos = pos

    def get_next_card_pos(self):
        return self.next_card_pos

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand

    def get_hand_size(self):
        return len(self.hand)

    def add_card(self, card):
        self.hand.append(card)

    # Returns TRUE/FALSE by checking if there is a card that can be played
    def can_play(self, color, value):
        for c in self.hand:
            if self.can_play_card(color, value, c):
                return True
        return False

    def can_play_card(self, color, value, card):
        return (
            color == "black"
            or card.color == color
            or card.value == value
            or card.color == "black"
        )

    def play_card(self, card):
        self.hand.remove(card)

    def get_is_turn(self):
        return self.is_turn

    def set_is_turn(self, is_turn):
        self.is_turn = is_turn

    def auto_card(self, color, value):
        # find first card that can be played
        for card in self.hand:
            if self.can_play_card(color, value, card):
                return card

    def is_human(self):
        return True

    def is_com(self):
        return False
