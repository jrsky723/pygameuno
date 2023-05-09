import pytest
from unittest.mock import MagicMock
from animations.animation import Animation
import time


class TestAnimation:
    def test_init(self):
        obj = MagicMock()
        delay = 1.0
        duration = 2.0
        animation = Animation(obj, delay, duration)

        assert animation.obj == obj
        assert animation.delay == delay
        assert animation.duration == duration
        assert animation.elapsed_time == 0
        assert animation.progress == 0
        assert animation.sound_played == False

    def test_update(self):
        obj = MagicMock()
        delay = 0.5
        duration = 1.0
        animation = Animation(obj, delay, duration)

        animation.update()
        obj.update.assert_not_called()

        time.sleep(delay)
        animation.update()
        obj.update.assert_called_once()

        time.sleep(duration)
        animation.update()
        assert animation.progress == 1
        assert animation.is_finished() == True

    def test_draw(self):
        obj = MagicMock()
        screen = MagicMock()
        delay = 0.5
        duration = 1.0
        animation = Animation(obj, delay, duration)

        animation.draw(screen)
        obj.draw.assert_called_once_with(screen)

    def test_sound_played(self):
        obj = MagicMock()
        delay = 0.5
        duration = 1.0
        animation = Animation(obj, delay, duration)

        assert animation.get_sound_played() == False
        animation.set_sound_played(True)
        assert animation.get_sound_played() == True

    def test_is_delay_finished(self):
        obj = MagicMock()
        delay = 0.5
        duration = 1.0
        animation = Animation(obj, delay, duration)

        assert animation.is_delay_finished() == False
        time.sleep(delay)
        animation.update()
        assert animation.is_delay_finished() == True
