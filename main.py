import pygame

# Width of the simulator window
WIDTH = 1280
# Height of the simulator window
HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

displaying = True
while displaying:
    # Input and general event handler
    for event in pygame.event.get():
        # If the program is shut down
        if event.type == pygame.QUIT:
            displaying = False

    screen.fill((121, 125, 133))

    pygame.display.flip()
    # Delta time between frames
    dt = clock.tick(60) / 1000 # tick locks fps to 60

pygame.quit()
