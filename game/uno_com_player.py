from game.uno_player import UnoPlayer


class UnoComPlayer(UnoPlayer):
    def __init__(self, name):
        super().__init__(name)
        pass

    def is_human(self):
        return False

    def is_com(self):
        return True
