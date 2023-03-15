import pygame
from fonts import get_text_surface

pygame.init()

screen = pygame.display.set_mode((800, 600))

text_surface = get_text_surface("Hello, world!", "Arial", 50)

screen.blit(text_surface, (100, 100))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
