from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from renders.input_box import InputBox


# TODO: get user input to get host IP address and join(submit) button, back button
class JoinMenuScreen(MenuScreen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.texts += [TextBox(text="JOIN", **self.title_params)]
        B_Y, B_GAP = 250, 150
        buttons_params = self.rect_params | {
            "y": B_Y + B_GAP * 2,
            "width": 300,
            "height": 100,
        }

        self.input_box = InputBox(
            x="center",
            y="center",
            width=500,
            height=100,
            text="IP ADDRESS",
            **self.rect_params,
        )
        self.input_boxes.append(self.input_box)
        self.button_sections += [[self.input_box]]
        self.join_button = Button(x=300, text="JOIN", **buttons_params)
        self.back_button = Button(x=1280 - 600, text="BACK", **buttons_params)

        self.button_sections += [
            [self.join_button, self.back_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.join_button:
                self.join()
            elif button == self.back_button:
                self.back()

    def join(self):
        pass
