import pytest
from utils.timer import Timer, wait
import time

def test_timer_initialization():
    timer = Timer()
    assert timer.start_time is None
    assert timer.remaining_time == 0

def test_set_timer():
    timer = Timer()
    timer.set_timer(5)
    assert timer.remaining_time == 5

def test_start():
    timer = Timer()
    timer.set_timer(5)
    timer.start()
    assert timer.start_time is not None

def test_pause_resume():
    timer = Timer()
    timer.set_timer(5)
    timer.start()
    wait(2)
    timer.pause()
    remaining_time_after_pause = timer.get_remaining_time()
    wait(1)
    assert timer.get_remaining_time() == remaining_time_after_pause
    timer.resume()
    assert timer.is_running()

def test_reset():
    timer = Timer()
    timer.set_timer(5)
    timer.start()
    wait(2)
    timer.reset()
    assert timer.start_time is None
    assert timer.remaining_time == 5

def test_is_finished():
    timer = Timer()
    timer.set_timer(1)
    timer.start()
    wait(1.1)
    assert timer.is_finished()

def test_wait():
    start_time = time.time()
    wait(1)
    end_time = time.time()
    assert round(end_time - start_time) == 1
