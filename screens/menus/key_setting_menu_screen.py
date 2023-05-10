import pygame
from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.options import save_options_json
from utils.constants import SCREEN as S


class KeySettingMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.selected_button = None
        ############### TITLE ################
        self.texts += [TextBox(text="KEY SETTINGS", **self.title_params)]

        ############# Subtitle ###############
        self.texts += [
            TextBox(
                x="center",
                y=S.TITLE_Y + 85,
                text="Use Mouse to select a button",
                **self.rect_params,
                font_size=25,
            )
        ]
        ############### TEXTS ################
        T_X, T_Y, T_GAP = 110, 220, 70
        text_params = self.rect_params | {"x": T_X, "font_size": 30}
        self.texts += [
            TextBox(y=T_Y, text="UP", **text_params),
            TextBox(y=T_Y + T_GAP, text="DOWN", **text_params),
            TextBox(y=T_Y + T_GAP * 2, text="LEFT", **text_params),
            TextBox(y=T_Y + T_GAP * 3, text="RIGHT", **text_params),
            TextBox(y=T_Y + T_GAP * 4, text="RETURN", **text_params),
        ]
        text_params["x"] = 720
        self.texts += [
            TextBox(y=T_Y, text="DRAW", **text_params),
        ]

        ############ Error #################
        error_params = self.rect_params | {
            "x": "center",
            "font_size": 30,
            "text_color": "red",
        }
        self.error_message = TextBox(
            y=T_Y + T_GAP * 5, text="KEY ALREADY IN USE", **error_params
        )
        self.error_message.visible = False
        self.texts.append(self.error_message)

        ########## KEY SETTINGS BUTTONS ##########
        B_X, B_Y, B_GAP = 350, 210, T_GAP
        key_button_params = self.rect_params | {
            "x": B_X,
            "width": 250,
            "height": 40,
            "font_size": 25,
        }
        B_X2 = 900

        self.button_sections += [
            [
                Button(y=B_Y, text=self.key_bindings["up"], **key_button_params),
                Button(
                    y=B_Y,
                    text=self.key_bindings["draw"],
                    **key_button_params | {"x": B_X2},
                ),
            ],
            [
                Button(
                    y=B_Y + B_GAP, text=self.key_bindings["down"], **key_button_params
                )
            ],
            [
                Button(
                    y=B_Y + B_GAP * 2,
                    text=self.key_bindings["left"],
                    **key_button_params,
                )
            ],
            [
                Button(
                    y=B_Y + B_GAP * 3,
                    text=self.key_bindings["right"],
                    **key_button_params,
                )
            ],
            [
                Button(
                    y=B_Y + B_GAP * 4,
                    text=self.key_bindings["return"],
                    **key_button_params,
                )
            ],
        ]

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

    def handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.selected_button is not None:
                self.handle_change_key(event)
            else:
                self.handle_movement(event)
        elif event.type == pygame.KEYUP:
            self.handle_return_up(event)

    def handle_change_key(self, event):
        self.selected_button.text = pygame.key.name(event.key)

    def button_click_down(self, button):
        super().button_click_down(button)
        if button is None or button.text in ["SAVE", "BACK"]:
            return
        if self.selected_button is not None:
            if button is self.selected_button:
                self.selected_button.unselect()
                self.selected_button = None
                self.no_movement = False
            else:
                self.selected_button.unselect()
                self.selected_button = button
                self.selected_button.select()
        else:
            self.selected_button = button
            self.selected_button.select()
            self.selected_button.unhover()
            self.no_movement = True

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button.text == "SAVE":
                self.save_options()

    def save_options(self):
        new_key_bindings = {
            "up": self.button_sections[0][0].text,
            "down": self.button_sections[1][0].text,
            "left": self.button_sections[2][0].text,
            "right": self.button_sections[3][0].text,
            "return": self.button_sections[4][0].text,
        }
        if self.check_duplicated_key(new_key_bindings):
            self.error_message.visible = True
            return
        else:
            self.error_message.visible = False
        self.options["key_bindings"] = new_key_bindings
        save_options_json(self.options)
        self.__init__(self.screen, self.clock, self.options)

    # returns True if there are no duplicated keyname
    def check_duplicated_key(self, new_key_bindings):
        key_names = []
        for key in new_key_bindings:
            key_names.append(new_key_bindings[key])
        return len(set(key_names)) != len(key_names)

    def run(self):
        super().run()
        return self.options
