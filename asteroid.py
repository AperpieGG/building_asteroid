import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, (255, 255, 255),
                           (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Pick a random angle between 20–50 degrees
        random_angle = random.uniform(20, 50)

        # Compute new directions by rotating velocity vector
        direction1 = self.velocity.rotate(random_angle) * 1.2
        direction2 = self.velocity.rotate(-random_angle) * 1.2

        # Create new asteroids with new direction and radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = direction1
        asteroid1.add(*self.containers)

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = direction2
        asteroid2.add(*self.containers)

        # Remove the original asteroid
        self.kill()
