import time
import pygame
pygame.init()
screen = pygame.display.set_mode((600,500)) # sets screen dimensions to 600 by 500
x = 275
y = 475
i = 40
i2 = 20
i3 = 0
i4 = 20
X_a = 20
Y_a = 475
font = pygame.font.SysFont("Copperplate",20) # font initialized
done = 0
while done != 1:
    for event in pygame.event.get():
        keyPressed = pygame.key.get_pressed() # sets the variable to the key which is pressed
        if event.type >= 2 and event.type <=5 or event.type == 12 or event.type == 17: # if any motion is done on the window then....
            i4 = 28 # sets the jump height
    i = i4
    while i != 0:
        pygame.draw.circle(screen,(0,0,255),(x,Y_a),25,0)
        Y_a -= i # subtract the Y-velocity
        coordinates = font.render("Co-ordinates = " + "(x + y)" + " = " + "(" + str(x) + " + " + str(Y_a) + ")", 15 , (0,255,0))
        screen.blit(coordinates,(1, 1)) # show coordinates in of the variable coordinates
        pygame.display.update() # update to the screen visible to user
        screen.fill((255,255,255)) # refresh screen
        time.sleep(0.03)# Wait 30 milliseconds (frames per second)
        i -= 1
    i2 = 0
    while i2 != (i4+1):
        pygame.draw.circle(screen,(0,0,255),(x,Y_a),25,0)
        Y_a += i2
        coordinates = font.render("Co-ordinates = " + "(x + y)" + " = " + "(" + str(x) + " + " + str(Y_a) + ")", 15 , (0,255,0))
        screen.blit(coordinates,(1, 1)) # show coordinates in of the variable coordinates
        pygame.display.update() # update to the screen visible to user
        screen.fill((255,255,255)) # refresh screen
        time.sleep(0.03)# Wait 30 milliseconds (frames per second)
        i2 += 1
    if i4 > 0:
        i4 -= 2
    
quit()

    
