import pygame
import time
pygame.init()
scr = pygame.display.set_mode((200,200))
font = pygame.font.SysFont('Agency FB', 23)
while True:
    scr.fill((0,0,0))
    pygame.draw.circle(scr, (0,0,255), (100,100), 100)
    scr.blit(font.render(str(time.ctime()), 1, (0, 255, 255)), (10 , 85))
    pygame.display.update()
        
                      
                       
    
