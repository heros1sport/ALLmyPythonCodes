from Fusion import *
import time
import pygame
pygame.init()
scr = pygame.display.set_mode((600,600))

font = pygame.font.SysFont('Agency FB',300)
a = 0
secs = 0
min2 = 0
sec1 = 0
min1 = 0
while True:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        a = 1
        sec1 = int(Fusion.getTimeSec())
        min1 = int(Fusion.getTimeMinutes())
        while a == 1:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    a = 0
                    time.sleep(1)
            if a == 0:
                continue
            scr.fill((0,0,0))
            secs = int(Fusion.getTimeSec())
            min2 = int(Fusion.getTimeMinutes())
            font = pygame.font.SysFont('Agency FB',20)
            text = font.render("Seconds",20,(0,255,255))
            font = pygame.font.SysFont('Agency FB',300)
            text1 = font.render(str((secs + (min2 * 60)) - (sec1 + (min1 * 60))),300,(0,255,255))
            scr.blit(text, (260,500))
            scr.blit(text1, (225,0))
            pygame.display.update()
    scr.fill((0,0,0))
    font = pygame.font.SysFont('Agency FB',20)
    text = font.render("Seconds",20,(0,255,255))
    font = pygame.font.SysFont('Agency FB',300)
    text1 = font.render(str((secs + (min2 * 60)) - (sec1 + (min1 * 60))),300,(0,255,255))
    scr.blit(text, (260,500))
    scr.blit(text1, (225,0))
    pygame.display.update()
        

    
