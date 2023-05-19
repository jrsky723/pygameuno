import pygame


def draw_x(surface, color, width=3):
    # draw X in the middle of the surface
    s_width, s_height = surface.get_width(), surface.get_height()
    pygame.draw.line(surface, color, (0, 0), (s_width, s_height), width)
    pygame.draw.line(surface, color, (0, s_height), (s_width, 0), width)


def draw_inner_border(surface, color, width=3):
    pygame.draw.rect(
        surface,
        color,
        (0, 0, surface.get_width(), surface.get_height()),
        width,
    )
