from animations.animation import Animation
from utils.draw_functions import draw_x
from utils.color_conversion import rgb


class SkipAnimation(Animation):
    def __init__(
        self,
        surface,
        duration,
        delay=0,
    ):
        super().__init__(None, delay, duration)
        self.surface = surface
        # position is a tuple of (x, y) coordinates

    def draw(self, screen):
        draw_x(self.surface, rgb("red"), 5)
