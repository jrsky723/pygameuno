from animations.animation import Animation


class MoveAnimation(Animation):
    def __init__(self, obj, src_pos, dest_pos, delay, duration, move_info):
        super().__init__(obj, delay, duration)
        # position is a tuple of (x, y) coordinates
        self.src_pos = src_pos
        self.dest_pos = dest_pos
        self.move_info = move_info

    def update(self):
        super().update()
        self.obj.x = (
            self.src_pos[0] + (self.dest_pos[0] - self.src_pos[0]) * self.progress
        )
        self.obj.y = (
            self.src_pos[1] + (self.dest_pos[1] - self.src_pos[1]) * self.progress
        )

    def set_dest_pos(self, pos):
        self.dest_pos = pos
