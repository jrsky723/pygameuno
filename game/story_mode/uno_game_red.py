from game.uno_game import UnoGame
import random


class UnoGameRed(UnoGame):
    def __init__(self, players_info):
        super().__init__(players_info)

    def start_game(self):
        self.players[self.current_player_idx].set_is_turn(True)
        self.make_initial_weight()
        self._deal_cards()
        self._set_top_discard_card()

    def make_initial_weight(self):
        for card in self.deck:
            if card.type == "action":
                card.initial_weight = random.randint(0, 3)
            elif card.type == "number":
                card.initial_weight = random.randint(0, 2)
        self._shuffle_deck()
        self.deck.sort(key=lambda x: x.initial_weight, reverse=True)

    def _deal_cards(self, num_cards=7):
        for _ in range(num_cards):
            for player in self.com_players:
                self.add_card_move_animation(
                    card=self.deck.pop(0),
                    src="deck",
                    dest=f"player_{player.get_id()}",
                    delay=0.1,
                    duration=0.5,
                )

        self._shuffle_deck()

        for _ in range(num_cards):
            for player in self.human_players:
                self.add_card_move_animation(
                    card=self.deck.pop(0),
                    src="deck",
                    dest=f"player_{player.get_id()}",
                    delay=0.1,
                    duration=0.5,
                )
