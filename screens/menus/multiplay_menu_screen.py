from screens.menu_screen import MenuScreen
from screens.menus.join_menu_screen import JoinMenuScreen
from screens.menus.host_menu_screen import HostMenuScreen
from renders.button import Button
from renders.text_box import TextBox


class MultiplayerMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.texts += [TextBox(text="MULTIPLAYER", **self.title_params)]
        B_Y, B_GAP = 250, 150
        buttons_params = self.rect_params | {"x": "center", "width": 300, "height": 100}
        self.host_button = Button(y=B_Y, text="HOST", **buttons_params)
        self.join_button = Button(y=B_Y + B_GAP, text="JOIN", **buttons_params)
        self.back_button = Button(y=B_Y + B_GAP * 2, text="BACK", **buttons_params)

        self.button_sections += [
            [self.host_button],
            [self.join_button],
            [self.back_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.host_button:
                self.host()
            elif button == self.join_button:
                self.join()
            elif button == self.back_button:
                self.back()

    def host(self):
        host_menu_screen = HostMenuScreen(self.screen, self.clock, self.options)
        host_menu_screen.run()
        pass

    def join(self):
        join_menu_screen = JoinMenuScreen(self.screen, self.clock, self.options)
        join_menu_screen.run()
