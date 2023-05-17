from screens.menu_screen import MenuScreen
from screens.game_screen import GameScreen
from renders.text_box import TextBox
from renders.button import Button
from renders.input_box import InputBox


class SingleplayMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.texts += [TextBox(text="SINGLE-PLAYER", **self.title_params)]

    def open_game(self):
        game_screen = GameScreen(self.screen, self.clock, self.options)
        game_screen.run()
        pass
