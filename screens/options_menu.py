import pygame
from screens.menu_screen import MenuScreen
from classes.button import Button
from classes.text_box import TextBox
from utils.constants import SCREEN as S


class OptionsMenu(MenuScreen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        rect_settings = {
            "screen_size": self.screen_size,
            "color_blind": self.color_blind,
        }
        # TITLE
        self.texts.append(TextBox(text="OPTIONS", **self.title_params))
        # TEXTS
        T_X, T_Y, T_GAP = 110, 230, 120
        text_settings = rect_settings.copy()
        text_settings["font_size"] = 40
        self.texts = [
            TextBox(x=T_X, y=T_Y, text="SCREEN SIZE", **text_settings),
            TextBox(x=T_X, y=T_Y + T_GAP, text="VOLUME", **text_settings),
            TextBox(x=T_X, y=T_Y + T_GAP * 2, text="COLOR BLIND", **text_settings),
        ]
        # SCREEN SIZE BUTTONS
        screen_size_idx = {"small": 0, "medium": 1, "large": 2}
        self.screen_size_selected_idx = screen_size_idx[self.screen_size]
        button_settings = rect_settings.copy()
        button_settings.update({"font_size": 35, "width": 120, "height": 50})
        B_X, B_Y, B_GAP = 800, T_Y, 120
        self.screen_size_buttons = [
            Button(x=B_X, y=B_Y, text="small", **button_settings),
            Button(x=B_X + B_GAP, y=B_Y, text="medium", **button_settings),
            Button(x=B_X + B_GAP * 2, y=B_Y, text="large", **button_settings),
        ]
        self.button_sections.append(self.screen_size_buttons)
        # VOLUME BUTTONS
        self.volume_selected_idx = 0
        self.volume_buttons = [
            Button(x=B_X, y=B_Y + B_GAP, text="0", **button_settings),
            Button(x=B_X + B_GAP, y=B_Y + B_GAP, text="", **button_settings),
            Button(x=B_X + B_GAP * 2, y=B_Y + B_GAP, text="100", **button_settings),
        ]
        self.button_sections.append(self.volume_buttons)

        # self.save_and_back_button.draw(self.screen)
