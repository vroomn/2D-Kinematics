import pygame
import math

# Holds information for an object, functions to simulate 2D kinematic behavior, and general helper functions
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

    # Locks a given angle in degrees between 1 and the specified max angle (best practice is 90D)
    def clampLaunchAngle(self, maxAngle: int) -> None:
        if self.launchAngle > maxAngle: self.launchAngle = maxAngle
        elif self.launchAngle < 1: self.launchAngle = 1

    # Draw call to pygame, blits filled circle onto screen surface
    def draw(self, screen: pygame.Surface) -> None: 
        pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), self.radius, (self.color))

    # Determines time since start of simulation and sets the position accordinly based on the Physics 1 distance formula (https://www.physicsclassroom.com/calcpad/1dkin/Equation-Overview)
    def physicsStep(self, tick: int, screen: pygame.Surface) -> None:
        # Time elapsed since start of program
        time = (pygame.time.get_ticks() - tick) / 1000

        # Y component calculation
        self.position.y = screen.get_height() - ( ((self.initVelocity*math.sin(math.radians(self.launchAngle)))*time) + (.5)*(self.gravity)*(time)**2 )*5

        # X Component calculation (removed acceleration because X acc is a constant zero)
        self.position.x = ((self.initVelocity*math.cos(math.radians(self.launchAngle)))*time)*5