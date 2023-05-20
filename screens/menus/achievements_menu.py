from screens.menu_screen import MenuScreen
from renders.text_box import TextBox
from renders.button import Button
from utils.json import load_json
from utils.constants import IMAGE as I
import pygame


class AchievementMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.achievements = load_json("achievements")
        self.icon = pygame.image.load(I.CROWN)
        self.icon = pygame.transform.scale(
            self.icon, (self.screen_width / 12.8, self.screen_height / 7.2)
        )

        self.texts += [TextBox(text="ACHIEVEMENTS", **self.title_params)]
        single_player_achievements = self.achievements["single player mode"]
        self.texts += [
            TextBox(
                text="SINGLE PLAYER MODE",
                x="center",
                y=150,
                font_size=20,
                **self.rect_params,
            )
        ]
        T_X, T_Y, T_GAP1, T_GAP2 = 100, 250, 40, 30
        text_params = {"x": T_X, "font_size": 20, **self.rect_params}
        i = 0
        for key, value in single_player_achievements.items():
            if isinstance(value, dict):
                self.texts += [
                    TextBox(text=key.upper(), y=T_Y, **text_params, text_color="green")
                ]
                for k, v in value.items():
                    self.texts += [
                        TextBox(
                            text=f"{k}: {v}",
                            y=T_Y + T_GAP2,
                            **text_params | {"x": T_X + 50},
                        )
                    ]
                    T_Y += T_GAP2
                T_Y += T_GAP1

        self.back_button = Button(x=1000, y=600, text="BACK", **self.rect_params)
        self.button_sections.append([self.back_button])

    def draw(self):
        super().draw()
        self.screen.blit(self.icon, (100, 100))
