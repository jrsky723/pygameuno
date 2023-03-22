import pygame
from utils.constants import SCREEN as S
from utils.color_conversion import rgb


class Screen:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.screen_size = options["screen_size"]
        self.color_blind = options["color_blind"]
        self.key_bindings = options["key_bindings"]
        self.volume = options["volume"]
        self.rect_params = {
            "screen_size": self.screen_size,
            "color_blind": self.color_blind,
        }
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.background_color = rgb(S.BACKGROUND_COLOR, self.color_blind)
        self.running = True

    def handle_quit_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def process_events(self):
        pass

    def update(self):
        if self.screen.get_size() != (self.screen_width, self.screen_height):
            self.screen = pygame.display.set_mode(
                (self.screen_width, self.screen_height)
            )

    def quit(self):
        pygame.quit()
        quit()

    def back(self):
        self.running = False

    def draw(self):
        self.screen.fill(self.background_color)

    def run(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()
            pygame.display.update()
