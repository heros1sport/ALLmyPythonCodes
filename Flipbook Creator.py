import time
import pygame
pygame.init()
scr = pygame.display.set_mode((600,500))
mem = [[]]
lastpos = [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]
i = 0
j = -1
while True:
    if j >= 1:
        for h in range(len(mem) - 1):
            for g in range(len(mem[h])):
                for k in range(len(mem[h][g])-1):
                    pygame.draw.line(scr,(100,100,100),(mem[h][g][k][0],mem[h][g][k][1]),(mem[h][g][k+1][0],mem[h][g][k+1][1]),5)
            pygame.display.update()
    for event in pygame.event.get():
        K = pygame.key.get_pressed()
        Mpos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1,0,0):
        lastpos = Mpos
        j += 1
        print(i)
        mem[i].append([])
        
        while pygame.mouse.get_pressed() != (0,0,0):
            for event in pygame.event.get():
                pass
            Mpos = pygame.mouse.get_pos()
            pygame.draw.line(scr,(255,255,255),(lastpos[0],lastpos[1]),(Mpos[0],Mpos[1]),5)
            pygame.display.update()
            lastpos = Mpos
            mem[i][j].append(lastpos)
    if K[pygame.K_s]:
        print(mem)
        mem.append([])
        i += 1
        j = -1
        time.sleep(1)
    if K[pygame.K_r]:
        for j in range(len(mem)):
            scr.fill((0,0,0))
            for g in range(len(mem[j])):
                for i in range(len(mem[j][g])-1):
                    pygame.draw.line(scr,(255,255,255),(mem[j][g][i][0],mem[j][g][i][1]),(mem[j][g][i+1][0],mem[j][g][i+1][1]),5)
            pygame.display.update()
            time.sleep(0.03)
    
    
    
    
