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

        # self.shuffle_deck()
        # self.deal_cards()
        # # Place the top card of the deck on the discard pile
        # self.discard_pile.append(self.deck.pop(0))
        # while True:
        #     # Get the current player
        #     current_player = self.players[self.current_player_index]
        #     print(f"Current player: {current_player.name}")
        #     # Check if the player can play a card
        #     if current_player.can_play(self.discard_pile[-1]):
        #         card = current_player.play_card(self.discard_pile[-1])
        #         print(f"{current_player.name} played {card}")
        #         self.discard_pile.append(card)
        #         # Check if the player has won
        #         if len(current_player.hand) == 0:
        #             print(f"{current_player.name} has won!")
        #             break
        #     else:
        #         # Draw a card
        #         card = self.deck.pop(0)
        #         print(f"{current_player.name} drew {card}")
        #         current_player.add_card(card)
        #         # Check if the player can now play a card
        #         if current_player.can_play(self.discard_pile[-1]):
        #             card = current_player.play_card(self.discard_pile[-1])
        #             print(f"{current_player.name} played {card}")
        #             self.discard_pile.append(card)
        #             # Check if the player has won
        #             if len(current_player.hand) == 0:
        #                 print(f"{current_player.name} has won!")
        #                 break
        #     # Move on to the next player
        #     self.current_player_index += self.direction
        #     if self.current_player_index < 0:
        #         self.current_player_index = len(self.players) - 1
        #     elif self.current_player_index >= len(self.players):
        #         self.current_player_index = 0
        #     print("------------------------------------------------------")


if __name__ == "__main__":
    game = UnoGame()
    for player in game.players:
        print(f"{player.name}: {player.hand}")
