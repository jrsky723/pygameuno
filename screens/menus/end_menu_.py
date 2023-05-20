import pygame
from screens.menu_screen import MenuScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.constants import MUSIC as M
from utils.json import load_json


class EndMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options, winner, game_info):
        super().__init__(screen, clock, options)
        pygame.mixer.music.pause()
        self.winner = winner
        self.texts += [TextBox(text="GAME OVER", **self.title_params)]
        self.game_info = game_info
        if winner.in_game_achievements is not None:
            in_game_achievement = winner.in_game_achievements
            self.achievements = load_json("achievements")
            self.update_achievements(
                self.achievements, in_game_achievement, self.game_info
            )
            self.save_achievements()
        self.winner_text = TextBox(
            text=f"{self.winner.get_name()} wins!",
            **self.rect_params,
            x="center",
            y=200,
        )
        self.texts += [self.winner_text]

        B_Y, B_GAP = 350, 150
        buttons_params = self.rect_params | {"x": "center", "width": 300, "height": 100}
        self.home_button = Button(y=B_Y, text="HOME", **buttons_params)
        self.quit_button = Button(y=B_Y + B_GAP, text="QUIT", **buttons_params)

        self.button_sections += [
            [self.home_button],
            [self.quit_button],
        ]

    def button_click_up(self, button):
        super().button_click_up(button)
        if button is not None:
            if button == self.home_button:
                self.open_home()
            elif button == self.quit_button:
                self.quit()

    def open_home(self):
        from screens.menus.start_menu import StartMenuScreen

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(M.MENU_BACKGROUND)
        pygame.mixer.music.play(-1)
        start_menu_screen = StartMenuScreen(self.screen, self.clock, self.options)
        start_menu_screen.run()

    def update_achievements(
        self,
        achievements,
        in_game_achievements,
        game_info,
    ):
        if game_info["mode"] == "story":
            if game_info["zone"] == "red_zone":
                achievements["single player mode"]["story mode"]["red"] += 1
            elif game_info["zone"] == "green":
                achievements["single player mode"]["story mode"]["green"] += 1
            elif game_info["zone"] == "yellow":
                achievements["single player mode"]["story mode"]["yellow"] += 1
            elif game_info["zone"] == "blue":
                achievements["single player mode"]["story mode"]["blue"] += 1
        else:
            achievements["single player mode"]["single mode"] += 1
        self.update_in_game_achievements(
            achievements["single player mode"]["in game"], in_game_achievements
        )

    def update_in_game_achievements(self, target, in_game_achievements):
        if in_game_achievements["draw"] > 10:
            target["over 10 draws"] += 1
        if in_game_achievements["uno"] > 10:
            target["over 10 unos"] += 1
        if in_game_achievements["10 turns"]:
            target["in 10 turns"] += 1
        if in_game_achievements["no action card"]:
            target["no action card"] += 1
        if in_game_achievements["after other uno"]:
            target["after other uno"] += 1
        if in_game_achievements["over 15 cards"]:
            target["over 15 cards"] += 1

    def save_achievements(self):
        from utils.json import save_json

        save_json("achievements", self.achievements)
