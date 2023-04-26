from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox


# TODO: get user input to get host IP address and join(submit) button, back button
class HostMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.texts += [TextBox(text="Host", **self.title_params)]
        B_Y, B_GAP = 250, 150
