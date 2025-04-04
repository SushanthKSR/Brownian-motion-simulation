import numpy as np
import random

class BrownianRobot:
    def __init__(self, arena_size=500, speed=2):
        self.arena_size = arena_size
        self.x = self.y = arena_size // 2
        self.angle = np.random.uniform(0, 2 * np.pi)
        self.speed = speed

    def move(self):
        dx = self.speed * np.cos(self.angle)
        dy = self.speed * np.sin(self.angle)
        self.x += dx
        self.y += dy

        if self._check_collision():
            self._handle_collision()

    def _check_collision(self):
        return not (0 < self.x < self.arena_size and 0 < self.y < self.arena_size)

    def _handle_collision(self):
        self.x = min(max(self.x, 0), self.arena_size)
        self.y = min(max(self.y, 0), self.arena_size)
        self.angle += np.radians(random.uniform(30, 150))
        self.angle %= 2 * np.pi

    def get_position(self):
        return self.x, self.y
