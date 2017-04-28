
# Imports
import pygame, math, random, sys
# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 250, 0)
GRASS = (0, 150, 0)
BLUE = (138, 178, 242)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255,255,0)
SUN = (255, 125 , 0)
BURGUNDY = (122, 7, 18)    
SKY = (0, 140, 255)
BROWN = (114, 55, 22)
BOTTOMHOUSE = (170, 135, 82)
GROUND = (249, 192, 120)
TOPHOUSE = (229, 161, 73)
DARKERGROUND = (189, 121, 33)
GRAY = (100, 100, 100)
FACE = (252, 224, 176)
LEAF = (45, 76, 37)
WINDOW = (46, 86, 150)
ROOF = (186, 122, 22)
HOUSE = (160, 129, 80)
LightLightOrange = (254, 160, 129)
LightOrange = (254, 146, 109)
DarkLightOrange = (254, 129, 86)
DarkOrange = (254, 106, 56)
DarkDarkOrange = (254, 97, 44)
SunSetOrange = (254, 85, 29)
DarkSunSetOrange = (254, 68, 5)
DarkDarkSunSetOrange = (235, 60, 1)
NightOrange = (216, 55, 1)
NightDarkOrange = (192, 49, 1)
SunSetSun = (254, 75, 44)
DEATHSTARGRAY = (91, 86, 76)
DUSTYDEWYELLOW = (255, 245, 153)
def draw_cloud(x, y):
    pygame.draw.ellipse(screen, DUSTYDEWYELLOW, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DUSTYDEWYELLOW, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DUSTYDEWYELLOW, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, DUSTYDEWYELLOW, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, DUSTYDEWYELLOW, [x + 20, y + 20, 60, 40])
def obiwan(x, y):
    pygame.draw.ellipse(screen, FACE, [x + 5, y, 10, 10])
    pygame.draw.rect(screen, TOPHOUSE, [x, y + 10, 20, 40])
    pygame.draw.rect(screen, BROWN, [x + 2, y + 10, 5, 40])
    pygame.draw.rect(screen, BROWN, [x + 12, y + 10, 5, 40])
    pygame.draw.rect(screen, BROWN, [x + 2, y + 45, 10, 5])
    pygame.draw.rect(screen, BROWN, [x - 4, y + 50, 9, 6])
    pygame.draw.rect(screen, BROWN, [x + 14, y + 50, 9, 6])
    pygame.draw.rect(screen, BROWN, [x - 5, y + 10, 5, 20])
    pygame.draw.rect(screen, BROWN, [x + 20, y + 10, 5, 20])
    

def draw_deathstar(x, y):
    pygame.draw.ellipse(screen, DEATHSTARGRAY, [x,y, 30, 30])
    pygame.draw.ellipse(screen, GRAY, [x + 6, y + 4, 10, 10])
def draw_jawa(x,y):
    pygame.draw.ellipse(screen, BROWN, [x,y, 10, 10])
    pygame.draw.rect(screen, BROWN, [x, y + 5, 10, 20])
    #Left Side
    pygame.draw.ellipse(screen, BROWN, [x - 5,y + 5, 10, 10])
    pygame.draw.ellipse(screen, BROWN, [x - 5,y + 10, 10, 10])
    pygame.draw.ellipse(screen, BROWN, [x - 5,y + 15, 10, 10])   
    #Right side 
    pygame.draw.ellipse(screen, BROWN, [x + 5,y + 10, 10, 10])
    pygame.draw.ellipse(screen, BROWN, [x + 5,y + 5, 10, 10])
    pygame.draw.ellipse(screen, BROWN, [x + 5,y + 15, 10, 10])
    #Face
    pygame.draw.ellipse(screen, BLACK, [x,y, 10, 10])
    pygame.draw.ellipse(screen, YELLOW, [x + 3,y + 3, 1, 2])
    pygame.draw.ellipse(screen, YELLOW, [x + 5,y + 3, 1, 2])



clouds = []
for i in range(20):
    x = random.randrange(-100, 2600)
    y = random.randrange(0,200)
    clouds.append([x, y])

obiwan_x = 300
obiwan_y = 300

def moveobiwan(pressed):
    global obiwan_x, obiwan_y
    
    if pressed[pygame.K_UP]:
        obiwan_y -= 5
    elif pressed[pygame.K_DOWN]:
        obiwan_y += 5
    if pressed[pygame.K_LEFT]:
        obiwan_x -= 5
    elif pressed[pygame.K_RIGHT]:
        obiwan_x += 5
    




# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    pressed = pygame.key.get_pressed()

    moveobiwan(pressed)  

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    for c in clouds:
        c[0] -= .5

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)
         
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(SKY)
    #sunsetsky

    pygame.draw.rect(screen, LightLightOrange, [1, 1, 900, 50])
    pygame.draw.rect(screen, LightOrange, [1, 50, 900, 50])
    pygame.draw.rect(screen, DarkLightOrange, [1, 100, 900, 50])
    pygame.draw.rect(screen, DarkOrange, [1, 150, 900, 50])
    pygame.draw.rect(screen, DarkDarkOrange, [1, 200, 900, 50])
    pygame.draw.rect(screen, SunSetOrange, [1, 250, 900, 50])
    pygame.draw.rect(screen, DarkSunSetOrange, [1, 300, 900, 50])
    pygame.draw.rect(screen, DarkDarkSunSetOrange, [1, 350, 900, 50])
    pygame.draw.rect(screen, NightOrange, [1, 400, 900, 50])
    pygame.draw.rect(screen, NightDarkOrange, [1, 450, 900, 50])
    pygame.draw.ellipse(screen, SunSetSun, [250, 40, 100, 100])
    pygame.draw.ellipse(screen, DARKERGROUND, [-400, 300, 700, 700])
    pygame.draw.ellipse(screen, NightDarkOrange, [400, 40, 50, 50])
    pygame.draw.ellipse(screen, DARKERGROUND, [-100, 450, 700, 700])
    draw_deathstar(100, 200)
    for c in clouds:
        draw_cloud(c[0], c[1])
    
    pygame.draw.ellipse(screen, TOPHOUSE, [435, 375, 200, 200])
    pygame.draw.rect(screen, GROUND, [0, 500, 800, 300])
    pygame.draw.rect(screen, TOPHOUSE, [410, 450, 250, 50])
    pygame.draw.rect(screen, BOTTOMHOUSE, [400, 475, 270, 33])
    pygame.draw.rect(screen, BLACK, [520, 450, 30, 58])    
    draw_jawa(350, 510)
    draw_jawa(400, 510)
    draw_jawa(366, 510)
    obiwan(obiwan_x, obiwan_y)
   
    #moveobiwan

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

