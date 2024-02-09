import pygame
import math

class PhysicsObject:
    def __init__(self, initVelocity: int, launchAngle: int, gravity: int, radius: int, color: tuple) -> None:
        # Variables for physics sim
        self.initVelocity = initVelocity
        self.launchAngle = launchAngle
        self.clampLaunchAngle(90)
        self.gravity = gravity

        # Rendering variables
        self.radius = radius
        self.color = color
        self.position = pygame.Vector2(100, 100)

    def clampLaunchAngle(self, maxAngle) -> None:
        if self.launchAngle > maxAngle: self.launchAngle = maxAngle
        elif self.launchAngle < 1: self.launchAngle = 1

    def draw(self, screen: pygame.Surface) -> None:
        pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), self.radius, (self.color))

    def physicsStep(self, tick, screen: pygame.Surface) -> None:
        time = (pygame.time.get_ticks() - tick) / 1000

        # Y component
        self.position.y = screen.get_height() - ( ((self.initVelocity*math.sin(math.radians(self.launchAngle)))*time) + (.5)*(self.gravity)*(time)**2 )*5

        # X Component
        self.position.x = ((self.initVelocity*math.cos(math.radians(self.launchAngle)))*time)*5