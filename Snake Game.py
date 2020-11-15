print("HEY,My name is Shaurya,i am in 6th grade, and I am 11 years old.I made this on 30th of December And I would like to say that i would be really cool if you appreciated this game(or project,whatever),It would really give me a booster, so yeah.\nAnd if any companies like Google or Apple take notice of me, please tell me immediately..It is my dream to work in a famous company(like Google and\nApple).Hope you like this game.Peace from India.")
import pygame
import time
import random
pygame.init()
scr = pygame.display.set_mode((500,500))
# IF THIS CODE WAS PRETTY FREAKIN' HARD TO WRITE, IT SHOULD BE HELLA HARD TO UNDERSTAND.
#----------------------------------------------------------------------class : self-----------------------------------------------------------------
class self:
    body = [[0,0],[10,0]]
    foodpos = [random.randint(0,50)*10,random.randint(0,50)*10]
    def show():
        for i in range(len(self.body)):
            pygame.draw.rect(scr,(0,255,0),pygame.Rect(self.body[i][0],self.body[i][1],10,10))
    def right():
        del self.body[0]
        self.body.append([self.body[-1][0]+10,self.body[-1][1]])
    def left():
        del self.body[0]
        self.body.append([self.body[-1][0]-10,self.body[-1][1]])
    def down():
        del self.body[0]
        self.body.append([self.body[-1][0],self.body[-1][1]+10])
    def up():
        del self.body[0]
        self.body.append([self.body[-1][0],self.body[-1][1]-10])
    def food():
        pygame.draw.rect(scr,(255,0,0),pygame.Rect(self.foodpos[0],self.foodpos[1],10,10))
#------------------------------------------------------------------------GAME------------------------------------------------------------------------
self.show()
a = 0
direction = 'right'
run = True
while run:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
    scr.fill((0,0,0))
    self.food()
    if key[pygame.K_RIGHT] and direction != 'left':
        direction = 'right'
    if key[pygame.K_DOWN] and direction != 'up':
        direction = 'down'
    if key[pygame.K_UP] and direction != 'down':
        direction = 'up'
    if key[pygame.K_LEFT] and direction != 'right':
        direction = 'left'
    if direction == 'right':
        self.right()
    if direction == 'down':
        self.down()
    if direction == 'left':
        self.left()
    if direction == 'up':
        self.up()
    for i in range(0,len(self.body)-1):
        if self.body[-1] == self.body[i]:
            self.body[-1] = [10,0]
    if self.body[-1][0] > 490:
        self.body[-1] = [10,0]
    if self.body[-1][0] < 0:
        self.body[-1] = [10,0]
    if self.body[-1][1] < 0:
        self.body[-1] = [10,0]
    if self.body[-1][1] > 490:
        self.body[-1] = [10,0]
    if self.foodpos == self.body[-1]:
        if direction == 'right':
            self.body.insert(0,[self.body[0][0]-10,self.body[0][1]])
            self.body.insert(0,[self.body[0][0]-10,self.body[0][1]])
            self.body.insert(0,[self.body[0][0]-10,self.body[0][1]])
        if direction == 'left':
            self.body.insert(0,[self.body[0][0]+10,self.body[0][1]])
            self.body.insert(0,[self.body[0][0]+10,self.body[0][1]])
            self.body.insert(0,[self.body[0][0]+10,self.body[0][1]])
        if direction == 'down':
            self.body.insert(0,[self.body[0][0],self.body[0][1]-10])
            self.body.insert(0,[self.body[0][0],self.body[0][1]-10])
            self.body.insert(0,[self.body[0][0],self.body[0][1]-10])
        if direction == 'up':
            self.body.insert(0,[self.body[0][0],self.body[0][1]+10])
            self.body.insert(0,[self.body[0][0],self.body[0][1]+10])
            self.body.insert(0,[self.body[0][0],self.body[0][1]+10])
        self.foodpos = [random.randint(0,49)*10,random.randint(0,49)*10]
    self.show()
    pygame.display.update()
    time.sleep(0.07)
    a += 1
#---------------------------------------------------------------------- THE END --------------------------------------------------------------------
# WAIT, it's not the end yet. GO STRAIGHT DOWN !!


























#----------------------------------------------------------------------FusionGames.co---------------------------------------------------------------
# Just kidding, that's not my company, alright?
# I'm Shaurya and nice to meet whoever is seeing my code.
# This is quite an old game, it felt interesting to me for some reason, so i made it. Dang, nice game right?
            
