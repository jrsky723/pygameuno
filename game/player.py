class Player:
    def __init__(self, player_idx):
        self.idx = player_idx
        self.hand = []
        self.name = f"Player {player_idx}"

    def add_card(self, card):
        self.hand.append(card)

    def can_play(self, card):
        for c in self.hand:
            if c.type == "wild" or c.color == card.color or c.value == card.value:
                return True
        return False

    def play_card(self, card):
        self.hand.remove(card)
