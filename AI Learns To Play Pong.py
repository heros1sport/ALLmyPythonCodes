import winsound
import time
import numpy
import math
import random
import pygame
pygame.init()
scr = pygame.display.set_mode((600,600))
numpy.random.seed(123)
pongx = 100
pongy = 100
pongangle = random.randint(0,180)

OY = 100

weights = []

for i in range(50):
    weights.append([2 * numpy.random.randn() - 1,2 * numpy.random.randn() - 1,0])
def sigmoid(x):
    return 1 / (1 - numpy.exp(-x))
AiX = 100
for i in range(1500):
    fitness = 0
    pongx = 100
    pongy = 100
    pongangle = 254
    AiX = 100
    pongangle = 44
    for j in range(50):
        fitness = 0
        pongx = 100
        pongy = 100
        AiX = 100
        
        while True:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
            scr.fill((0,0,0))
            pongx = pongx + 3 * math.cos(math.radians(pongangle))
            pongy = pongy + 3 * math.sin(math.radians(pongangle))
            AiX += (0.5 - sigmoid((AiX-pongy) * weights[j][0] + AiX * weights[j][1])) * 4
            if AiX < 0:
                while AiX < 0:
                    AiX += 1
            if AiX+50 > 600:
                while AiX+50 > 600:
                    AiX -= 1
            if pongx > 590 and pongy >= AiX and pongy <= AiX+50:
                pongangle += pongangle + pongangle
                fitness += 600
                while pongx > 590 and pongy >= AiX and pongy <= AiX+50:
                    pongx = pongx + 3 * math.cos(math.radians(pongangle))
                    pongy = pongy + 3 * math.sin(math.radians(pongangle))
            if pongx > 600:
                fitness += math.fabs(600 - math.fabs((AiX+27) - pongy))
                weights[j][2] = fitness
                break
            if pongx <= 10:
                pongangle += pongangle + pongangle
            if pongy < 0:
                pongangle -= pongangle + pongangle
            if pongy > 600:
                pongangle -= pongangle + pongangle
            if pongangle > 360:
                while pongangle > 360:
                    pongangle -= 360
            if pongangle < -360:
                while pongangle < -360:
                    pongangle += 360    
            OY = pongy
            pygame.draw.rect(scr,(255,255,255),pygame.Rect(pongx,pongy,10,10))
            pygame.draw.rect(scr,(255,255,255),pygame.Rect(0,OY,10,50))
            pygame.draw.rect(scr,(255,255,255),pygame.Rect(590,AiX,10,50))
            pygame.display.update()
            if key[pygame.K_k]:
                time.sleep(0.015)
        
        print("Number : " + str(j) + ", " + "Creature Fitness Score : " + str(fitness))
    print("\nNEXT GENERATION\n")
    best_fitness = 0
    best_Ai = None
    for k in weights:
        if best_fitness < k[2]:
            best_fitness = k[2]
            best_Ai = k
    for g in range(50):
        if random.randint(1,3) > 2:
            creature = [2 * numpy.random.randn() - 1,2 * numpy.random.randn() - 1,0]
            weights[g] = creature
        else:
            creature = best_Ai
            weights[g] = creature
            
