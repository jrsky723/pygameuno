import pygame
from screens.menus.start_menu_screen import StartMenuScreen
from utils.options import load_options_json
from utils.constants import SCREEN as S, BACKGROUND_MUSIC

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Pygame Uno")
    options = load_options_json()
    screen_size = options["screen_size"]
    screen = pygame.display.set_mode(
        (S.WIDTH[screen_size], S.HEIGHT[screen_size]), pygame.DOUBLEBUF
    )
    clock = pygame.time.Clock()
    start_menu = StartMenuScreen(screen, clock, options)
    pygame.mixer.music.load(BACKGROUND_MUSIC)
    pygame.mixer.music.play(-1)
    pygame.event.get()
    start_menu.run()
    pygame.quit()
    quit()
