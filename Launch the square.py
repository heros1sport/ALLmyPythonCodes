import math
import pygame
import time
pygame.init()
scr = pygame.display.set_mode((800,600))
y = 300
power = int(input('power = '))
height = 600 - int(input('height = '))
l = []
while True:
    for x in range(-25,25,1):
        for event in pygame.event.get():
            pass
        y = (x**2+0.5*x + height)
        x *= power
        scr.fill((0,0,0))
        pygame.draw.rect(scr,(255,0,0),pygame.Rect(x + 300,y,20,20))
        pygame.display.update()
        time.sleep(0.03)
        
