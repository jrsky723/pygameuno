import pygame
from utils.constants import SCREEN as S
from utils.color_conversion import rgb


class Screen:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.screen_size = options["screen_size"]
        self.color_blind = options["color_blind"]
        self.rect_params = {
            "screen_size": self.screen_size,
            "color_blind": self.color_blind,
        }
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.background_color = rgb(S.BACKGROUND_COLOR, self.color_blind)

    def handle_quit_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def process_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.background_color)

    def run(self):
        while True:
            self.process_events()
            self.update()
            self.draw()
            pygame.display.update()
