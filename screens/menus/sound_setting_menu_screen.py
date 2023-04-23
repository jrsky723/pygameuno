import pygame
from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.options import save_options_json
from utils.constants import SCREEN as S


class SoundSettingMenuScreen(MenuScreen):
    def __init__(self, screen, options):
        super().__init__(screen, options)

        ############### TITLE ################
        self.texts += [TextBox(text="SOUND SETTINGS", **self.title_params)]

        ############### TEXTS ################
        T_X, T_Y, T_GAP = 110, 250, 90
        text_params = self.rect_params | {"x": T_X, "font_size": 40}
        self.texts += [
            TextBox(y=T_Y, text="GAME VOLUME", **text_params),
            TextBox(y=T_Y + T_GAP, text="MUSIC", **text_params),
            TextBox(y=T_Y + T_GAP * 2, text="SOUND EFFECTS", **text_params),
        ]

        ######### GAME VOLUME BUTTONS #########
        button_params = self.rect_params | {"width": 120, "height": 50, "font_size": 30}
        B_X, B_Y, B_GAP = 800, T_Y, 120

        game_volume_params = button_params | {"y": B_Y}
        self.game_volume_buttons = [
            Button(x=B_X, text="-", **game_volume_params),
            Button(x=B_X + B_GAP * 2, text="+", **game_volume_params),
        ]
        self.game_volume = TextBox(
            x=B_X + B_GAP, text=str(self.sound["volume"]), **game_volume_params
        )
        self.texts.append(self.game_volume)
        self.button_sections.append(self.game_volume_buttons)

        ########## MUSIC BUTTONS ##########
        music_params = button_params | {"y": B_Y + T_GAP}
        self.music_buttons = [
            Button(x=B_X, text="-", **music_params),
            Button(x=B_X + B_GAP * 2, text="+", **music_params),
        ]
        self.music = TextBox(
            x=B_X + B_GAP, text=str(self.sound["music"]), **music_params
        )
        self.texts.append(self.music)
        self.button_sections.append(self.music_buttons)

        ########## SOUND EFFECTS BUTTONS ##########
        sound_effects_params = button_params | {"y": B_Y + T_GAP * 2}
        self.sound_effects_buttons = [
            Button(x=B_X, text="-", **sound_effects_params),
            Button(x=B_X + B_GAP * 2, text="+", **sound_effects_params),
        ]
        self.sound_effects = TextBox(
            x=B_X + B_GAP, text=str(self.sound["effects"]), **sound_effects_params
        )
        self.texts.append(self.sound_effects)
        self.button_sections.append(self.sound_effects_buttons)

        ########    SAVE AND BACK BUTTONS   ########
        S_B_GAP, S_B_WIDTH, S_B_HEIGHT = 400, 200, 50
        S_B_X, S_B_Y = (
            (S.WIDTH_BASE - S_B_WIDTH - S_B_GAP) / 2,
            S.HEIGHT_BASE - S_B_HEIGHT - 50,
        )
        save_params = self.rect_params | {
            "y": S_B_Y,
            "width": 200,
            "height": 50,
            "font_size": 40,
        }
        self.save_back_buttons = [
            Button(x=S_B_X, text="SAVE", **save_params),
            Button(x=S_B_X + S_B_GAP, text="BACK", **save_params),
        ]
        self.button_sections.append(self.save_back_buttons)

    def button_click_down(self, button):
        super().button_click_down(button)
        if button is None or button.text in ["SAVE", "BACK"]:
            return
        if button in self.game_volume_buttons:
            if button.text == "+":
                self.sound["volume"] = min(self.sound["volume"] + 1, 10)
            else:
                self.sound["volume"] = max(self.sound["volume"] - 1, 0)
            self.game_volume.text = str(self.sound["volume"])
        elif button in self.music_buttons:
            if button.text == "+":
                self.sound["music"] = min(self.sound["music"] + 1, 10)
            else:
                self.sound["music"] = max(self.sound["music"] - 1, 0)
            self.music.text = str(self.sound["music"])
        elif button in self.sound_effects_buttons:
            if button.text == "+":
                self.sound["effects"] = min(self.sound["effects"] + 1, 10)
            else:
                self.sound["effects"] = max(self.sound["effects"] - 1, 0)
            self.sound_effects.text = str(self.sound["effects"])

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button.text == "SAVE":
                self.save_options()

    def save_options(self):
        new_sound_settings = {
            "volume": int(self.game_volume.text),
            "music": int(self.music.text),
            "effects": int(self.sound_effects.text),
        }
        self.options["sound"] = new_sound_settings
        save_options_json(self.options)
        self.__init__(self.screen, self.options)

    def run(self):
        super().run()
        return self.options
