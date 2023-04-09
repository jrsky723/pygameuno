import time


class Timer:
    def __init__(self):
        self.seconds = 0
        self.start_time = None
        self.remaining_time = 0

    def set_timer(self, seconds):
        self.seconds = seconds
        self.remaining_time = seconds

    def start(self):
        self.start_time = time.time()

    def pause(self):
        if self.start_time is not None:
            self.remaining_time = self.seconds - (time.time() - self.start_time)
            self.start_time = None

    def resume(self):
        if self.start_time is None:
            self.start_time = time.time()
            self.seconds = self.remaining_time

    def reset(self):
        self.start_time = None
        self.remaining_time = self.seconds

    def is_finished(self):
        return (
            self.start_time is not None
            and time.time() - self.start_time >= self.seconds
        )

    def is_running(self):
        return not self.is_finished()

    def get_remaining_time(self):
        if self.start_time is None:
            return self.remaining_time
        else:
            return self.seconds - (time.time() - self.start_time)


def wait(seconds):
    time.sleep(seconds)
