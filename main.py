import pygame
from screens.start_menu import StartMenu
from utils.helpers import load_options
from utils.constants import *

FPS = 60

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Pygame Uno")
    options = load_options()
    screen_size = options["screen_size"]
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH[screen_size], SCREEN_HEIGHT[screen_size])
    )
    clock = pygame.time.Clock()

    start_menu = StartMenu(screen, options)

    while True:
        clock.tick(FPS)
        start_menu.run()

    pygame.quit()
    quit()
