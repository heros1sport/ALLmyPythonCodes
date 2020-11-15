import pygame
import random
import time
import matplotlib.pyplot as plt
pygame.init()
scr= pygame.display.set_mode((600,600))

class Organism:
    def __init__(self,energy,size,speed):
        self.energy = energy
        self.size = size
        self.x = random.randint(1,600)
        self.y = random.randint(1,600)
        self.speed = speed
        self.me = "N"
    def move(self):
        xoff = random.randint(-self.speed,self.speed)
        yoff = random.randint(-self.speed,self.speed)
        while self.x + xoff < 0 or self.x + xoff > 600 or self.y + yoff < 0 or self.y + yoff > 600:
            xoff = random.randint(-self.speed,self.speed)
            yoff = random.randint(-self.speed,self.speed)
        self.x += xoff
        self.y += yoff
    def show(self):
        pygame.draw.rect(scr,(255,0,0),pygame.Rect(self.x,self.y,self.size,self.size))
    def collide(self,ls):
        def CHECK(i):
            yea = 0
            if self.x > i.x and self.x < i.x+i.size and self.y > i.y and self.y < i.y+i.size:
                yea = 1    
            if self.x+10 > i.x and self.x+self.size < i.x+i.size and self.y > i.y and self.y < i.y+i.size:
                yea = 1        
            if self.x+10 > i.x and self.x+self.size < i.x+i.size and self.y+self.size > i.y and self.y+self.size < i.y+i.size:
                yea = 1
            if self.x > i.x and self.x < i.x+i.size and self.y+i.size > i.y and self.y+10 < i.y+i.size:
                yea = 1
            if yea == 0:
                return False
            else:
                return True
        yea = 0
        for i in range(len(ls)):
            if CHECK(ls[i]):
                if ls[i].energy*ls[i].size > self.energy*self.size and ls[i].me == "N":
                    yea = 1
                elif ls[i].energy*ls[i].size < self.energy*self.size and ls[i].me == "N":
                    self.energy += ls[i].energy
                    self.size += ls[i].size
                    del ls[i]
                elif ls[i].energy*ls[i].size > self.energy*self.size and ls[i].me == "H":
                    self.energy += 10
                    self.size += 5
                elif ls[i].energy*ls[i].size < self.energy*self.size and ls[i].me == "H":
                    self.energy += ls[i].energy
                    self.size += ls[i].size
                    del ls[i]
        if yea == 0:
            return False
        else:
            return True
    def update_hunger(self):
        self.energy -= self.speed/12
        self.size -= self.speed/12
class Organism2:
    def __init__(self,energy,size,speed):
        self.energy = energy
        self.size = size
        self.x = random.randint(1,600)
        self.y = random.randint(1,600)
        self.speed = 5
        self.me = "H"
    def show(self):
        pygame.draw.rect(scr,(0,255,0),pygame.Rect(self.x,self.y,self.size,self.size))
        self.energy +=2
        self.size +=2
    def move(self):
        xoff = random.randint(-self.speed,self.speed)
        yoff = random.randint(-self.speed,self.speed)
        while self.x + xoff < 0 or self.x + xoff > 600 or self.y + yoff < 0 or self.y + yoff > 600:
            xoff = random.randint(-self.speed,self.speed)
            yoff = random.randint(-self.speed,self.speed)
        self.x += xoff
        self.y += yoff
    def collide(self,ls):
        def CHECK(i):
            yea = 0
            if self.x > i.x and self.x < i.x+i.size and self.y > i.y and self.y < i.y+i.size:
                yea = 1    
            if self.x+10 > i.x and self.x+self.size < i.x+i.size and self.y > i.y and self.y < i.y+i.size:
                yea = 1        
            if self.x+10 > i.x and self.x+self.size < i.x+i.size and self.y+self.size > i.y and self.y+self.size < i.y+i.size:
                yea = 1
            if self.x > i.x and self.x < i.x+i.size and self.y+i.size > i.y and self.y+10 < i.y+i.size:
                yea = 1
            if yea == 0:
                return False
            else:
                return True
        yea = 0
        for i in range(len(ls)):
            if CHECK(ls[i]):
                if ls[i].me == "N":
                    yea = 1
        if yea == 0:
            return False
        else:
            return True
orgs = []
for i in range(900):
    orgs.append(Organism(random.randint(0,100),random.randint(0,20),random.randint(5,15)))
for i in range(100):
    orgs.append(Organism2(random.randint(0,100),random.randint(0,20),random.randint(5,15)))
yea = True
org1_his = []
org2_his = []
while True:
    org1 = 0
    org2 = 0
    for i in orgs:
        if i.__class__.__name__ == "Organism":
            org1 += 1
        if i.__class__.__name__ == "Organism2":
            org2 += 1
    org1_his.append(org1)
    org2_his.append(org2)
    for event in pygame.event.get():
        if event.type == 5:
            
            plt.stackplot(list(range(0,len(org1_his))),org1_his,org2_his,colors=["red", "green"])
            plt.show()
    scr.fill((0,0,0))
    for i in range(len(orgs)):
        try:
            try:
                orgs[i].move()
            except:
                pass
            orgs[i].show()
            if orgs[i].collide(orgs):
                del orgs[i]
            if orgs[i].energy < 0:
                del orgs[i]
            if orgs[i].size < 0:
                del orgs[i]
            if orgs[i].energy > 50 and orgs[i].size > 20:
                if orgs[i].__class__.__name__ == "Organism":
                    orgs.append(Organism(random.randint(0,100),random.randint(0,20),random.randint(5,15)))
                    orgs[i].energy -= 20
                    orgs[i].size -= 10
                else:
                    orgs.append(Organism2(random.randint(0,100),random.randint(0,20),random.randint(5,15)))
                    orgs[i].energy -= 20
                    orgs[i].size -= 10
            try:
                orgs[i].update_hunger()
            except:
                pass
        except:
            pass

    pygame.display.update()

    
