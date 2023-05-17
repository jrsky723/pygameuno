from screens.menu_screen import MenuScreen
from screens.menus.story_mode_menu import StoryModeMenuScreen
from screens.menus.singleplay_lobby_menu import SingleplayLobbyMenuScreen

from renders.text_box import TextBox
from renders.button import Button
from renders.input_box import InputBox


class SingleplayMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.texts += [TextBox(text="SINGLE-PLAYER", **self.title_params)]

        B_Y, B_GAP = 250, 150
        buttons_params = self.rect_params | {"x": "center", "width": 500, "height": 100}
        self.story_mode_button = Button(y=B_Y, text="STORY MODE", **buttons_params)
        self.single_play_button = Button(
            y=B_Y + B_GAP, text="SINGLE PLAY", **buttons_params
        )
        self.back_button = Button(y=B_Y + B_GAP * 2, text="BACK", **buttons_params)

        self.button_sections += [
            [self.story_mode_button],
            [self.single_play_button],
            [self.back_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.story_mode_button:
                self.open_story_mode()
            elif button == self.single_play_button:
                self.open_single_play()

    def open_story_mode(self):
        story_mode_menu_screen = StoryModeMenuScreen(
            self.screen, self.clock, self.options
        )
        story_mode_menu_screen.run()

    def open_single_play(self):
        single_play_lobby_menu_screen = SingleplayLobbyMenuScreen(
            self.screen, self.clock, self.options
        )
        single_play_lobby_menu_screen.run()
