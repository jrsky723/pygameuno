import time


class Animation:  # duration is in seconds
    def __init__(self, obj, duration, delay=0):
        self.obj = obj
        self.duration = duration
        self.start_time = time.time() + delay
        self.elapsed_time = 0
        self.progress = 0

    def update(self):
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
