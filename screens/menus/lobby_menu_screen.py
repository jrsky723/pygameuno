import pygame
from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from renders.input_box import InputBox
from utils.color_conversion import rgb


players_sample = [
    {
        "id": "0",
        "is_host": True,
        "is_com": False,
        "name": "Player 1",
        "ip": "127.0.0.1",
        "is_ready": False,
    },
    {
        "id": "1",
        "is_host": False,
        "is_com": False,
        "name": "Player 2",
        "ip": "127.0.0.2",
        "is_ready": False,
    },
    {
        "id": "2",
        "is_host": False,
        "is_com": False,
        "name": "Player 3",
        "ip": "127.0.0.4",
        "is_ready": False,
    },
    {
        "id": "3",
        "is_host": False,
        "is_com": False,
        "name": "Player 4",
        "ip": "127.0.0.5",
        "is_ready": False,
    },
]


# TODO: lobby screen, player list, password, start button, back button
class LobbyMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options, isHost):
        super().__init__(screen, clock, options)
        self.is_host = isHost
        self.my_id = 0
        self.players = players_sample
        self.host = next(p for p in self.players if p["is_host"])
        self.my_player = self.players[self.my_id]
        self.other_players = [p for p in self.players if p != self.my_player]
        self.password = ""
        self.max_players = 6
        self.texts += [TextBox(text="LOBBY", **self.title_params)]
        T_X, T_Y, T_GAP = 200, 250, 60
        text_params = self.rect_params | {"x": T_X, "font_size": 30}
        self.texts += [
            TextBox(y=T_Y, text=f"Host IP: {self.host['ip']}", **text_params),
            TextBox(
                y=T_Y + T_GAP,
                text=f"Current Players: {len(self.players)}/{self.max_players}",
                **text_params,
            ),
            TextBox(
                y=T_Y + T_GAP * 2, text=f"Host Name: {self.host['name']}", **text_params
            ),
        ]
        buttons_params = self.rect_params | {
            "width": 1280 * (1 / 5),
            "height": 720 * (1 / 10),
            "font_size": 30,
        }
        B_X, B_Y, B_GAP = 1280 * (3 / 5) + 20, 720 * (7 / 10) + 10, 720 * (1 / 10) + 30
        ready_start_params = buttons_params | {"x": B_X}
        self.ready_button = Button(y=B_Y, text="READY", **ready_start_params)
        self.start_button = Button(y=B_Y + B_GAP, text="START", **ready_start_params)
        self.button_sections += [[self.ready_button], [self.start_button]]
        self.back_button = Button(
            x=T_X - 10, y=90, text="BACK", **self.rect_params, font_size=30, width=150
        )
        self.button_sections += [[self.back_button]]

        self.my_info_surface_const = {
            "pos": (0, self.screen_height * (7 / 10)),
            "size": (self.screen_width * (3 / 5), self.screen_height * (3 / 10)),
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
        for i, player in enumerate(self.other_players):
            self.draw_player(
                self.other_info_surfaces[i], self.other_players[i], is_me=False
            )

    def draw_blank(self, surface):
        # draw add player button and add com button

        pass

    def draw_blanks(self):
        for i in range(self.max_players - len(self.players)):
            self.draw_blank(self.other_info_surfaces[i])

    def draw(self):
        super().draw()
        self.draw_surfaces()
        self.draw_players()
