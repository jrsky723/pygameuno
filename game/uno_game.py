import random
from game.card import Card
from game.player import Player


class UnoGame:
    def __init__(self, player_number=2):
        self.deck = self.create_deck()
        self.player_number = player_number
        self.players = []
        self.discard_pile = []
        self.current_player_index = 0
        self.direction = 1
        self.top_card = None
        self.init_game()

    def create_deck(self):
        cards = []
        colors = ["red", "green", "blue", "yellow"]
        for color in colors:
            # Add numbered cards
            for i in range(10):
                cards.append(Card(type="number", color=color, value=str(i)))
                if i != 0:
                    cards.append(Card(type="number", color=color, value=str(i)))
            # Add action cards
            for value in ["skip", "reverse", "draw2"]:
                cards.append(Card(type="action", color=color, value=value))
            # Add wild cards
            for value in ["draw4", "color_change", "reload"]:
                cards.append(Card(type="wild", color="black", value=value))
        return cards

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self, num_cards=7):
        for i in range(num_cards):
            for player in self.players:
                card = self.deck.pop(0)
                player.add_card(card)

    def add_player(self, player):
        self.players.append(player)

    def init_game(self):
        self.shuffle_deck()
        self.deal_cards()
        self.discard_pile.append(self.deck.pop(0))
        for player_idx in range(self.player_number):
            self.add_player(Player(player_idx))
        self.deal_cards()
        self.discard_pile.append(self.deck.pop(0))
        self.top_card = self.discard_pile[-1]


if __name__ == "__main__":
    game = UnoGame()
    for player in game.players:
        print(player.idx)
        for card in player.hand:
            print(card.color, card.type, card.value)
    print(
        "Discard pile:",
        game.discard_pile[0].color,
        game.discard_pile[0].type,
        game.discard_pile[0].value,
    )
