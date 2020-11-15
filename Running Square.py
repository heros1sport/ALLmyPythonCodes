print("""This game made on pygame
         How to use: use arrows to move the square and w to speed up the square          and s to slow the square and a to to set normal speed
         approved of government
         made in India in Dec 21, 2018
         made by Shaurya
     """)
                    
#This game made on pygame
#How to use: use arrows to move the square and w to speed up the square and s to slow the square and a to to set normal speed
#approved of government
#made in India in Dec 21, 2018
#made by Shaurya

#-------------------------------------------------------------------------Start----------------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||                                                                                                                                                                     
#------------------------------------------------------------------------modules---------------------------------------------------------------------------------------

#imports pygame                                                                                                                                                          

import pygame

#------------------------------------------------------------------------initializers----------------------------------------------------------------------------------
#initializes pygame

pygame.init()

#initializes pygame window

screen = pygame.display.set_mode((1000,1000))

#sets the project title to Running square

Title = pygame.display.set_caption('Running square')

#------------------------------------------------------------------------variables-------------------------------------------------------------------------------------

#sets font

my_font = pygame.font.SysFont("italic", 20)

#sets variable color to blue

color = (0, 0, 255)

#sets variable switch to False

switch = False

#sets variable clock to time

clock = pygame.time.Clock()

#sets variable y to 100

y = 100

#sets variable x to 100

x = 100

#sets normal_speed to 60

normal_speed = 60

#sets slow_speed to 10

slow_speed = 10

#sets fast speed to 300

fast_speed = 300000

#sets speed 60

speed = 60

#------------------------------------------------------------------------main program----------------------------------------------------------------------------------

while not switch:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            done = True
            
    keyPressed = pygame.key.get_pressed()
    
    screen.fill((0, 0, 0))
    
    if keyPressed[pygame.K_UP]:
        
        y -= 1
        
    if keyPressed[pygame.K_DOWN]:
        
        y += 1
        
    if keyPressed[pygame.K_LEFT]:
        
        x -= 1
        
    if keyPressed[pygame.K_RIGHT]:
        
         x += 1
        
    if keyPressed[pygame.K_w]:
        
        speed = fast_speed
        
    if keyPressed[pygame.K_s]:
        
        speed = slow_speed
        
    if keyPressed[pygame.K_a]:
        
        speed = normal_speed
        
    coordinates = my_font.render("(x + y) = ( " + str(x) + " , " + str(y) + " )", 20, (0, 255, 0))
    
#------------------------------------------------------------------------Executors-------------------------------------------------------------------------------------

#prints coordinates on the pygame window

    screen.blit(coordinates, (1, 1))
    
#draws a rectangle

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 100, 100))
    
#frames another display

    pygame.display.update()
    
#sets speed of the square

    clock.tick(speed)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#--------------------------------------------------------------------------End-----------------------------------------------------------------------------------------
