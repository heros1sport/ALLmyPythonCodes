import math
import time
import pygame
pygame.init()
scr = pygame.display.set_mode((600,500))
y1 = 200
x1 = 200
h1 = 100
w1 = 100
y2 = 300
x2 = 300
h2 = 100
w2 = 100
angle1 = 0
angle2 = 0
while True:
    scr.fill((0,0,0))
    for event in pygame.event.get():
        keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_LEFT]:
        angle1 += 1
        angle2 += 1
        x1 -= 1
        x2 += 1
    if keyPressed[pygame.K_RIGHT]:
        x1 += 1
        x2 -= 1
        if x1 > x2:
            w1 -= 1
            w2 -=1
    if keyPressed[pygame.K_DOWN]:
        y1 -= 1
        y2 += 1

    if keyPressed[pygame.K_UP]:
        y1 += 1
        y2 -= 1
    time.sleep(0.03)
    pygame.draw.rect(scr,(255,255,255),pygame.Rect(x1,y1,w1,h1),5)
    pygame.draw.rect(scr,(255,255,255),pygame.Rect(x2,y2,w2,h2),5)
    pygame.draw.line(scr,(255,255,255),(x1,y1),(x2,y2),5)
    pygame.draw.line(scr,(255,255,255),(x1+w1,y1+h1),(x2+w2,y2+h2),5)
    pygame.draw.line(scr,(255,255,255),(x1+w1,y1),(x2+w2,y2),5)
    pygame.draw.line(scr,(255,255,255),(x1,y1+h1),(x2,y2+h2),5)
    pygame.display.update()
    

