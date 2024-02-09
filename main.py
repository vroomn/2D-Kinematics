import pygame
import ui_system

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

#valid_grav = False
#gravity = 0
#while not valid_grav:
 #   gravity = abs(int(input("Enter a valid integer for the value of the gravitational pull:")))
  #  print (gravity)
   # if gravity < 0:
    #    valid_grav = True

#valid_speed = False
#initial_speed = 0
#while not valid_speed:
 #   initial_speed = abs(int(input("Enter a valid integer for the value of the object's speed:")))
  #  if initial_speed >= 1:
   #     valid_speed = True

pygame.quit()
