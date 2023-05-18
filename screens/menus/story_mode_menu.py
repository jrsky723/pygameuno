from screens.menu_screen import MenuScreen
from screens.menus.story_mode_start_menu import StoryModeStartMenuScreen
from renders.button import Button
from renders.text_box import TextBox
from utils.constants import IMAGE
from utils.json import load_json
import pygame


class StoryModeMenuScreen(MenuScreen):
    def __init__(self, screen, clock, options):
        super().__init__(screen, clock, options)
        self.achievements = load_json("achievements")
        self.game_info = {
            "mode": "story",
        }
        self.zone_available = {
            "red_zone": True,
            "green_zone": False,
            "yellow_zone": False,
            "blue_zone": False,
        }
        # 하나의 영역이 완료되면 그 다음 영역이 해금된다. 예를들어 red_zone가 완료되면 green_zone가 해금된다.
        self.zone_available["green_zone"] = (
            self.achievements["single player mode"]["story mode"]["red"] >= 1
        )
        self.zone_available["yellow_zone"] = (
            self.achievements["single player mode"]["story mode"]["green"] >= 1
        )
        self.zone_available["blue_zone"] = (
            self.achievements["single player mode"]["story mode"]["yellow"] >= 1
        )

        self.texts += [TextBox(text="STORY MODE", **self.title_params)]
        self.background_image = pygame.image.load(IMAGE.STORY_MODE)
        self.background_image = pygame.transform.scale(
            self.background_image, (self.screen_width, self.screen_height)
        )
        B_W, B_H = 120, 50
        button_params = {
            "width": B_W,
            "height": B_H,
            "text": "START",
            "font_size": 25,
        } | self.rect_params

        self.red_zone_button = Button(x=320, y=310, **button_params)
        self.green_zone_button = Button(x=500, y=600, **button_params)
        self.yellow_zone_button = Button(x=780, y=380, **button_params)
        self.blue_zone_button = Button(x=830, y=520, **button_params)
        self.start_buttons = [
            self.red_zone_button,
            self.green_zone_button,
            self.yellow_zone_button,
            self.blue_zone_button,
        ]
        self.button_sections.append([self.red_zone_button])
        if self.zone_available["green_zone"]:
            self.button_sections.append([self.green_zone_button])
        if self.zone_available["yellow_zone"]:
            self.button_sections[0].append(self.yellow_zone_button)
        if self.zone_available["blue_zone"]:
            self.button_sections[1].append(self.blue_zone_button)

        self.back_button = Button(x=20, y=20, **button_params | {"text": "BACK"})
        self.button_sections.append([self.back_button])

    def draw(self):
        super().draw()
        self.screen.blit(self.background_image, (0, 0))

    def button_click_up(self, button):
        super().button_click_up(button)
        # use button index to find zone
        if button in self.start_buttons:
            zone = list(self.zone_available.keys())[self.start_buttons.index(button)]
            self.open_story_mode_start(zone)

    def open_story_mode_start(self, zone):
        game_info = self.game_info | {"zone": zone}
        story_mode_start_menu_screen = StoryModeStartMenuScreen(
            self.screen, self.clock, self.options, game_info
        )
        story_mode_start_menu_screen.run()
        pass
