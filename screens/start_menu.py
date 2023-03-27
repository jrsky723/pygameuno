from utils.constants import SCREEN as S
from screens.menu_screen import MenuScreen
from screens.game_screen import GameScreen
from screens.options_menu import OptionsMenu
from classes.button import Button
from classes.text_box import TextBox


class StartMenu(MenuScreen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.texts += [TextBox(text="Pygame UNO", **self.title_params)]
        B_Y, B_GAP = 250, 150
        buttons_params = self.rect_params | {"x": "center", "width": 300, "height": 100}
        self.button_sections += [
            [Button(y=B_Y, text="START", **buttons_params)],
            [Button(y=B_Y + B_GAP, text="OPTIONS", **buttons_params)],
            [Button(y=B_Y + B_GAP * 2, text="QUIT", **buttons_params)],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button.text == "START":
                self.start_game()
            elif button.text == "OPTIONS":
                self.open_options()
            elif button.text == "QUIT":
                self.quit()

    def start_game(self):
        game_screen = GameScreen(self.screen, self.options)
        game_screen.run()

    def open_options(self):
        options_menu = OptionsMenu(self.screen, self.options)
        new_options = options_menu.run()
        self.__init__(self.screen, new_options)
