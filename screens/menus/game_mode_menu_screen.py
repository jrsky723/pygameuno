from screens.menu_screen import MenuScreen
from screens.game_screen import GameScreen
from screens.menus.multiplay_menu_screen import MultiplayerMenuScreen
from renders.button import Button
from renders.text_box import TextBox


class GameModeMenuScreen(MenuScreen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.texts += [TextBox(text="GAME MODE", **self.title_params)]
        B_Y, B_GAP = 250, 150
        buttons_params = self.rect_params | {"x": "center", "width": 500, "height": 100}
        self.single_player_button = Button(
            y=B_Y, text="SINGLE-PLAYER", **buttons_params
        )
        self.multi_player_button = Button(
            y=B_Y + B_GAP, text="MULTI-PLAYER", **buttons_params
        )
        self.back_button = Button(y=B_Y + B_GAP * 2, text="BACK", **buttons_params)
        self.button_sections += [
            [self.single_player_button],
            [self.multi_player_button],
            [self.back_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.single_player_button:
                self.open_single_player()
            elif button == self.multi_player_button:
                self.open_multiplayer()
            elif button == self.back_button:
                self.back()

    def open_single_player(self):
        game_screen = GameScreen(self.screen, self.options)
        game_screen.run()
        pass

    def open_multiplayer(self):
        multiplayer_menu_screen = MultiplayerMenuScreen(self.screen, self.options)
        multiplayer_menu_screen.run()
        pass
