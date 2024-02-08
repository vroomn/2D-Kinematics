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

#Drawing objects
ball = pygame.draw.circle (screen, pygame.Color(255, 0, 0, 255), (60, 110), 20 )
 

#variables
gravity = 1.0


#circle class 
class Ball:
    def __init__(self,acceleration, angle, x_initialvel, y_initialvel, x_finalvel, y_finalvel, y_position, x_position):
        self.accel = acceleration
        self.angle = angle
        self.initial_x = x_initialvel
        self.initial_y = y_initialvel
        self.x_final = x_finalvel
        self.y_final = y_finalvel
        self.y_pos = y_position
        self.x_pos = x_position

#drawing the circle
        def draw_circle(self):
            pygame.draw.circle (screen, pygame.Color(255, 0, 0, 255), (60, 110), 20 )
            
#gravity function
#def if_falling ():
    
    


angle_check = False

while not angle_check: 
    def less_than():
        angle = int(input("Please enter the angle you want the ball to be fired at:")) 
        if angle > 90:
            return False
        else: 
            True
    
    
    pygame.quit()

