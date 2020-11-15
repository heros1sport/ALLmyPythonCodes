import time
import math
import pygame
pygame.init()
scr = pygame.display.set_mode((600,500))
angle = -90
angle2 = -90
x2 = 100
y2 = 100
a = 0
b = 0
c = 0
while True:
    for event in pygame.event.get():
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        x2 = pygame.mouse.get_pos()[0]
        y2 = pygame.mouse.get_pos()[1]
        if event.type == 5:
            angle = -90
            angle2 = -90
            a = 0
            b = 0
            c = 0
            while True:
                scr.fill((0,0,0))
                pygame.draw.rect(scr,(0,255,255),pygame.Rect(x,y,50,50))
                pygame.draw.rect(scr,(0,255,255),pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],50,50))
                for event in pygame.event.get():
                    if event.type == 5:
                        angle2 = -90
                        a += 1
                if a == 1:
                    pygame.draw.rect(scr,(0,255,255),pygame.Rect(x2,y2,50,50))
                    x2 = x2 + 4 * math.cos(math.radians(angle2))
                    y2 = y2 + 1 * math.sin(math.radians(angle2))
                    if angle2 != 270:
                        angle2 += 1
                pygame.display.update()
                if angle != 270:
                    angle += 1
                    x = x + 4 * math.cos(math.radians(angle))
                    y = y + 1 * math.sin(math.radians(angle))
                else:
                    c = 1
                time.sleep(0.003)
                if angle2 == 270:
                    
                    break
    scr.fill((0,0,0))
    pygame.draw.rect(scr,(0,255,255),pygame.Rect(x,y,50,50))
    pygame.display.update()
