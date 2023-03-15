import pygame
from utils.constants import *
from classes.button import Button


class EndMenu:
    pass
    # def __init__(self, screen):
    #     self.screen = screen
    #     self.background_color = BACKGROUND_COLOR

    #     self.start_button = Button(
    #         (SCREEN_WIDTH / 2) - 75,
    #         SCREEN_HEIGHT / 2 - 100,
    #         150,
    #         50,
    #         "Start",
    #         TEXT_COLOR,
    #         BUTTON_COLOR,
    #     )
    #     self.settings_button = Button(
    #         (SCREEN_WIDTH / 2) - 75,
    #         SCREEN_HEIGHT / 2,
    #         150,
    #         50,
    #         "Settings",
    #         TEXT_COLOR,
    #         BUTTON_COLOR,
    #     )
    #     self.end_button = Button(
    #         (SCREEN_WIDTH / 2) - 75,
    #         SCREEN_HEIGHT / 2 + 100,
    #         150,
    #         50,
    #         "End",
    #         TEXT_COLOR,
    #         BUTTON_COLOR,
    #     )
    #     self.is_running = True
    #     self.buttons = [self.start_button, self.settings_button, self.end_button]
    #     self.selected_button = 0

    # def process_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #         # Mouse Controls
    #         elif event.type == pygame.MOUSEMOTION:
    #             pos = pygame.mouse.get_pos()
    #             for i, button in enumerate(self.buttons):
    #                 if button.is_on_mouse(pos):
    #                     self.selected_button = i
    #         elif event.type == pygame.MOUSEBUTTONUP:
    #             self.select_button()

    #         # Keyboard Controls
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_UP:
    #                 self.selected_button = (self.selected_button - 1) % len(
    #                     self.buttons
    #                 )
    #             elif event.key == pygame.K_DOWN:
    #                 self.selected_button = (self.selected_button + 1) % len(
    #                     self.buttons
    #                 )
    #             elif event.key == pygame.K_RETURN:
    #                 self.select_button()

    # def update(self):
    #     pass

    # def draw(self):
    #     self.screen.fill(self.background_color)
    #     for i, button in enumerate(self.buttons):
    #         button.draw(self.screen, selected=i == self.selected_button)

    # def select_button(self):
    #     self.buttons[self.selected_button].click()
    #     if self.selected_button == 0:
    #         self.start_game()
    #     elif self.selected_button == 1:
    #         self.settings()
    #     elif self.selected_button == 2:
    #         self.end()

    # def start_game(self):
    #     game_screen = GameScreen(self.screen)
    #     game_screen.run()
    #     pass

    # def settings(self):
    #     settings_menu = SettingsMenu(self.screen)
    #     settings_menu.run()

    # def end(self):
    #     end_menu = EndMenu(self.screen)
    #     end_menu.run()

    # def run(self):
    #     while True:
    #         self.process_events()
    #         self.update()
    #         self.draw()
    #         pygame.display.update()
