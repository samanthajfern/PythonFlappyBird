#*******GAME BY SAMANTHA FERNANDEZ******
#Inspired by Megaman, music from YouTube
import pygame
# To use the random function
import random

pygame.init()

#loading images
imageUp = pygame.image.load('megaUP.png')
imageUp = pygame.transform.scale(imageUp, (40,40))

imageDown = pygame.image.load("megaDown.png")
imageDown = pygame.transform.scale(imageDown,(40,40))

imageDead = pygame.image.load('megaDead.png')
imageDead = pygame.transform.scale(imageDead, (40,40))

#loading music
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

#creating colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (192, 0, 255)
white = (255, 255, 255)
skyBlue = (0,191,255)
orange = (255,215,0)
gray = (112,138,144)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird")

done = False

clock = pygame.time.Clock()

x = 350
y = 250

x_speed = 0
y_speed = 0

ground = 458


xloc = 700
yloc = 0
xsize = 70
ysize = random.randint(0, 350)
space = 150
obspeed = 2.5
score = 0

##def obstacles(xloc, yloc, xsize, ysize):
    ##pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    ##pygame.draw.rect(screen, green, [xloc, int(yloc + ysize + space), xsize, ysize + 500])
def obstacles(xloc, yloc, xsize, ysize):
    imgTop = pygame.image.load('pipe.png')
    imgTop = pygame.transform.scale(imgTop, (xsize,ysize))
    imgTop = pygame.transform.rotate(imgTop,180)
    imgTop = pygame.transform.scale(imgTop, (xsize,ysize))
    imgBottom = pygame.image.load('pipe.png')
    imgBottom = pygame.transform.scale(imgBottom, (xsize,ysize))
    imgBottom = pygame.transform.scale(imgBottom, (xsize, 500 - ysize))
    screen.blit(imgTop, (xloc, yloc))
    screen.blit(imgBottom, (xloc, int(yloc + ysize + space)))

    #passing in image of current flappy
def ball(x, y, image):
    ## pygame.draw.circle(screen, black, (x, y), 20)
    ## pygame.draw.circle(screen, red, (x, y), 15)
    screen.blit(image, (x,y)) 

def gameover():
    ####flappy drop
    pygame.mixer.music.stop()
    y_speed = -2
    image = imageDead;
    font = pygame.font.SysFont(None, 50, False, True)
    text = font.render("Game Over!!! ", True, white)
    screen.blit(text, [250, 250])
    if y < 473:
       y_speed = 0


#function to write the score being kept
def Score(score):
    font = pygame.font.SysFont(None, 75)
    #We use str to convert
    text = font.render("Score: "+ str(score), True, white)
    #top left corner coordinates
    screen.blit(text, [0,0])

#global image object
image = imageUp
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #change imageUp
                image = imageUp
                y_speed = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                #change image down
                image = imageDown
                y_speed = 5

    #replace the white sky with skyblue

    #screen.fill(white)
    imageB = pygame.image.load('background.png')
    imageB = pygame.transform.scale(imageB, (700,500))
    screen.fill(skyBlue)
    screen.blit(imageB,(0,0))
    obstacles(xloc, yloc, xsize, ysize)
    ball(x, y, image)

    #If the ball is inbetween two obstacles
    Score(score)

    y += y_speed
    xloc -= obspeed

    if y > ground:
        gameover()
        obspeed = 0
        y = ground
        image = imageDead;
    if y <= 20:   
        y += 40
    #If we hit obstacles in the top block
    if x + 20 > xloc and y - 10 < ysize and x - 15 < xsize + xloc:
        gameover()
        obspeed = 0
        image = imageDead;
    #If we hit obstacles in the bottom block
    if x + 20 > xloc and y + 10 > ysize + space and x - 15 < xsize + xloc:
        gameover()
        obspeed = 0
        image = imageDead;
    #If the obstacle location x is
    if xloc < -70:
        xloc = 700
        ysize = random.randint(0, 350)

    #Check is obstacle was passed adding to score
    if x > xloc and x < xloc + 3:
        score += 1

    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
