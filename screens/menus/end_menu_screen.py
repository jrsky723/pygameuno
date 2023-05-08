import pygame
from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.constants import MUSIC as M


class EndMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options, winner):
        super().__init__(screen, clock, options)
        pygame.mixer.music.pause()
        self.winner = winner
        self.texts += [TextBox(text="GAME OVER", **self.title_params)]

        self.winner_text = TextBox(
            text=f"{self.winner.get_name()} wins!",
            **self.rect_params,
            x="center",
            y=200,
        )
        self.texts += [self.winner_text]

        B_Y, B_GAP = 350, 150
        buttons_params = self.rect_params | {"x": "center", "width": 300, "height": 100}
        self.home_button = Button(y=B_Y, text="HOME", **buttons_params)
        self.quit_button = Button(y=B_Y + B_GAP, text="QUIT", **buttons_params)

        self.button_sections += [
            [self.home_button],
            [self.quit_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.home_button:
                self.open_home()
            elif button == self.quit_button:
                self.quit()

    def open_home(self):
        from screens.menus.start_menu_screen import StartMenuScreen

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(M.MENU_BACKGROUND)
        pygame.mixer.music.play(-1)
        start_menu_screen = StartMenuScreen(self.screen, self.clock, self.options)
        start_menu_screen.run()
