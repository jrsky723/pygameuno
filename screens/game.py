import pygame
from screens.screen import Screen
from utils.constants import SCREEN as S
from utils.color_conversion import rgb


class GameScreen(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.player_name = options["player_name"]
        self.font = pygame.font.Font(None, S.FONT_SIZE)
        self.text_surface = self.font.render(
            f"Hello, {self.player_name}!", True, rgb("white", self.color_blind)
        )
        self.text_rect = self.text_surface.get_rect(
            center=(
                self.screen_width // 2,
                self.screen_height // 2,
            )
        )

    def draw(self):
        super().draw()
        self.screen.blit(self.text_surface, self.text_rect)
