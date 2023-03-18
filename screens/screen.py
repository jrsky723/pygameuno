import pygame
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR


class Screen:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.screen_size = options["screen_size"]
        self.screen_width = SCREEN_WIDTH[self.screen_size]
        self.screen_height = SCREEN_HEIGHT[self.screen_size]
        self.background_color = BACKGROUND_COLOR

    def handle_quit_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def process_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while True:
            self.process_events()
            self.update()
            self.draw()
            pygame.display.update()
