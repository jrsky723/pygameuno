from screens.menu_screen import MenuScreen
from screens.menus.join_menu import JoinMenuScreen
from renders.button import Button
from renders.text_box import TextBox


class StoryModeMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.texts += [TextBox(text="STORY MODE", **self.title_params)]
        B_Y, B_GAP = 250, 150
        buttons_params = self.rect_params | {"x": "center", "width": 300, "height": 100}
        self.multiplay_button = Button(
            y=B_Y + B_GAP, text="MULTI PLAY", **buttons_params
        )
        self.multiplay_button = Button(
            y=B_Y + B_GAP, text="MULTI PLAY", **buttons_params
        )
        self.back_button = Button(y=B_Y + B_GAP * 2, text="BACK", **buttons_params)

        self.button_sections += [
            [self.singleplay_button],
            [self.multiplay_button],
            [self.back_button],
        ]
