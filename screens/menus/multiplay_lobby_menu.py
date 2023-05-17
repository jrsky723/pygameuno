import pygame
from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from renders.input_box import InputBox
from utils.color_conversion import rgb


# players_sample = [
#     {
#         "id": "0",
#         "is_host": True,
#         "name": "Player 1",
#         "ip": "127.0.0.1",
#         "is_ready": False,
#     },
#     {
#         "id": "1",
#         "is_host": False,
#         "name": "Player 2",
#         "ip": "127.0.0.2",
#         "is_ready": False,
#     },
#     {
#         "id": "2",
#         "is_host": False,
#         "name": "Player 3",
#         "ip": "127.0.0.4",
#         "is_ready": False,
#     },
#     {
#         "id": "3",
#         "is_host": False,
#         "name": "Player 4",
#         "ip": "127.0.0.5",
#         "is_ready": False,
#     },
# ]

players_sample = [
    {
        "id": "0",
        "is_host": True,
        "name": "Player 1",
        "ip": "127.0.0.1",
        "is_ready": False,
    },
]


# TODO: lobby screen, player list, password, start button, back button
class MultiplayLobbyMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options, isHost):
        super().__init__(screen, clock, options)
        self.is_host = isHost
        self.my_id = 0
        self.players = players_sample
        self.host = next(p for p in self.players if p["is_host"])
        self.my_player = self.players[self.my_id]
        self.other_players = [p for p in self.players if p != self.my_player]
        self.password = "current password"
        self.max_players = 6
        self.opend_slots = 0
        self.texts += [TextBox(text="LOBBY", **self.title_params)]
        T_X, T_Y, T_GAP = 200, 200, 60
        text_params = self.rect_params | {"x": T_X, "font_size": 30}
        self.current_player_text = TextBox(
            y=T_Y + T_GAP,
            text=f"Current Players: {len(self.players)}/{len(self.players) + self.opend_slots}",
            **text_params,
        )

        self.texts += [
            TextBox(y=T_Y, text=f"Host IP: {self.host['ip']}", **text_params),
            self.current_player_text,
            TextBox(
                y=T_Y + T_GAP * 2, text=f"Host Name: {self.host['name']}", **text_params
            ),
            TextBox(y=T_Y + T_GAP * 3, text="PASSWORD: ", **text_params),
            TextBox(y=T_Y + T_GAP * 4, text="KICK: ", **text_params),
        ]
        # self.is_host = False
        # Host only
        if self.is_host:
            slot_button_params = self.rect_params | {
                "width": 50,
                "height": 50,
                "font_size": 30,
                "y": T_Y + T_GAP - 15,
            }
            self.slot_down_button = Button(x=T_X + 500, text="-", **slot_button_params)
            self.slot_up_button = Button(x=T_X + 560, text="+", **slot_button_params)
            self.button_sections += [
                [self.slot_down_button, self.slot_up_button],
            ]

            input_params = self.rect_params | {
                "width": 400,
                "height": 50,
                "x": 420,
                "font_size": 30,
            }
            self.password_input_box = InputBox(
                y=T_Y + T_GAP * 3 - 15, text=f"{self.password}", **input_params
            )
            self.input_boxes.append(self.password_input_box)
            button_params = self.rect_params | {
                "x": 830,
                "width": 120,
                "height": 50,
                "font_size": 20,
            }
            self.password_change_button = Button(
                y=T_Y + T_GAP * 3 - 15, text="CHANGE", **button_params
            )
            self.button_sections += [
                [self.password_input_box, self.password_change_button]
            ]
            self.kick_input_box = InputBox(
                y=T_Y + T_GAP * 4 - 15, text=f"Player Name", **input_params
            )
            self.input_boxes.append(self.kick_input_box)
            self.kick_button = Button(
                y=T_Y + T_GAP * 4 - 15, text="KICK", **button_params
            )
            self.button_sections += [[self.kick_input_box, self.kick_button]]

        else:
            # erase x in text_params
            text_params.pop("x")
            self.password_text = TextBox(
                x=420, y=T_Y + T_GAP * 3, text=f"{self.password}", **text_params
            )
            self.host_only_kick_text = TextBox(
                x=340, y=T_Y + T_GAP * 4, text="Only host can kick", **text_params
            )
            self.texts += [self.password_text, self.host_only_kick_text]

        buttons_params = self.rect_params | {
            "width": 1280 * (1 / 5),
            "height": 720 * (1 / 10),
            "font_size": 30,
        }
        B_X, B_Y, B_GAP = 1280 * (1 / 3), 720 * (7 / 10) + 10, 720 * (1 / 10) + 30
        name_params = buttons_params | {"x": 420, "width": 400, "font_size": 35}
        self.name_input_box = InputBox(
            y=B_Y, text=f"{self.my_player['name']}", **name_params
        )
        self.input_boxes.append(self.name_input_box)
        self.name_change_button = Button(
            x=830,
            y=B_Y,
            text="CHANGE",
            **buttons_params | {"width": 120, "font_size": 20},
        )
        self.button_sections += [[self.name_input_box, self.name_change_button]]
        ready_start_params = buttons_params | {"y": B_Y + B_GAP}
        ready_start_section = []
        self.ready_button = Button(x=B_X, text="READY", **ready_start_params)
        ready_start_section.append(self.ready_button)
        if self.is_host:
            self.start_button = Button(x=B_X + 270, text="START", **ready_start_params)
            ready_start_section.append(self.start_button)
        self.button_sections += [ready_start_section]
        self.back_button = Button(
            x=T_X - 10, y=90, text="BACK", **self.rect_params, font_size=30, width=150
        )
        self.button_sections += [[self.back_button]]

        self.my_info_surface_const = {
            "pos": (0, self.screen_height * (7 / 10)),
            "size": (self.screen_width * (2 / 7), self.screen_height * (3 / 10)),
        }

        self.other_info_surface_const = {
            "pos": (self.screen_width * (5 / 6), 0),
            "size": (self.screen_width / 6, self.screen_height / 5),
            "gap": (self.screen_height / 5),
        }

        self.my_info_surface = None
        self.other_info_surfaces = []
        self.create_surfaces()

    def create_surfaces(self):
        self.my_info_surface = pygame.Surface(self.my_info_surface_const["size"])
        for _ in range(self.max_players - 1):
            self.other_info_surfaces.append(
                pygame.Surface(self.other_info_surface_const["size"])
            )
        self.surfaces = [self.my_info_surface] + self.other_info_surfaces

    def draw_surfaces(self):
        self.screen.blit(self.my_info_surface, self.my_info_surface_const["pos"])
        for i, surface in enumerate(self.other_info_surfaces):
            self.screen.blit(
                surface,
                (
                    self.other_info_surface_const["pos"][0],
                    self.other_info_surface_const["pos"][1]
                    + self.other_info_surface_const["gap"] * i,
                ),
            )
        # fill surfaces & add inner border
        for surface in self.surfaces:
            surface.fill(self.background_color)
            self.add_inner_border(surface, rgb("white"), 3)

    def add_inner_border(self, surface, color, width):
        pygame.draw.rect(
            surface,
            color,
            (0, 0, surface.get_width(), surface.get_height()),
            width,
        )

    def draw_player(self, surface, player, is_me):
        s_width, s_height = surface.get_width(), surface.get_height()
        FONT_SIZE = 35 if is_me else 20
        text_params = {"font_size": FONT_SIZE, "reposition": False} | self.rect_params
        player_name_text = TextBox(
            text=player["name"], x=20, y=s_height * 0.15, **text_params
        )
        player_name_text.draw(surface)
        ready_params = text_params | {"x": s_width * 0.1, "y": s_height * 0.5}
        if player["is_ready"]:
            ready_text = TextBox(text="READY", **ready_params, text_color="green")
        else:
            ready_text = TextBox(text="NOT READY", **ready_params, text_color="red")
        ready_text.draw(surface)

    def draw_players(self):
        self.draw_player(self.my_info_surface, self.my_player, is_me=True)
        for i in range(len(self.other_players)):
            self.draw_player(
                self.other_info_surfaces[i], self.other_players[i], is_me=False
            )

    def draw_blank(self, surface):
        # draw X in the middle of the surface
        s_width, s_height = surface.get_width(), surface.get_height()
        pygame.draw.line(surface, rgb("white"), (0, 0), (s_width, s_height), 3)
        pygame.draw.line(surface, rgb("white"), (0, s_height), (s_width, 0), 3)

    def draw_blanks(self):
        for i in range(self.max_players - len(self.players) - self.opend_slots):
            self.draw_blank(
                self.other_info_surfaces[self.opend_slots + i + len(self.other_players)]
            )

    def draw(self):
        super().draw()
        self.draw_surfaces()
        self.draw_players()
        self.draw_blanks()

    def button_click_up(self, button):
        super().button_click_up(button)
        if button != None:
            if button == self.ready_button:
                self.ready()
            elif button == self.name_change_button:
                self.change_name()
        if self.is_host:
            if button == self.start_button:
                self.start()
            if button == self.slot_down_button:
                self.slot_down()
            if button == self.slot_up_button:
                self.slot_up()
            if button == self.kick_button:
                self.kick()
            if button == self.password_change_button:
                self.change_password()

    def ready(self):
        self.my_player["is_ready"] = not self.my_player["is_ready"]

    def slot_down(self):
        self.opend_slots = max(0, self.opend_slots - 1)
        self.update_slot_text()

    def slot_up(self):
        self.opend_slots = min(
            self.max_players - len(self.players), self.opend_slots + 1
        )
        self.update_slot_text()

    def update_slot_text(self):
        self.current_player_text.set_text(
            f"Current Players: {len(self.players)}/{len(self.players) + self.opend_slots}"
        )

    def kick(self):
        pass

    def change_password(self):
        self.password = self.password_input_box.get_text()
        pass

    def change_name(self):
        self.my_player["name"] = self.name_input_box.get_text()
        pass

    def start(self):
        pass
