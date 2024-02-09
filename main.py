import pygame
import pygame.gfxdraw

from physics import PhysicsObject
from ui_system import UI

# Width of the simulator window
WIDTH = 1280
# Height of the simulator window
HEIGHT = 720

# Pygame initalization and setup of the screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

initVelocity = UI.getAbsIntInput("What is the inital velocity")
launchAngle = UI.getAbsIntInput("What is the launch angle (degrees)")
gravity = UI.getAbsIntInput("What is the gravity (as a scalar)")
print("Simulating...")

physObject = PhysicsObject(initVelocity, launchAngle, -(gravity), 10, (255, 255, 255))

# First tick of the distance sim
initTick = pygame.time.get_ticks()

displaying = True
# Primary Render Loop
while displaying:
    # Input and general event handler
    for event in pygame.event.get():
        # If the program is shut down
        if event.type == pygame.QUIT:
            displaying = False

    # Set the background color
    screen.fill((121, 125, 133))

    # Only step physics when not on ground
    if physObject.position.y <= screen.get_height():
        physObject.physicsStep(initTick, screen)
    
    physObject.draw(screen)

    # Switch the framebuffer
    pygame.display.flip()
    # Delta time between frames
    dt = clock.tick(60) / 1000 # tick locks fps to 60

pygame.quit()

