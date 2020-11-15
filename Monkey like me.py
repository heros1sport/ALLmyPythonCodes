import random
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((700,600))
inj = pygame.image.load('injection.jpg')
inj = pygame.transform.smoothscale(inj,(50,50))
inj = pygame.transform.rotate(inj,270)
posx = pygame.mouse.get_pos()
monkey = pygame.image.load('monkey.jpg')
monkey = pygame.transform.smoothscale(monkey,(100,100))
x = random.randint(1,600)
x2 = 0
y = 200
posy = 550
i = 0
boolean = True
while True:
    screen.blit(monkey,(x,y)) 
    screen.blit(inj,(posx[0],posy)) 
    pygame.display.update()
    for event in pygame.event.get():
        posx = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1,0,0):
            i = 0
            x2=posx[0]
            while i != 600:
                screen.blit(inj,(x2,posy))
                screen.blit(monkey,(x,200)) 
                posy -= 1
                pygame.display.update()
                screen.fill((255,255,255))
                i +=1
                if x <= posx[0] and (x+100) >= posx[0] and posy > y and posy < (y+100):
                    x = random.randint(1,700)
                    time.sleep(0.5)
                    i = 600
            posy = 550
    screen.fill((255,255,255))
    
        
    
        
