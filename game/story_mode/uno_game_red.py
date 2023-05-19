from game.uno_game import UnoGame
import random


class UnoGameRed(UnoGame):
    def __init__(self, players_info):
        self.action_cards = []
        self.number_cards = []

        super().__init__(players_info)

    def _start_game(self):
        self._start_turn(self.players[self.current_player_idx])
        self.seperate_cards()
        self._deal_cards()
        self._set_top_discard_card()

    def seperate_cards(self):
        self._shuffle_deck()
        for card in self.deck:
            if card.type == "action":
                self.action_cards.append(card)
            elif card.type == "number":
                self.number_cards.append(card)

    def _deal_cards(self, num_cards=7):
        for _ in range(num_cards):
            for player in self.com_players:
                weight = random.randint(0, 2)
                if weight == 0:
                    card = self.number_cards.pop(0)

                else:
                    card = self.action_cards.pop(0)
                self.add_card_move_animation(
                    card=card,
                    src="deck",
                    dest=f"player_{player.get_id()}",
                    delay=0.1,
                    duration=0.5,
                )

        self.deck = self.number_cards + self.action_cards

        for _ in range(num_cards):
            for player in self.human_players:
                self.add_card_move_animation(
                    card=self.deck.pop(0),
                    src="deck",
                    dest=f"player_{player.get_id()}",
                    delay=0.1,
                    duration=0.5,
                )
