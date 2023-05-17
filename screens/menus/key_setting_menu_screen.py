import pygame
from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.json import save_json
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
        # just 5 keys in key_bindings using for loop

        for i, key in enumerate(self.key_bindings):
            text_params["x"] = 720 if i >= 5 else text_params["x"]
            self.texts += [
                TextBox(y=T_Y + T_GAP * (i % 5), text=key.upper(), **text_params)
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

        # make below code shorter
        for i, key in enumerate(self.key_bindings):
            y_position = B_Y + B_GAP * (i % 5)
            key_button_params["x"] = B_X2 if i >= 5 else B_X
            button = Button(
                y=y_position, text=self.key_bindings[key], **key_button_params
            )
            section_index = i % 5
            if i < 5:
                self.button_sections.append([button])
            else:
                self.button_sections[section_index] += [button]

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
        self.save_button = Button(x=S_B_X, text="SAVE", **save_params)
        self.back_button = Button(x=S_B_X + S_B_GAP, text="BACK", **save_params)
        self.save_back_buttons = [
            self.save_button,
            self.back_button,
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

    def save_options(self):
        # use for loop to make new_key_bindings
        new_key_bindings = {}
        for i, key in enumerate(self.key_bindings):
            if i < 5:
                new_key_bindings[key] = self.button_sections[i][0].text
            else:
                new_key_bindings[key] = self.button_sections[i % 5][1].text

        if self.check_duplicated_key(new_key_bindings):
            self.error_message.visible = True
            return
        else:
            self.error_message.visible = False
        self.options["key_bindings"] = new_key_bindings
        save_json("options", self.options)
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
