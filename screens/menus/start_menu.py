from screens.menu_screen import MenuScreen
from screens.menus.game_mode_menu import GameModeMenuScreen
from screens.menus.options_menu import OptionsMenuScreen
from screens.menus.achievements_menu import AchievementMenuScreen
from renders.button import Button
from renders.text_box import TextBox


class StartMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.texts += [TextBox(text="Pygame UNO", **self.title_params)]
        B_Y, B_GAP = 200, 120
        buttons_params = self.rect_params | {"x": "center", "width": 300, "height": 100}
        self.start_button = Button(y=B_Y, text="START", **buttons_params)
        self.options_button = Button(y=B_Y + B_GAP, text="OPTIONS", **buttons_params)
        self.achievements_button = Button(
            y=B_Y + B_GAP * 2, text="ACHIEVE", **buttons_params
        )
        self.quit_button = Button(y=B_Y + B_GAP * 3, text="QUIT", **buttons_params)

        self.button_sections += [
            [self.start_button],
            [self.options_button],
            [self.achievements_button],
            [self.quit_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.start_button:
                self.open_game_mode_menu()
            elif button == self.options_button:
                self.open_options()
            elif button == self.achievements_button:
                self.open_achievements()
            elif button == self.quit_button:
                self.quit()

    def open_game_mode_menu(self):
        game_mode_menu_screen = GameModeMenuScreen(
            self.screen, self.clock, self.options
        )
        game_mode_menu_screen.run()

    def open_options(self):
        options_menu = OptionsMenuScreen(self.screen, self.clock, self.options)
        new_options = options_menu.run()
        self.__init__(self.screen, self.clock, new_options)

    def open_achievements(self):
        achievements_menu = AchievementMenuScreen(self.screen, self.clock, self.options)
        achievements_menu.run()

    def escape(self):
        pass
