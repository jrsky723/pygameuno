import pygame
from screens.menus.start_menu import StartMenuScreen as MenuScreen
from utils.json import load_json
from utils.constants import SCREEN as S, MUSIC as M
import sys

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Pygame Uno")
    options = load_json("options")
    achievements = load_json("achievements")
    screen_size = options["screen_size"]
    screen = pygame.display.set_mode(
        (S.WIDTH[screen_size], S.HEIGHT[screen_size]), pygame.DOUBLEBUF
    )
    clock = pygame.time.Clock()
    pygame.mixer.music.load(M.MENU_BACKGROUND)
    pygame.mixer.music.play(-1)
    pygame.event.get()
    start_menu = MenuScreen(screen, clock, options)
    start_menu.run()
    pygame.quit()
    sys.exit()
