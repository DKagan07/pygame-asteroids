import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, PLAYER_SPEED


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            width=2,
            radius=self.radius,
            center=(self.position[0], self.position[1]),
            surface=screen,
            color="white",
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # small asteroid, just kill it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast1.velocity = vel1 * 1.2
        ast2.velocity = vel2 * 1.2
