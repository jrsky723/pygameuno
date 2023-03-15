import pygame
from utils.constants import *
from screens.start_menu import StartMenu

FPS = 60

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Pygame Uno")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    start_menu = StartMenu(screen)

    while True:
        clock.tick(FPS)
        start_menu.run()

    pygame.quit()
    quit()
