import pygame
from math import pi

#Initialize the game engine
pygame.init()

#Define some colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = (255, 0, 0)
 
#Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

#Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

while not done:
    #This limits the while loop to a max of 10 times per second.
    #Leave this out and we will use all CPU we can
    clock.tick(10)

    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked close
            done = True # Flag that we are done so we exit this loop

#All drawing code happens after the for loop and but
#inside the main while done == false loop

#Clear the screen and set the screen background
    screen.fill(WHITE)

    #line(Surface, color, start_pos, end_pos, width=1) -> Rect
    #Draw a straight line segment on a Surface. There are no endcaps,
    #The ends are squared off for thick lines

    #Draw on the screen a green line from (0,0) to (50,30)
    #5 pixels wide
    pygame.draw.line(screen, GREEN, [0,0], [50,30], 5) 


    #Go ahead and update the screen with what we've drawn
    #This must happen after all the other drawing commands
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()