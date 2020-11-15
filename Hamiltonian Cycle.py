import pygame
import time
import random
pygame.init()
scr = pygame.display.set_mode((620,620))
grid = []
for i in range(0,601,50):
    for j in range(0,601,50):
        grid.append([i,j])
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(i,j,10,10))
pygame.display.update()
grid2 = grid
grid3 = []
for i in grid2:
    if i[0] >= 50 and i[1] >= 50 and i[0] <= 550 and i[1] <= 550 :
        grid3.append(i)
for i in grid3:
    pygame.draw.rect(scr,(255,0,0),pygame.Rect(i[0],i[1],10,10))
lines = []
for i in grid3:
    lines.append([i[0],i[1],i[0],i[1]-50])
    lines.append([i[0],i[1],i[0]+50,i[1]])
    lines.append([i[0],i[1],i[0],i[1]+50])
    lines.append([i[0],i[1],i[0]-50,i[1]])
lines2 = []
for i in range(len(lines)):
    g = True
    for j in lines[i]:
        if j >= 50 and j <= 550:
            pass
        else:
            g = False
    if g == True:
        lines2.append(lines[i])
for i in lines2:
    pygame.draw.line(scr,(255,0,0),(i[0],i[1]),(i[2],i[3]),3)


pygame.display.update()


input()

    