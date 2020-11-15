import random
import pygame
import time
pygame.init()
scr = pygame.display.set_mode((1400,700))
blocks = []
level = 3
GrassBlock = pygame.image.load('Grass Block.png')
DirtBlock = pygame.image.load('Dirt Block.png')]
WoodBlock = pygame.image.load('Wood Block.png')
Leaves = pygame.image.load('Leaves.png')
Y = 100
Sprite = (pygame.image.load('Left-Standing Sprite.png'),pygame.image.load('Right-Standing Sprite.png'))
Direction = 'Right'
Jump = 0
for i in range(0,1400,50):
    for j in range(level):
        if j == level-1:
            blocks.append([i,700 - (j*50),'Grass Block'])
        else:
            blocks.append([i,700 - (j*50),'Dirt Block'])]]]]]
    if random.randint(1,10) == random.randint(1,10):
        blocks.append([i,700 - ((level) * 50),'Wood Block'])
        blocks.append([i,700 - ((level+1) * 50),'Wood Block'])
        blocks.append([i,700 - ((level+2) * 50),'Wood Block'])

        blocks.append([i,700 - (((level-1)+4) * 50),'Leaves'])
        blocks.append([i+50,700 - (((level-1)+4) * 50),'Leaves'])
        blocks.append([i-50,700 - (((level-1)+4) * 50),'Leaves'])
        
        blocks.append([i,700 - (((level-1)+5) * 50),'Leaves'])
        blocks.append([i+50,700 - (((level-1)+5) * 50),'Leaves'])
        blocks.append([i-50,700 - (((level-1)+5) * 50),'Leaves'])
        
        blocks.append([i,700 - (((level-1)+6) * 50),'Leaves'])
        blocks.append([i+50,700 - (((level-1)+6) * 50),'Leaves'])
        blocks.append([i-50,700 - (((level-1)+6) * 50),'Leaves'])
    if random.randint(1,4) == 3 and level < 5:
        level += 1
    if random.randint(1,4) == 1 and level > 2:
        level -= 1
while True:
    pygame.draw.rect(scr,(153,217,234),pygame.Rect(0,0,1400,700))
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            for i in range(len(blocks)):
                blocks[i][0] -= 50
            if blocks[-1][0] < 1350:
                for j in range(level):
                    if j == level-1:
                        blocks.append([1350,700 - (j*50),'Grass Block'])
                    else:
                        blocks.append([1350,700 - (j*50),'Dirt Block'])
                if random.randint(1,10) == random.randint(1,10):
                    blocks.append([1350,700 - (((level-1)+1) * 50),'Wood Block'])
                    blocks.append([1350,700 - (((level-1)+2) * 50),'Wood Block'])
                    blocks.append([1350,700 - (((level-1)+3) * 50),'Wood Block'])
                    blocks.append([1350,700 - (((level-1)+4) * 50),'Leaves'])
                    blocks.append([1400,700 - (((level-1)+4) * 50),'Leaves'])
                    blocks.append([1300,700 - (((level-1)+4) * 50),'Leaves'])
                    
                    blocks.append([1350,700 - (((level-1)+5) * 50),'Leaves'])
                    blocks.append([1400,700 - (((level-1)+5) * 50),'Leaves'])
                    blocks.append([1300,700 - (((level-1)+5) * 50),'Leaves'])
                    
                    blocks.append([1350,700 - (((level-1)+6) * 50),'Leaves'])
                    blocks.append([1400,700 - (((level-1)+6) * 50),'Leaves'])
                    blocks.append([1300,700 - (((level-1)+6) * 50),'Leaves'])
                if random.randint(1,4) == 3 and level < 5:
                    level += 1
                if random.randint(1,4) == 1 and level > 2:
                    level -= 1
                
        if key[pygame.K_LEFT]:
            for i in range(len(blocks)):
                blocks[i][0] += 50
            if blocks[0][0] > 0:
                for j in range(level):
                    if j == level-1:
                        blocks.append([0,700 - (j*50),'Grass Block'])
                    else:
                        blocks.append([0,700 - (j*50),'Dirt Block'])
                if random.randint(1,15) == random.randint(1,15):
                    blocks.append([0,700 - (((level-1)+1) * 50),'Wood Block'])
                    blocks.append([0,700 - (((level-1)+2) * 50),'Wood Block'])
                    blocks.append([0,700 - (((level-1)+3) * 50),'Wood Block'])

                    blocks.append([0,700 - (((level-1)+4) * 50),'Leaves'])
                    blocks.append([50,700 - (((level-1)+4) * 50),'Leaves'])
                    blocks.append([-50,700 - (((level-1)+4) * 50),'Leaves'])
                    
                    blocks.append([0,700 - (((level-1)+5) * 50),'Leaves'])
                    blocks.append([50,700 - (((level-1)+5) * 50),'Leaves'])
                    blocks.append([-50,700 - (((level-1)+5) * 50),'Leaves'])
                    
                    blocks.append([0,700 - (((level-1)+6) * 50),'Leaves'])
                    blocks.append([50,700 - (((level-1)+6) * 50),'Leaves'])
                    blocks.append([-50,700 - (((level-1)+6) * 50),'Leaves'])
                if random.randint(1,4) == 3 and level < 5:
                    level += 1
                if random.randint(1,4) == 1 and level > 2:
                    level -= 1
        if key[pygame.K_UP]:
            Jump = 30
    highest_block = 700
    for i in blocks:
        if i[0]+50 > 675 and i[0] < 675:
            if highest_block > i[1]:
                highest_block = i[1]

    Y -= Jump
    if Jump > 1:
        Jump -= 5 
    if 700 - (Y+100) > 700 - highest_block:
        Y += j
        j += 5
        if 700 - (Y+100) < 700 - highest_block and 700 - (Y+100) > (700 - highest_block) - 50:
            Y = highest_block-100
            
    else:
        j = 0
        
    for i in blocks:
        if i[0] < 1350 or i[0] > 0:
            if i[2] == 'Grass Block':
                scr.blit(GrassBlock,(i[0],i[1]))
            if i[2] == 'Dirt Block':
                scr.blit(DirtBlock,(i[0],i[1]))
            if i[2] == 'Wood Block':
                scr.blit(WoodBlock,(i[0],i[1]))
            if i[2] == 'Leaves':
                scr.blit(Leaves,(i[0],i[1]))
            if Direction == 'Right':
                scr.blit(Sprite[1],(1350/2,Y))
            if Direction == 'Left':
                scr.blit(Sprite[0],(1350/2,Y))
    time.sleep(0.003)
    pygame.display.update()
