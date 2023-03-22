import pygame
from screens.start_menu import StartMenu
from utils.options import load_options_json
from utils.constants import SCREEN as S

FPS = 60
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Pygame Uno")
    options = load_options_json()
    screen_size = options["screen_size"]
    screen = pygame.display.set_mode((S.WIDTH[screen_size], S.HEIGHT[screen_size]))
    clock = pygame.time.Clock()
    start_menu = StartMenu(screen, options)
    while True:
        clock.tick(FPS)
        start_menu.run()
        if not start_menu.running:
            break
    pygame.quit()
    quit()
