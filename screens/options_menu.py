import pygame
from classes.button import Button
from classes.text_box import TextBox
from screens.screen import Screen
from utils.constants import *
from utils.helpers import save_options


class OptionsMenu(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)

    def run(self):
        print("Options Screen Running")
        pass

    # def __init__(self, screen, options):
    #     self.title = TextBox(
    #         x="center",
    #         y=self.screen_height // 10,
    #         size=self.screen_size,
    #         text="OPTIONS",
    #         text_color=GREEN,
    #     )
    #     self.texts = [
    #         TextBox(
    #             x=self.screen_width // 8,
    #             y=self.screen_height // 10 * 3,
    #             size=self.screen_size,
    #             text="SCREEN SIZE",
    #         ),
    #         TextBox(
    #             x=self.screen_width // 8,
    #             y=self.screen_height // 10 * 5,
    #             size=self.screen_size,
    #             text="VOLUME",
    #         ),
    #         TextBox(
    #             x=self.screen_width // 8,
    #             y=self.screen_height // 10 * 7,
    #             size=self.screen_size,
    #             text="COLOR BLIND",
    #         ),
    #     ]
    #     self.screen_size_buttons = [
    #         Button(
    #             x=self.screen_width // 8 * 5,
    #             y=self.screen_height // 10 * 3,
    #             size=self.screen_size,
    #             text="SMALL",
    #         ),
    #         Button(
    #             x=self.screen_width // 8 * 6,
    #             y=self.screen_height // 10 * 3,
    #             size=self.screen_size,
    #             text="MEDIUM",
    #         ),
    #         Button(
    #             x=self.screen_width // 8 * 7,
    #             y=self.screen_height // 10 * 3,
    #             size=self.screen_size,
    #             text="LARGE",
    #         ),
    #     ]
    #     self.save_and_back_button = Button(
    #         x="center",
    #         y=self.screen_height // 10 * 9,
    #         size=self.screen_size,
    #         text="SAVE AND BACK",
    #     )
    #     self.selected_button = 0

    # def draw(self):
    #     self.screen.fill(BLACK)
    #     self.title.draw(self.screen)
    #     for text in self.texts:
    #         text.draw(self.screen)
    #     for button in self.screen_size_buttons:
    #         button.draw(self.screen)

    #     self.screen = screen
    #     self.options = options
    #     self.background_color = BACKGROUND_COLOR
    #     self.width_text_box = TextBox(
    #         self.screen_width//8, , 200, 50, self.options["width"]
    #     )
    #     self.height_text_box = TextBox(
    #         self.screen_width//8, 300, 200, 50, self.options["height"]
    #     )
    #     self.volume_text_box = TextBox(
    #         self.screen_width//8, 400, 200, 50, self.options["volume"]
    #     )
    #     self.color_blind_button = Button(
    #         self.screen,
    #         300,
    #         500,
    #         200,
    #         50,
    #         "Color Blind: " + str(self.options["color_blind"]),
    #     )
    #     self.back_button = Button(self.screen, 300, 600, 200, 50, "Back")

    # def draw(self):
    #     self.screen.fill(BLACK)

    #     self.width_text_box.draw()
    #     self.height_text_box.draw()
    #     self.volume_text_box.draw()
    #     self.color_blind_button.draw()
    #     self.back_button.draw()

    #     pygame.display.update()

    # def run(self):
    #     self.width_text_box.update()
    #     self.height_text_box.update()
    #     self.volume_text_box.update()
    #     self.color_blind_button.update()
    #     self.back_button.update()

    #     if self.color_blind_button.clicked:
    #         self.options["color_blind"] = not self.options["color_blind"]
    #         self.color_blind_button.text = "Color Blind: " + str(
    #             self.options["color_blind"]
    #         )

    #     if self.back_button.clicked:
    #         self.options["width"] = self.width_text_box.text
    #         self.options["height"] = self.height_text_box.text
    #         self.options["volume"] = self.volume_text_box.text
    #         save_options(self.options)
    #         return "start_menu"

    #     self.draw()
