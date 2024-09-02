import pygame
from circleshape import CircleShape
from constants import PLAYER_SPEED


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
