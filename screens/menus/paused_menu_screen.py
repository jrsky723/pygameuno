import pygame
from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.constants import MUSIC as M


class PausedMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        pygame.mixer.music.pause()
        self.texts += [TextBox(text="PAUSED", **self.title_params)]

        B_Y, B_GAP = 250, 150
        buttons_params = self.rect_params | {"x": "center", "width": 300, "height": 100}
        self.resume_button = Button(y=B_Y, text="RESUME", **buttons_params)
        self.options_button = Button(y=B_Y + B_GAP, text="OPTIONS", **buttons_params)
        self.quit_button = Button(y=B_Y + B_GAP * 2, text="QUIT", **buttons_params)

        self.button_sections += [
            [self.resume_button],
            [self.options_button],
            [self.quit_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.resume_button:
                self.resume()
            elif button == self.options_button:
                self.open_options()
            elif button == self.quit_button:
                self.quit()

    def resume(self):
        pygame.mixer.music.unpause()
        self.running = False

    def open_options(self):
        from screens.menus.options_menu_screen import OptionsMenuScreen

        options_menu = OptionsMenuScreen(self.screen, self.clock, self.options)
        new_options = options_menu.run()
        self.__init__(self.screen, self.clock, new_options)

    def run(self):
        super().run()
        return self.options
