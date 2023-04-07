import random
from game.uno_card import UnoCard
from game.uno_player import UnoPlayer
from game.uno_constants import COLORS, NUMBERS, COLOR_ACTION_VALUES, WILD_ACTION_VALUES
from utils.timer import wait


class UnoGame:
    def __init__(self, player_number=2):
        self.deck = self._create_deck()
        self.player_number = player_number
        self.players = []
        self.discard_pile = []
        self.current_player_idx = 0
        self.direction = 1
        self.top_card = None
        self._init_game()

    def _init_game(self):
        self._shuffle_deck()
        self._add_players()
        self._deal_cards()
        self._set_top_card()

    # Initializing Game Functions

    def _create_deck(self):
        """
        Creates a deck of cards
        """
        cards = []
        # Add color cards
        for color in COLORS:
            # Add color number cards
            for i in NUMBERS:
                cards.append(UnoCard(type="number", color=color, value=str(i)))
            # Add color action cards
            for value in COLOR_ACTION_VALUES * 2:
                cards.append(UnoCard(type="action", color=color, value=value))
        # Add wild cards
        for value in WILD_ACTION_VALUES:
            cards.append(UnoCard(type="action", color="black", value=value))

        return cards

    def _shuffle_deck(self):
        random.shuffle(self.deck)

    def _deal_cards(self, num_cards=7):
        for i in range(num_cards):
            for player in self.players:
                if len(self.deck) == 0:
                    return
                card = self.deck.pop(0)
                player.add_card(card)

    def _add_players(self):
        for player_idx in range(self.player_number):
            self.players.append(UnoPlayer(player_idx))

    def _set_top_card(self):
        self.discard_pile.append(self.deck.pop(0))
        self.top_card = self.discard_pile[-1]

    def get_top_card(self):
        return self.top_card

    def get_com_players(self):
        return self.players[1:]

    def get_player(self):
        return self.players[0]

    # Game Functions
    def start_game(self):
        self.players[self.current_player_idx].set_is_turn(True)

    def next_turn(self):
        print("Next Turn")
        self.players[self.current_player_idx].set_is_turn(False)
        self.current_player_idx += self.direction + self.player_number
        self.current_player_idx %= self.player_number
        self.players[self.current_player_idx].set_is_turn(True)

    def get_current_player(self):
        return self.players[self.current_player_idx]
