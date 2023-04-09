import random
from game.uno_card import UnoCard
from game.uno_player import UnoPlayer
from game.uno_com_player import UnoComPlayer
from game.uno_constants import COLORS, NUMBERS, COLOR_ACTION_VALUES, WILD_ACTION_VALUES


# TODO: change com player hand to we can see the actual cards


class UnoGame:
    def __init__(self, human_number, com_number):
        self.deck = self._create_deck()
        self.player_number = human_number + com_number
        self.human_number = human_number
        self.com_number = com_number
        self.players = []
        self.discard_pile = []
        self.current_player_idx = 0
        self.direction = 1
        self.top_card = None
        self.game_ended = False
        self._init_game()

    def _init_game(self):
        self._add_players()
        self._shuffle_deck()
        self._deal_cards()
        self._set_top_card()

    # region Initializing Game Functions

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
        for i in range(self.human_number):
            self.players.append(UnoPlayer(name="Player " + str(i + 1)))
        for i in range(self.com_number):
            self.players.append(UnoComPlayer(name="Computer " + str(i + 1)))

    def _set_top_card(self):
        self.discard_pile.append(self.deck.pop(0))
        self.top_card = self.discard_pile[-1]

    # endregion

    # region get functions
    def get_top_card(self):
        return self.top_card

    def get_com_players(self):
        return self.players[self.human_number :]

    def get_player(self):
        return self.players[0]

    def get_current_player(self):
        return self.players[self.current_player_idx]

    def get_next_player(self):
        return self.players[
            (self.current_player_idx + self.direction) % self.player_number
        ]

    # endregion

    # region game play functions

    def _draw_card(self, player, draw_number=1):
        for i in range(draw_number):
            if len(self.deck) == 0:
                self.game_ended = True
                return
            card = self.deck.pop(0)
            player.add_card(card)

    def _play_card(self, card):
        self.discard_pile.append(card)
        self.top_card = card

    # endregion

    # region Game Functions

    def start_game(self):
        self.players[self.current_player_idx].set_is_turn(True)

    def next_turn(self):
        self.get_current_player().set_is_turn(False)
        self.get_next_player().set_is_turn(True)
        self.current_player_idx += self.direction + self.player_number
        self.current_player_idx %= self.player_number
        print("Current player: " + self.players[self.current_player_idx].name)

    def auto_turn(self):
        com_player = self.get_current_player()
        if not com_player.can_play(self.top_card):
            self._draw_card(com_player)
            return
        card = com_player.auto_play(self.top_card)
        self._play_card(card)

    def turn_time_out(self):
        player = self.get_current_player()
        self.auto_turn()
        # if player is human, draw card
        # if player.is_human():
        #     self._draw_card(player)
        # else:
        #     self.com_turn()

    # endregion

    # region Card Functions

    # TODO: add card action

    # if card.type is "action":
    #     self._handle_action(card)

    def _handle_action(self, card):
        if card.value == "reverse":
            self.direction *= -1
        elif card.value == "skip":
            self.next_turn()
        elif card.value == "draw2":
            self._draw_card(self.get_next_player(), 2)
        elif card.value == "draw4":
            self._draw_card(self.get_next_player(), 4)
        elif card.value == "reload":
            self._reload_hand(self.get_current_player())
        elif card.value == "change_color":
            self._change_color()
        elif card.value == "bonus":
            return
        self.next_turn()

    def _change_color(self):
        self.top_card.color = random.choice(COLORS)

    # reload player's hand
    # def _reload_hand(self, player):
    #     for i, card in enumerate(self.deck):

    # endregion
