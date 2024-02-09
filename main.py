import pygame
import pygame.gfxdraw
import math

# Width of the simulator window
WIDTH = 1280
# Height of the simulator window
HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class PhysicsObject:
    def __init__(self, initVelocity: int, launchAngle: int, gravity: int, radius: int, color: tuple) -> None:
        # Variables for physics sim
        self.initVelocity = initVelocity
        self.launchAngle = launchAngle
        self.clampLaunchAngle(90)
        self.gravity = gravity
        self.dStartTime = 0

        # Rendering variables
        self.radius = radius
        self.color = color
        self.position = pygame.Vector2(100, 100)

    def clampLaunchAngle(self, maxAngle) -> None:
        if self.launchAngle > maxAngle: self.launchAngle = maxAngle
        elif self.launchAngle < 1: self.launchAngle = 1

    def draw(self, screen: pygame.Surface) -> None:
        pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), self.radius, (self.color))

    def physicsStep(self, tick) -> None:
        time = (pygame.time.get_ticks() - tick) / 1000

        # Y component
        self.position.y = screen.get_height() - ( ((self.initVelocity*math.sin(math.radians(self.launchAngle)))*time) + (.5)*(self.gravity)*(time)**2 )*5

        # X Component
        self.position.x = ((self.initVelocity*math.cos(math.radians(self.launchAngle)))*time)*5
        pass

physObject = PhysicsObject(50, -10, -10, 10, (255, 255, 255))

dt = 0

initTick = pygame.time.get_ticks()

displaying = True
while displaying:
    # Input and general event handler
    for event in pygame.event.get():
        # If the program is shut down
        if event.type == pygame.QUIT:
            displaying = False

    screen.fill((121, 125, 133))

    if physObject.position.y <= screen.get_height():
        physObject.physicsStep(initTick)

    physObject.draw(screen)

    pygame.display.flip()
    # Delta time between frames
    dt = clock.tick(60) / 1000 # tick locks fps to 60

pygame.quit()

