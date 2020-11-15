

#                               WE NEED THESE THINGS TO PERFECTLY PICK AN AI OUT OF MILLIONS OF OTHER CREATURES ( and torture the worst )


import numpy
import random
import math
import pygame
pygame.init()
scr = pygame.display.set_mode((700,30))
font = pygame.font.SysFont('Agency FB',20)
numpy.random.seed(random.randint(1,98))
flowers = [[2.5,4,0],
           [5,3,1],
           [3.5,5,0],
           [2.5,5.5,0],
           [4,3,1],
           [4.5,4,1]]
print("These are the values that computer will train on : \n")
print("The black window shows by how much the computer's probablity wasn't correct.\nComputer right now is training hard and watching videos\non how to compare numbers and repeatedly taking test and stuff")

for i in flowers:
    if i[2] == 0:
        print(str(i[0]) + ' < ' + str(i[1]))
    if i[2] == 1:
        print(str(i[0]) + ' > ' + str(i[1]))
weights = []
def sigmoid(x):
    return 1 / (1 - numpy.exp(-x))
for i in range(50):
    weights.append([])
    weights[i] += [2 * numpy.random.randn() - 1,2 * numpy.random.randn() - 1]
    average_fitness = 0
    fitness = []
    for k in flowers:
        fitness.append(k[2] - sigmoid((k[0] * weights[i][0] + k[1] * weights[i][1])))
    average_fitness = sum(fitness) / 6
    weights[i].append(average_fitness)


#                                   Creating THE PERFECT AI by SLAUGHTERING MILLIONS OF INOCCENT CREATURES AND..I mean training.


history = []
history += weights
error_history = []
for f in range(5000):
    numpy.random.seed(random.randint(1,98))
    # Get the best creature and tell him to sit in a corner.
    for event in pygame.event.get():
        pass
    best_fitness = 1000
    best_weight = 0
    fitness = []
    for j in range(len(weights)):
        if weights[j][2] < best_fitness:
            best_fitness = weights[j][2]
            best_weight = weights[j]
    # Create a new generation where 30% of creatures have random weights ( and the other 70% will be replicates of the BEST GUY WITH A CHANCE OF HAVING GOOD VALUES)
    for i in range(50):
        if random.randint(1,3) == 2:
            weights[i] = [2 * numpy.random.randn() - 1,2 * numpy.random.randn() - 1,0]
            
        else:        
            weights[i] = best_weight
    for i in range(50):
        average_fitness = 0
        fitness = []
        for k in flowers:
            fitness.append(math.fabs(k[2] - sigmoid((k[0] * weights[i][0] + k[1] * weights[i][1]))))
        average_fitness = sum(fitness) / 6
        weights[i][2] = average_fitness
    # Just record AI error progression
    if f % 100 == 0:
        error_history.append(best_fitness)
    history += [weights]
    # Gettin' some o' that sweet sweet mistake value
    scr.fill((0,0,0))
    py = 680
    px = 0
    y = 680
    x = 0
    pos1 = 60
    scr.blit(font.render("Average Error Of Main Generation : " + str(best_fitness),15,(0,255,0)),(0,0))
    for i in error_history:
        y = 680 - (math.fabs(1 - i) * 10)
        x += 700 / len(error_history)
        pygame.draw.line(scr,(0,0,0),(px,py),(x,y),5)
        py = y
        px = x
    pygame.display.update()
    

#                                                               ALRIGHT!!! TIME TO FRIGGIN' TEST THIS OUT!!!
print("\n\n IIT GENIUS TEST QUESTIONS : ")
#  Quiz for absolute IQ 999 people
quiz = [[3.3,5],
        [1.2,3],
        [3,1.1],
        [4,2],
        [3,3.4],
        [5.5,4.5],
        [2.1,4.3],
        [56.3,57.3]]
# solve the quiz, AI, SHOW US WHATCHA GOT BUDDY, TIME TO USE THOSE SICK WEIGHTS YOU'VE BEEN CARRYIN' AROUND
for i in quiz:
    ans = sigmoid((i[0] * best_weight[0] + i[1] * best_weight[1]))
    if ans < 0.5:
        bias = ' < '
    if ans > 0.5:
        bias = ' > '
    print(str(i[0]) + str(bias) + str(i[1]))
# convert history of progression into a .txt file cuz showin' 45 megabytes of characters in one shell, pretty much sucks
while True:
    no = input('Would like millions of rational numbers representing millions of creatures dying out which one creature is the best? : ')
    if no == 'yes':
        f = open('history of cost.txt','x')
        f.close()
        f = open('history of cost.txt','w')
        for i in history:
            for j in i:
                f.write(str(j) + "\n")
            f.write('\n next gen: \n')
        f.close()
    else:
        print('Alright, then, MILLIONS OF BABIES SLAUGHTERED JUST TO COMPARE 2 NUMBERS????????!!!!!!!!!')
#                                                       WE DID IT!!! WE FRIGGIN' MANAGED TO SLAUGHTER...I mean create an AI!!
