import time
import pygame
pygame.init()
scr = pygame.display.set_mode((600,500))
scr.fill((255,255,255))
class self:
    lst1 = [450,200,200]
    lst2 = [400,200,200]# y, width, x
    main = [600,200]
    def createRect(left,top,width,height):
        pygame.draw.rect(scr,(255,0,0),pygame.Rect(left,top,width,height))
    def lst1_():
        self.lst1[1] = self.lst2[1]
        self.lst1[2] = self.lst2[2]
self.createRect(200,self.lst1[0],self.lst1[1],50)
self.createRect(200,self.lst2[1],self.lst2[1],50)
pygame.display.update()
switch = -1
a = 1
while True:
    scr.fill((255,255,255))
    for event in pygame.event.get():
        pass
    if event.type == 5:
        if self.main[0] < self.lst2[2]+self.lst2[1] and self.main[0] > self.lst2[2]:
            self.lst1_()
            self.lst2[1] -= (self.main[0] - self.lst2[2])
            self.lst2[2] = self.main[0]
            self.main[1] = (self.lst2[2]+self.lst2[1] - self.main[0])
            time.sleep(0.3)
        if self.main[0]+self.main[1] < self.lst2[2]+self.lst2[1] and self.main[0]+self.main[1] > self.lst2[2]:
            self.lst1_()
            self.lst2[1] = (self.main[0]+self.main[1]-self.lst2[2])
            self.main[1] = (self.main[0]+self.main[1]-self.lst2[2])
        self.main[0] = 600
        time.sleep(0.3)
        switch = -1
    if switch == -1:
        time.sleep(0.01)
        self.createRect(self.main[0],350,self.main[1],50)
        self.main[0] -= 1
    if switch == 1:
        time.sleep(0.01)
        self.createRect(self.main[0],350,self.main[1],50)
        self.main[0] += 1
    self.createRect(self.lst1[2],self.lst1[0],self.lst1[1],50)
    self.createRect(self.lst2[2],self.lst2[0],self.lst2[1],50)
    if self.main[0] == 0 and switch == -1:
        switch = 1
    if self.main[0] == 600 - self.main[1] and switch == 1:
        switch = -1
    pygame.display.update()
