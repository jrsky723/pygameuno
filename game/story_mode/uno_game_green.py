from game.uno_game import UnoGame


class UnoGameGreen(UnoGame):
    def __init__(self, players_info):
        super().__init__(players_info)

    def remove_all_draw_cards(self):
        new_deck = []
        for card in self.deck:
            if not (card.value.startswith("draw") or card.value == "reload"):
                new_deck.append(card)
        self.deck = new_deck

    def _create_deck(self):
        super()._create_deck()
        self.remove_all_draw_cards()

    # deal all cards to players except the top discard card
    def _deal_cards(self):
        while len(self.deck) > 1:
            for player in self.players:
                self.add_card_move_animation(
                    card=self.deck.pop(0),
                    src="deck",
                    dest=f"player_{player.get_id()}",
                    delay=0.1,
                    duration=0.5,
                )
                if len(self.deck) == 1:
                    break
