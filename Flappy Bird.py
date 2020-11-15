print("""HEY,My name is Shaurya,i am in 6th grade, and I am 11 years old.I completed this on 29th of October,2019
And I would like to say that i would be really cool if you appreciated this game,It would really give me a booster, so yeah.
And if any companies like Google or Apple take notice of me, please tell me immediately..It is my dream to work in a famous company(like Google and
Apple).Hope you like this game.
Peace from India.""")
import random
import time
import pygame
pygame.init()
font = pygame.font.SysFont('OCR A Extended',35)
width = 600
height = 500 
scr = pygame.display.set_mode((600,500))
global event
event = pygame.event.get()
Mpos = pygame.mouse.get_pos()
pygame.display.set_caption("Flappy Bird - By Fusion (11 yr old)")
#if this code was hard to make, it should be hard to understand.
class Menu:
    def Label(left,top,text,size = 35):
        font = pygame.font.SysFont('OCR A Extended',size)
        text = font.render(text,size,(0,255,255))
        scr.blit(text,(left,top))
    def Title():
        Menu.Label(150,0,"Flappy Bird!!!",45)
        pygame.display.update()
    def buttonPlay():
        if Mpos[0] > 240 and Mpos[0] < 340 and Mpos[1] > 150 and Mpos[1] < 200:
            pygame.draw.rect(scr,(0,255,0),pygame.Rect((width//2)-60,(height//2)-100,100,50))
            Menu.Label(((width//2)-60)+10,((height//2)-100)+5,"Play")
            pygame.display.update()
            return True
        else:
            pygame.draw.rect(scr,(0,0,255),pygame.Rect((width//2)-60,(height//2)-100,100,50))
            Menu.Label(((width//2)-60)+10,((height//2)-100)+5,"Play")
            pygame.display.update()
    def buttonExit():
        if Mpos[0] > 240 and Mpos[0] < 340 and Mpos[1] > 250 and Mpos[1] < 300:
            pygame.draw.rect(scr,(0,255,0),pygame.Rect((width//2)-60,(height//2),100,50))
            Menu.Label(((width//2)-60)+10,((height//2))+5,"Exit")
            pygame.display.update()
            return True
        else:
            pygame.draw.rect(scr,(0,0,255),pygame.Rect((width//2)-60,(height//2),100,50))
            Menu.Label(((width//2)-60)+10,((height//2))+5,"Exit")
            pygame.display.update()
while True:
    Mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        pass
    Menu.buttonPlay()
    if Menu.buttonPlay() == True and event.type == 5:
        break
    Menu.buttonExit()
    if Menu.buttonExit() == True and event.type == 5:
        break

    if Menu.buttonExit() == True and event.type == 5:
        quit()
    Menu.Title()
    
#-----------------------------------------------------------------------------Game init()------------------------------------------------------------------                         
global g
global g2
global g3
global a1
global a2
global g1back

class selfGame(Menu):
    g = 0
    B_x = 250
    B_y = 250
    a = 0
    obs = 600
    run = True
    score = 0 #Edit this if you want to get unlimited points in Flappy Bird,I dont care anymore >:[ dfsafs
    passed =False
    def Score():
        Menu.Label(0,0,str(selfGame.score),25)
    def createBird(x,y):
        b = pygame.image.load('FlappyBird.jpg')
        b = pygame.transform.smoothscale(b,(25,25))
        scr.blit(b,(x,y))
        selfGame.B_x = x
        selfGame.B_y = y
    def gravityDown():
        scr.fill((0,0,0))
        selfGame.Score()
        selfGame.createBird(selfGame.B_x,selfGame.B_y+selfGame.a)
        selfGame.Check()
        selfGame.B_y += selfGame.a
        selfGame.lines(selfGame.g,selfGame.obs)
        selfGame.Check()
        time.sleep(0.03)
        selfGame.a += 1
        return True
    def Up():
        a = 7
        while a != 0 and selfGame.run == True:
            if selfGame.obs == selfGame.B_x:
                selfGame.score += 1
            scr.fill((0,0,0))
            selfGame.Score()
            selfGame.Check()
            selfGame.B_y -= a
            selfGame.createBird(selfGame.B_x,selfGame.B_y-a)
            selfGame.obs -= 5
            selfGame.lines(selfGame.g,selfGame.obs)
            pygame.display.update()
            time.sleep(0.03)
            a -= 1
            selfGame.obs -= 1
    def simulation():
        selfGame.obs -= 5
        if selfGame.obs <= -50:
            selfGame.obs = 650
            selfGame.g = random.randint(100,350)
            selfGame.passed = False
        selfGame.lines(selfGame.g,selfGame.obs)
    def lines(value,x):
        pygame.draw.line(scr,(0,255,0),(x,0),(x,value),50)
        pygame.draw.line(scr,(0,255,0),(x,value+130),(x,500),50)
    def Check():
        x = selfGame.B_x
        y = selfGame.B_y
        if y < selfGame.g or y+25 > selfGame.g+150:
            if x+25 > selfGame.obs and x < selfGame.obs+50:
                time.sleep(1)
                selfGame.Game_Over()#Erase it if u want to be immortal in Flappy Bird,I don't care :)
        if y > 500:
            selfGame.Game_Over()#Erase it if u want to be immortal in Flappy Bird,I don't care :)
    def Game_Over():
        selfGame.run = False
        scr.fill((0,0,0))
        Menu.Label(2,2,"RIP Flappy Bird",20)
        Menu.Label(2,40,"Died at "+ str(time.ctime()) + ",not a big deal",20)
        Menu.Label(2,70,"Press X to exit and R to Retry",20)
        Menu.Label(2,100,"Your Score: " + str(selfGame.score),20)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[pygame.K_x]:
                    quit()
                if key[pygame.K_r]:
                    selfGame.score = 0 
                    selfGame.g = 0
                    selfGame.B_x = 250
                    selfGame.B_y = 250
                    selfGame.a = 0
                    selfGame.obs = 600
                    selfGame.run = True
                    scr.fill((0,0,0))
                    selfGame.g = random.randint(100,350)
                    while selfGame.run:
                        selfGame.Check()
                        for event in pygame.event.get():
                            keyPressed = pygame.key.get_pressed()
                            if event.type == 5 or keyPressed[pygame.K_UP] or keyPressed[pygame.K_SPACE]:
                                selfGame.Up()
                                selfGame.a = 0
                        selfGame.simulation()
                        pygame.display.update()
                        selfGame.gravityDown()
                        selfGame.Score()
                        pygame.display.update()
                        if selfGame.obs < 258 and selfGame.passed == False:
                            selfGame.score += 1
                            selfGame.passed = True


selfGame.g = random.randint(100,350)
while selfGame.run:
    selfGame.Check()
    for event in pygame.event.get():
        keyPressed = pygame.key.get_pressed()
        if event.type == 5 or keyPressed[pygame.K_UP] or keyPressed[pygame.K_SPACE]:
            selfGame.Up()
            selfGame.a = 0
    selfGame.simulation()
    pygame.display.update()
    selfGame.gravityDown()
    selfGame.Score()
    pygame.display.update()
    if selfGame.obs < 250 and selfGame.passed == False:
        selfGame.score += 1
        selfGame.passed = True
        
    
#182 lines in total
    
#(And Finally at the comment of each and every last game)
#Made by Fusion (not a company)
#copyright Flappy Bird.py (i didnt copy graphics of the game, just the logic)
#11yr old made this so yeah if you could just download it....oh u did?
#Peace from India    

