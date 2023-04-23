import time


class Animation:  # duration is in seconds
    def __init__(self, obj, delay, duration):
        self.obj = obj
        self.start_time = time.time() + delay
        self.delay = delay
        self.duration = duration
        self.elapsed_time = 0
        self.progress = 0
        self.sound_played = False

    def update(self):
        if self.start_time is None:
            return
        self.elapsed_time = time.time() - self.start_time
        self.progress = self.elapsed_time / self.duration
        if self.progress > 1:
            self.progress = 1
        if self.progress < 0:
            self.progress = 0
        self.obj.update()

    def is_finished(self):
        return self.progress == 1

    def draw(self, screen):
        self.obj.draw(screen)

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time + self.delay

    def is_delay_finished(self):
        return self.elapsed_time >= 0

    def get_sound_played(self):
        return self.sound_played

    def set_sound_played(self, sound_played):
        self.sound_played = sound_played
