from screens.menu_screen import MenuScreen
from renders.text_box import TextBox
from utils.json import load_json


class AchievementMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.achievements = load_json("achievements")
        self.texts += [TextBox(text="ACHIEVEMENTS", **self.title_params)]
        single_mode_achievements = self.achievements["single player mode"]
        self.texts += [
            TextBox(
                text="SINGLE PLAYER MODE",
                x="center",
                y=150,
                font_size=20,
                **self.rect_params,
            )
        ]
