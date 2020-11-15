import math
import time
import pygame
pygame.init()
scr = pygame.display.set_mode((1300,650))
turn = 1
startx = -1
starty = -1
destx = -1
desty = -1
obs = []
path = []
wee = [0,0]
def distance(x,y):
    xw = math.fabs(x)
    yh = math.fabs(y)
    return math.hypot(xw,yh)
while True:
    scr.fill((0,0,0))
    for event in pygame.event.get():
        Mpos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()
        if key[pygame.K_k]:
            turn += 1
        if turn == 1:
            for i in range(1,1300,10):
                for j in range(1,650,10): 
                    if Mpos[0] > i and Mpos[0] < i+10 and Mpos[1] > j and Mpos[1] < j+10:
                        pygame.draw.rect(scr,(255,255,255),pygame.Rect(i,j,10,10),2)
                        for event in pygame.event.get():
                            Mpos = pygame.mouse.get_pos()
                        if event.type == 5:
                            obs.append([i,j])
    for i in range(1,1300,10):
        for j in range(1,650,10): 
            pygame.draw.rect(scr,(255,255,255),pygame.Rect(i,j,10,10),1)
    if turn == 3:
        for i in range(1,1300,10):
            for j in range(1,650,10): 
                if Mpos[0] > i and Mpos[0] < i+10 and Mpos[1] > j and Mpos[1] < j+10:
                    pygame.draw.rect(scr,(255,0,0),pygame.Rect(i,j,10,10),2)
                    for event in pygame.event.get():
                        Mpos = pygame.mouse.get_pos()
                        key = pygame.key.get_pressed()
                    if event.type == 5:
                        turn += 1
                        startx = i
                        starty = j
                        time.sleep(2)
    if turn == 2:
        for i in range(1,1300,10):
            for j in range(1,650,10): 
                if Mpos[0] > i and Mpos[0] < i+10 and Mpos[1] > j and Mpos[1] < j+10:
                    pygame.draw.rect(scr,(0,255,0),pygame.Rect(i,j,10,10),2)
                    for event in pygame.event.get():
                        Mpos = pygame.mouse.get_pos()
                        key = pygame.key.get_pressed()
                    if event.type == 5:
                        turn += 1
                        destx = i
                        desty = j
                        time.sleep(1)
    if startx != -1:
        pygame.draw.rect(scr,(255,0,0),pygame.Rect(startx,starty,10,10))
    if destx != -1:
        pygame.draw.rect(scr,(0,255,0),pygame.Rect(destx,desty,10,10))
    
    for i in obs:
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(i[0],i[1],10,10))
    path = [[startx,starty]]
    while startx != -1 and destx != -1 and path[-1] != [destx,desty]:
        best_distance = distance(destx-path[-1][0],desty-path[-1][1])
        if distance(destx-(path[-1][0]+10),desty-path[-1][1]) < best_distance:
            valid = True
            for j in range(len(obs)):
                if [obs[j][0],obs[j][1]] == [path[-1][0] + 10,path[-1][1]]:
                    valid = False
            if valid:
                best_distance = distance(destx-(path[-1][0]+10),desty-path[-1][1])
                wee = [10,0]
        print(valid)
        if distance(destx-(path[-1][0]),desty-(path[-1][1]+10)) < best_distance:
            valid = True
            for j in range(len(obs)):
                if [obs[j][0],obs[j][1]] == [path[-1][0],path[-1][1] + 10]:
                    valid = False
            if valid:
                best_distance = distance(destx-(path[-1][0]),desty-(path[-1][1]+10))
                wee = [0,10]
        print(valid)
        if distance(destx-(path[-1][0]),desty-(path[-1][1]-10)) < best_distance:
            valid = True
            for j in range(len(obs)):
                if [obs[j][0],obs[j][1]] == [path[-1][0],path[-1][1] - 10]:
                    valid = False
            if valid:
                best_distance = distance(destx-(path[-1][0]),desty-(path[-1][1]-10))
                wee = [0,-10]

        print(valid)
        if distance(destx-(path[-1][0] - 10),desty-(path[-1][1])) < best_distance:
            valid = True
            for j in range(len(obs)):
                if [obs[j][0],obs[j][1]] == [path[-1][0] - 10,path[-1][1]]:
                    valid = False
            if valid:
                best_distance = distance(destx-(path[-1][0]-10),desty-(path[-1][1]))
                wee = [-10,0]
        print(valid)
        path.append([path[-1][0] + wee[0],path[-1][1] + wee[1]])
        for i in path:
            pygame.draw.rect(scr,(255,0,0),pygame.Rect(i[0],i[1],10,10))
        pygame.display.update()
    for i in path:
        pygame.draw.rect(scr,(255,0,0),pygame.Rect(i[0],i[1],10,10))
    pygame.display.update()
