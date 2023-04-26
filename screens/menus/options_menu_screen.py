import pygame
from screens.menu_screen import MenuScreen
from screens.menus.key_setting_menu_screen import KeySettingMenuScreen
from screens.menus.sound_setting_menu_screen import SoundSettingMenuScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.options import save_options_json
from utils.constants import SCREEN as S
import os


class OptionsMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        ############### TITLE ################
        self.texts += [TextBox(text="OPTIONS", **self.title_params)]

        ############### TEXTS ################
        T_X, T_Y, T_GAP = 110, 250, 90
        text_params = self.rect_params | {"x": T_X, "font_size": 40}
        self.texts += [
            TextBox(y=T_Y, text="SCREEN SIZE", **text_params),
            TextBox(y=T_Y + T_GAP, text="SOUND SETTINGS", **text_params),
            TextBox(y=T_Y + T_GAP * 2, text="KEY SETTINGS", **text_params),
            TextBox(y=T_Y + T_GAP * 3, text="COLOR BLIND", **text_params),
        ]

        ######### SCREEN SIZE BUTTONS #########
        button_params = self.rect_params | {"width": 120, "height": 50, "font_size": 30}
        B_X, B_Y, B_GAP = 800, T_Y, 120

        screen_size_params = button_params | {"y": B_Y, "font_size": 20}
        self.screen_size_buttons = [
            Button(x=B_X, text="small", **screen_size_params),
            Button(x=B_X + B_GAP, text="medium", **screen_size_params),
            Button(x=B_X + B_GAP * 2, text="large", **screen_size_params),
        ]
        screen_size_idx = {"small": 0, "medium": 1, "large": 2}
        self.screen_size_selected_button = self.screen_size_buttons[
            screen_size_idx[self.screen_size]
        ]
        self.screen_size_selected_button.select()
        self.button_sections.append(self.screen_size_buttons)

        ##########    SOUND BUTTONS   ##########
        sound_settings_params = button_params | {"y": B_Y + T_GAP, "width": 360}
        self.sound_settings_buttons = [
            Button(x=B_X, text="SETTINGS", **sound_settings_params)
        ]
        self.button_sections.append(self.sound_settings_buttons)
        ########## KEY SETTINGS BUTTON5S ##########
        key_settings_params = button_params | {"y": B_Y + T_GAP * 2, "width": 360}
        self.key_settings_buttons = [
            Button(x=B_X, text="SETTINGS", **key_settings_params)
        ]
        self.button_sections.append(self.key_settings_buttons)

        ##########  COLOR BLIND BUTTONS ##########
        color_blind_params = button_params | {"y": B_Y + T_GAP * 3}
        self.color_blind_buttons = [
            Button(x=B_X, text="OFF", **color_blind_params),
            Button(x=B_X + B_GAP * 2, text="ON", **color_blind_params),
        ]
        self.color_blind_selected_button = self.color_blind_buttons[self.color_blind]
        self.color_blind_selected_button.select()
        self.button_sections.append(self.color_blind_buttons)

        ########    SAVE AND BACK BUTTONS   ########
        save_params = button_params | {"y": B_Y + T_GAP * 4, "width": 170}
        self.save_back_buttons = [
            Button(x=B_X, text="SAVE", **save_params),
            Button(
                x=B_X + B_GAP * 3 - save_params["width"], text="BACK", **save_params
            ),
        ]
        self.button_sections.append(self.save_back_buttons)

    # Handle events
    def button_click_down(self, button):
        super().button_click_down(button)
        if button is None:
            return
        if button in self.screen_size_buttons:
            self.screen_size_selected_button.unselect()
            button.select()
            self.screen_size_selected_button = button
        elif button in self.color_blind_buttons:
            self.color_blind_selected_button.unselect()
            button.select()
            self.color_blind_selected_button = button

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button.text == "SAVE":
                self.save_options()
            elif button in self.key_settings_buttons:
                self.open_key_settings()
            elif button in self.sound_settings_buttons:
                self.open_sound_settings()

    def change_screen_size(self, new_screen_size):
        os.environ["SDL_VIDEO_CENTERED"] = "1"  # center window
        pygame.display.set_mode((S.WIDTH[new_screen_size], S.HEIGHT[new_screen_size]))

    def save_options(self):
        new_options = {
            "screen_size": self.screen_size_selected_button.text,
            "sound": self.sound,
            "key_bindings": self.options["key_bindings"],
            "color_blind": self.color_blind_selected_button.text == "ON",
        }
        self.options = new_options
        save_options_json(new_options)
        if new_options["screen_size"] != self.screen_size:
            self.change_screen_size(new_options["screen_size"])
        self.__init__(self.screen, self.clock, new_options)

    def open_key_settings(self):
        key_setting_menu = KeySettingMenuScreen(self.screen, self.clock, self.options)
        options = key_setting_menu.run()
        self.__init__(self.screen, self.clock, options)

    def open_sound_settings(self):
        sound_setting_menu = SoundSettingMenuScreen(
            self.screen, self.clock, self.options
        )
        options = sound_setting_menu.run()
        self.__init__(self.screen, self.clock, options)

    # Update and run
    def update(self):
        super().update()
        # self.texts[5].text = str(self.volume)

    def run(self):
        super().run()
        return self.options
