import pygame
from utils.constants import *
from utils.fonts import get_text_surface


class SettingsMenu:
    pass

    def __init__(self, screen):
        self.screen = screen
        self.background_color = BACKGROUND_COLOR
        self.back_button = pygame.Rect(20, 20, 100, 50)
        self.back_text = get_text_surface("Back", "Arial", "medium", TEXT_COLOR)
        self.is_back = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.back_button.collidepoint(pos):
                    self.is_back = True

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.background_color)
        pygame.draw.rect(self.screen, BUTTON_COLOR, self.back_button)
        self.screen.blit(
            self.back_text,
            (
                self.back_button.x
                + self.back_button.width / 2
                - self.back_text.get_width() / 2,
                self.back_button.y
                + self.back_button.height / 2
                - self.back_text.get_height() / 2,
            ),
        )

    def run(self):
        while True:
            self.process_events()
            self.update()
            self.draw()
            pygame.display.update()
            if self.is_back:
                return
