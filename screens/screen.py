import pygame
import traceback
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

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def return_down(self):
        pass

    def return_up(self):
        pass

    def handle_movement(self, event):
        if event.key == pygame.key.key_code(self.key_bindings["up"]):
            self.move_up()
        elif event.key == pygame.key.key_code(self.key_bindings["down"]):
            self.move_down()
        elif event.key == pygame.key.key_code(self.key_bindings["left"]):
            self.move_left()
        elif event.key == pygame.key.key_code(self.key_bindings["right"]):
            self.move_right()

    def handle_return_down(self, event):
        if event.key == pygame.key.key_code(self.key_bindings["return"]):
            self.return_down()

    def handle_return_up(self, event):
        if event.key == pygame.key.key_code(self.key_bindings["return"]):
            self.return_up()

    def handle_quit_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def handle_mouse_event(self, event):
        pass

    def handle_key_event(self, event):
        pass

    def process_events(self):
        for event in pygame.event.get():
            self.handle_quit_event(event)
            self.handle_mouse_event(event)
            self.handle_key_event(event)

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

    def main_loop(self):
        self.process_events()
        self.update()
        self.draw()
        pygame.display.update()

    def run(self):
        try:
            while self.running:
                self.main_loop()
        except Exception as e:
            traceback.print_exc()
            self.quit()
