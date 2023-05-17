from screens.menu_screen import MenuScreen
from screens.game_screen import GameScreen
from renders.button import Button
from renders.input_box import InputBox
from renders.text_box import TextBox
from utils.constants import SCREEN as SC


class SingleplayLobbyMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)

        self.my_player = {
            "id": 0,
            "name": "Player",
            "is_com": False,
        }
        computer1 = {
            "id": 1,
            "name": "Computer 1",
            "is_com": True,
        }
        self.players = [
            self.my_player,
            computer1,
        ]
        self.texts += [TextBox(text="SINGLE MODE", **self.title_params)]
        T_X, T_Y, T_GAP = 130, 250, 90
        text_params = self.rect_params | {"x": T_X, "font_size": 40}
        self.texts += [
            TextBox(text="Player Name:", y=T_Y, **text_params),
            TextBox(text="Computers  :", y=T_Y + T_GAP, **text_params),
        ]

        B_X, B_Y = 550, 240
        button_params = self.rect_params | {
            "width": 200,
            "height": 50,
            "font_size": 30,
        }
        self.name_input_box = InputBox(
            x=B_X, y=B_Y, text=self.my_player["name"], **button_params | {"width": 450}
        )
        self.input_boxes.append(self.name_input_box)
        self.button_sections += [[self.name_input_box]]

        com_buttton_params = self.rect_params | {
            "y": B_Y + T_GAP,
            "width": 100,
            "height": 50,
            "font_size": 40,
        }
        # computer player addition buttons
        self.sub_button = Button(x=B_X + 50, text="-", **com_buttton_params)
        self.add_button = Button(x=B_X + 300, text="+", **com_buttton_params)
        self.button_sections += [[self.add_button, self.sub_button]]
        self.computer_numbers_box = TextBox(
            x=B_X + 175,
            text=str(self.get_com_number()),
            **com_buttton_params | {"width": 100},
        )
        self.texts += [self.computer_numbers_box]

        B_X, B_Y = 300, 500
        self.start_button = Button(x=B_X, y=B_Y, text="START", **button_params)
        self.back_button = Button(x=B_X + 350, y=B_Y, text="BACK", **button_params)
        self.button_sections += [[self.start_button, self.back_button]]

        self.slot_const = {
            "x": SC.WIDTH_BASE * (5 / 6),
            "width": SC.WIDTH_BASE / 6,
            "height": SC.HEIGHT_BASE / 5,
        }
        self.slot_params = self.rect_params | {
            "x": self.slot_const["x"],
            "text": "empty",
            "font_size": 30,
            "width": self.slot_const["width"],
            "height": self.slot_const["height"],
            "border_width": 3,
        }
        self.empty_slot_boxes = []
        for i in range(5):
            self.empty_slot_boxes.append(
                TextBox(y=self.slot_const["height"] * i, **self.slot_params)
            )
        self.texts += self.empty_slot_boxes

        self.no_computer_buttons_sections = self.button_sections.copy()
        # computer player buttons
        self.com_player_buttons_sections = []
        self.com_player_buttons = []
        self.create_com_player_buttons()

    def update(self):
        super().update()
        self.computer_numbers_box.set_text(str(self.get_com_number()))

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.add_button:
                self.add_com_player()
            elif button == self.sub_button:
                self.sub_com_player()
            elif button == self.start_button:
                self.start_game()
            elif button in self.com_player_buttons:
                self.remove_com_player()

    def create_com_player_buttons(self):
        self.button_sections = self.no_computer_buttons_sections.copy()
        self.com_player_buttons_sections = []
        self.com_player_buttons = []
        for i, player in enumerate(self.players[1:]):
            button = Button(
                y=self.slot_const["height"] * i,
                **self.slot_params | {"text": player["name"], "font_size": 20},
            )
            self.com_player_buttons.append(button)
            self.com_player_buttons_sections.append([button])

        self.button_sections += self.com_player_buttons_sections

    def get_com_number(self):
        return len(self.players) - 1

    def add_com_player(self):
        if len(self.players) < 6:
            self.players.append(
                {
                    "id": len(self.players),
                    "name": f"Computer {len(self.players)}",
                    "is_com": True,
                }
            )
        self.create_com_player_buttons()

    def sub_com_player(self):
        if len(self.players) > 2:
            self.players.pop()
        self.create_com_player_buttons()

    def remove_com_player(self):
        if len(self.players) > 2:
            self.players.pop()
            self.create_com_player_buttons()
            self.hovered_button = self.com_player_buttons[-1]
            self.hovered_button.hover()

    def start_game(self):
       
        game_screen = GameScreen(self.screen, self.clock, self.options, self.players)
        game_screen.run()
