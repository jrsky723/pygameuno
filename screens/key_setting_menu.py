from screens.menu_screen import MenuScreen
from classes.button import Button
from classes.text_box import TextBox
from utils.constants import SCREEN as S


class KeySettingMenu(MenuScreen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.new_key_settings = self.options["key_settings"]
        # ############### TITLE ################
        # self.texts += [TextBox(text="KEY SETTINGS", **self.title_params)]

        # ############### TEXTS ################
        # T_X, T_Y, T_GAP = 110, 250, 90
        # text_params = self.rect_params | {"x": T_X, "font_size": 40}
        # self.texts += [
        #     TextBox(y=T_Y, text="UP", **text_params),
        #     TextBox(y=T_Y + T_GAP, text="DOWN", **text_params),
        #     TextBox(y=T_Y + T_GAP * 2, text="LEFT", **text_params),
        #     TextBox(y=T_Y + T_GAP * 3, text="RIGHT", **text_params),
        #     TextBox(y=T_Y + T_GAP * 4, text="ROTATE", **text_params),
        #     TextBox(y=T_Y + T_GAP * 5, text="HOLD", **text_params),
        #     TextBox(y=T_Y + T_GAP * 6, text="DROP", **text_params),
        #     TextBox(y=T_Y + T_GAP * 7, text="PAUSE", **text_params),
        # ]
