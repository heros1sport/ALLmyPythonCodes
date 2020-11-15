import pygame
import random
pygame.init()
scr = pygame.display.set_mode((1300,680))
font = pygame.font.SysFont('Agency FB',20)
alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ',',','.','!','?']
word = input()
gen = 0
guess_words = []
guess_fitness = []
w = ''
for i in range(50):
    w = ''
    for i in range(len(word)):
        w += alphabet_list[random.randint(0,len(alphabet_list) - 1)]
    guess_words.append(w)
fitness = 0
for i in guess_words:
    fitness = 0
    for j in range(len(word)):
        if i[j] == word[j]:
            fitness += 1
    guess_fitness.append(fitness * 100 / len(word))
    
for i in range(len(guess_words)):
    guess_words[i] = [guess_words[i],guess_fitness[i]]
    
for i in range(len(guess_words) - 1):
    print(guess_words[i][0] + "  " + str(guess_words[i][1]))
best_word = ''
gen = 1
fitness_history = [0]
mutations_per_generation = []
while True:
    if word == best_word:
        break
    for event in pygame.event.get():
        pass
    # search for best fitness scores
    best_word = ''
    best_fitness = 0
    fitness = 0
    for s in range(len(guess_words)-1):
        fitness = int(guess_words[s][1])
        if best_fitness < fitness:
            best_word = guess_words[s][0]
            best_fitness = fitness
        
    # make new replicates of the best word (with 30% chance of words having tweaks in letters)
    d2 = ''
    ko = 0
    mutations_per_generation = []
    for i in range(len(guess_words)):
        
        
        if random.randint(1,3) == 2:
            bword = best_word
            f = random.randint(0,len(bword)-1)
            
            if f == len(bword)-1:
                d = ''
            else:
                d2 = bword[f+1:]
            b = alphabet_list[random.randint(0,len(alphabet_list) - 1)]
            d1 = bword[0:f]
            if f == len(bword)-1:
                bword = d1 + b
            else:
                bword = d1 + b + d2
                
            if f == len(bword)-1:
                d = ''
            else:
                d2 = bword[f+1:]
            b = alphabet_list[random.randint(0,len(alphabet_list) - 1)]
            d1 = bword[0:f]
            if f == len(bword)-1:
                bword = d1 + b
            else:
                bword = d1 + b + d2
            fitness = 0
            for j in range(len(word)):
                if bword[j] == word[j]:
                    fitness += 1
            guess_words[i] = [bword , fitness * 100 / len(word)]
            mutations_per_generation.append([bword , fitness * 100 / len(word)])
        else:
            guess_words[i][0] = best_word
            fitness = 0
            for j in range(len(word)):
                if guess_words[i][0][j] == word[j]:
                    fitness += 1
            guess_words[i][1] = fitness * 100 / len(word)
    print("GENERATION : " + str(gen) + "\n")
    for i in guess_words:
        print(i[0] + "  " + str(i[1]))
    print("Best word : " + best_word)
    print("Fitness of best word : " + str(best_fitness))
    gen += 1
    fitness_history.append(best_fitness)
    scr.fill((0,0,0))
    py = 700
    px = 0
    y = 700
    x = 0
    pos1 = 60
    for i in mutations_per_generation:
        pos1 += 20
        if int(i[1]) > best_fitness:
            scr.blit(font.render(str(i),15,(0,255,0)),(0,pos1))
        elif int(i[1]) < best_fitness:
            scr.blit(font.render(str(i),15,(255,0,0)),(0,pos1))
        elif int(i[1]) == best_fitness:
            scr.blit(font.render(str(i),15,(255,255,0)),(0,pos1))
    scr.blit(font.render("Fitness : " + str(best_fitness) + "%",20,(0,255,255)),(0,0))
    scr.blit(font.render("Generation : " + str(gen),20,(0,255,255)),(0,20))
    scr.blit(font.render("Main generation gene : " + str(best_word) + " || Actual Word : " + str(word),20,(0,255,255)),(0,40))
    scr.blit(font.render("Mutated genes : ",20,(0,255,255)),(0,60))
    for i in fitness_history:
        y = 680 - (i * 2)
        x += 1300 / len(fitness_history)
        pygame.draw.line(scr,(255,0,0),(px,py),(x,y),5)
        py = y
        px = x
    
    pygame.display.update()
