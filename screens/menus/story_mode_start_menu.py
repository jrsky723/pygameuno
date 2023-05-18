from screens.menu_screen import MenuScreen
from screens.game_screen import GameScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.constants import STORY_MODE_DESCRIPTION as SMD, STORY_MODE_COMS as SMC


# TODO: get user input to get host IP address and join(submit) button, back button
class StoryModeStartMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options, game_info):
        super().__init__(screen, clock, options)
        self.game_info = game_info
        self.players = [
            {"name": "Player", "is_com": False},
        ]
        self.players += SMC[self.game_info["zone"]]
        self.game_info["players"] = self.players
        self.texts += [
            TextBox(text=f"{self.game_info['zone'].upper()}", **self.title_params)
        ]
        text_params = self.rect_params | {"font_size": 25}
        T_Y, T_GAP = 200, 50
        for i, text in enumerate(SMD[self.game_info["zone"]]):
            self.texts += [
                TextBox(text=text, x="center", y=T_Y + T_GAP * i, **text_params)
            ]
        self.texts += [
            TextBox(
                text="Do you want to start the match?",
                x="center",
                y=550,
                **text_params,
            )
        ]
        button_params = self.rect_params | {
            "y": 600,
            "width": 300,
            "height": 100,
        }
        self.back_button = Button(x=300, text="BACK", **button_params)
        self.start_button = Button(x=680, text="START", **button_params)
        self.button_sections += [
            [self.back_button, self.start_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.start_button:
                self.start()

    def start(self):
        game_screen = GameScreen(self.screen, self.clock, self.options, self.game_info)
        game_screen.run()
