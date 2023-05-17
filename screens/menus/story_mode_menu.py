from screens.menu_screen import MenuScreen
from screens.menus.join_menu import JoinMenuScreen
from renders.button import Button
from renders.text_box import TextBox


class StoryModeMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.texts += [TextBox(text="STORY MODE", **self.title_params)]
        B_Y, B_GAP = 250, 150
