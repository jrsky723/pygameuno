import pygame
import pytest

from utils.color_conversion import rgb
from utils.constants import SCREEN as S
from renders.rect import Rect

@pytest.fixture(scope='module')
def screen():
    pygame.init()
    return pygame.display.set_mode((S.WIDTH_BASE, S.HEIGHT_BASE))

def test_rect(screen):
    # Given
    x, y, width, height = 50, 50, 100, 100
    screen_size, color_blind = 'medium', False
    reposition, resize = True, True
    background_color = (255, 255, 255)
    border_color, border_width = (255, 0, 0), 2

    # When
    rect = Rect(
        x=x, y=y, width=width, height=height,
        screen_size=screen_size, color_blind=color_blind,
        reposition=reposition, resize=resize,
        background_color=background_color,
        border_color=border_color, border_width=border_width,
    )

    # Then
    assert rect.x == x * 1.5  # assuming medium screen size
    assert rect.y == y * 1.5  # assuming medium screen size
    assert rect.width == width * 1.5  # assuming medium screen size
    assert rect.height == height * 1.5  # assuming medium screen size
    assert rect.background_color == background_color
    assert rect.border_color == border_color
    assert rect.border_width == border_width

    # Test draw
    screen.fill((0, 0, 0))  # fill screen with black color
    rect.draw(screen)  # draw the rectangle
    pygame.display.update()  # update the display
    assert screen.get_at((int(x * 1.5) + border_width // 2, int(y * 1.5) + border_width // 2)) == border_color
    assert screen.get_at((int(x * 1.5) + border_width // 2 + 1, int(y * 1.5) + border_width // 2 + 1)) == background_color
