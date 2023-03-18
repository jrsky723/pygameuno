import pygame
from utils.constants import *
from screens.screen import Screen
from screens.game_screen import GameScreen
from screens.options_menu import OptionsMenu
from classes.button import Button
from classes.text_box import TextBox


class StartMenu(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.title = TextBox(
            x="center",
            y=self.screen_height // 10,
            size=self.screen_size,
            text="Pygame UNO",
            text_color=GREEN,
        )
        self.buttons = [
            Button(
                x="center",
                y=self.screen_height // 10 * 3,
                size=self.screen_size,
                text="START",
            ),
            Button(
                x="center",
                y=self.screen_height // 10 * 5,
                size=self.screen_size,
                text="OPTIONS",
            ),
            Button(
                x="center",
                y=self.screen_height // 10 * 7,
                size=self.screen_size,
                text="QUIT",
            ),
        ]
        self.selected_button = 0

    def process_events(self):
        for event in pygame.event.get():
            self.handle_quit_event(event)
            # Mouse Controls
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for i, button in enumerate(self.buttons):
                    if button.is_on_mouse(pos):
                        self.selected_button = i
            elif event.type == pygame.MOUSEBUTTONUP:
                self.select_button()

            # Keyboard Controls
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_button = (self.selected_button - 1) % len(
                        self.buttons
                    )
                elif event.key == pygame.K_DOWN:
                    self.selected_button = (self.selected_button + 1) % len(
                        self.buttons
                    )
                elif event.key == pygame.K_RETURN:
                    self.select_button()

    def draw(self):
        self.screen.fill(self.background_color)
        self.title.draw(self.screen)
        for i, button in enumerate(self.buttons):
            button.draw(self.screen, selected=i == self.selected_button)

    def select_button(self):
        self.buttons[self.selected_button].click()
        if self.selected_button == 0:
            self.start_game()
        elif self.selected_button == 1:
            self.open_options()
        elif self.selected_button == 2:
            self.quit_game()

    def start_game(self):
        game_screen = GameScreen(self.screen, self.options)
        game_screen.run()
        pass

    def open_options(self):
        options_menu = OptionsMenu(self.screen, self.options)
        options_menu.run()

    def quit_game(self):
        pygame.quit()
        quit()
