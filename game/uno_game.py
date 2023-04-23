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
        self.game_over = False
        self.winner = None
        self.animation_infos = []
        self.game_event_infos = []
        self.selected_color = None
        self._init_game()

    def _init_game(self):
        self._add_players()

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

    # Deal 7 cards to each player in turns.
    def _deal_cards(self, num_cards=7):
        for i in range(num_cards):
            for player in self.players:
                self.add_card_move_animation(
                    self.deck.pop(0),
                    src="deck",
                    dest=f"player_{player.get_id()}",
                    delay=0.1,
                    duration=0.5,
                )

    # Add players to the game
    def _add_players(self):
        for i in range(self.human_number):
            self.players.append(UnoPlayer(name="Player " + str(i + 1)))
        for i in range(self.com_number):
            self.players.append(UnoComPlayer(name="Computer " + str(i + 1)))

    def _set_top_discard_card(self):
        self.add_card_move_animation(self.deck.pop(0), src="deck", dest="discard")

    # endregion

    # region get card
    def top_discard_card(self):
        return self.discard_pile[-1] if len(self.discard_pile) > 0 else None

    def top_deck_card(self):
        return self.deck[-1] if len(self.deck) > 0 else None

    # endregion
    # region get functions
    def get_animation_infos(self):
        return self.animation_infos

    def get_game_event_infos(self):
        return self.game_event_infos

    def get_direction(self):
        return self.direction

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

    def get_prev_player(self):
        return self.players[
            (self.current_player_idx - self.direction) % self.player_number
        ]

    def get_deck(self):
        return self.deck

    def is_game_over(self):
        return self.game_over

    # endregion

    # region set functions

    def set_animation_infos(self, animation_infos):
        self.animation_infos = animation_infos

    def set_game_event_infos(self, game_event_infos):
        self.game_event_infos = game_event_infos

    def set_selected_color(self, color):
        self.selected_color = color

    # endregion
    # region game play functions

    def _draw_card(self, player, draw_number=1):
        for i in range(draw_number):
            if len(self.deck) == 0:
                self.game_over = True
                return
            card = self.deck.pop(0)
            self.add_card_move_animation(
                card, src="deck", dest=f"player_{player.get_id()}"
            )

    def _play_card(self, player, card):
        self.add_card_move_animation(
            card, src=f"player_{player.get_id()}", dest="discard"
        )
        if card.type == "action":
            self._handle_action(player, card)
        # if len(player.get_hand()) == 0:
        #     self.game_over = True
        #     self.winner = player

    # endregion

    # region Game Functions

    def start_game(self):
        self.players[self.current_player_idx].set_is_turn(True)
        self._shuffle_deck()
        self._deal_cards()
        self._set_top_discard_card()

    def next_turn(self):
        self.get_current_player().set_is_turn(False)
        self.get_next_player().set_is_turn(True)
        self.current_player_idx += self.direction + self.player_number
        self.current_player_idx %= self.player_number

    def prev_turn(self):
        self.get_current_player().set_is_turn(False)
        self.get_prev_player().set_is_turn(True)
        self.current_player_idx -= self.direction + self.player_number
        self.current_player_idx %= self.player_number

    # automatically play card, if player can't play, draw card
    def auto_turn(self, com_player):
        if not com_player.can_play(self.top_discard_card()):
            self._draw_card(com_player)
            return
        card = com_player.auto_play(self.top_discard_card())
        self._play_card(com_player, card)

    def turn_time_out(self):
        player = self.get_current_player()
        self.auto_turn(player)
        # if player is human, draw card
        # if player.is_human():
        #     self._draw_card(player)
        # else:
        #     self.auto_ture()

    # endregion

    # region Card Functions

    def _handle_action(self, player, card):
        if card.value == "reverse":
            self.direction *= -1
        elif card.value == "skip":
            self.next_turn()
        elif card.value == "draw2":
            self._draw_card(self.get_next_player(), 2)
            self.next_turn()
        elif card.value == "draw4":
            self._draw_card(self.get_next_player(), 4)
            self.next_turn()
        elif card.value == "reload":
            self._reload_hand(player)
        elif card.value == "color_change":
            self._change_color(player)
        elif card.value == "bonus":  # one more current player's turn
            self.prev_turn()

    # change color of top card to color which is most in player's hand
    def _change_color(self, player):
        color_count = {}
        for color in COLORS:
            color_count[color] = 0
        for card in player.hand:
            if card.color != "black":
                color_count[card.color] += 1
        self.add_game_event_info("color_change", max(color_count, key=color_count.get))

    # reload player's hand put all card on deck and shuffle then draw the same number of card
    def _reload_hand(self, player):
        hand_size = len(player.hand)
        for card in player.hand:
            self.add_card_move_animation(
                card, src=f"player_{player.get_id()}", dest="deck"
            )
        player.hand = []
        self._shuffle_deck()
        self._draw_card(player, hand_size)

    # endregion

    # # region Animation Functions
    def add_card_move_animation(self, card, src, dest, delay=0.1, duration=0.3):
        self.animation_infos.append(
            {
                "type": "card_move",
                "card": card,
                "src": src,
                "dest": dest,
                "delay": delay,
                "duration": duration,
            }
        )

    def add_game_event_info(self, type, value):
        self.game_event_infos.append(
            {
                "type": type,
                "value": value,
            }
        )

    def update_by_animtaion_info(self, info):
        if info["type"] == "card_move":
            card, dest = info["card"], info["dest"]
            if dest == "deck":
                self.deck.append(card)
            elif dest == "discard":
                self.discard_pile.append(card)
            else:  # dest == "player_#"
                player_id = int(dest.split("_")[1])
                self.players[player_id].add_card(card)

    # # endregion
