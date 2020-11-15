import os
import random
import pygame
import time
from Fusion import *
pygame.init()
scr = pygame.display.set_mode((600,500))
pygame.display.set_caption("""RUBIX Slide Puzzle - An 10 year old made this so, RESPECT!!!846 lines of code(literally)""")
font2 = pygame.font.SysFont('OCR A Extended',33)
font3 = pygame.font.SysFont('OCR A Extended',15,bold = False)
print("""HEY,My name is Shaurya,i am in 6th grade, and I am 10 years old.I made this on 15th of August(three days before my birthday)
And I would like to say that i would be really cool if you appreciated this game(or project,whatever),It would really give me a booster, so yeah.
And if any companies like Google or Apple take notice of me, please tell me immediately..It is my dream to work in a famous company(like Google and
Apple).Hope you like this game.
Peace from India.""")
#-------------------------------------------------------------class: self---------------------------------------------------------------------------
players = 1
#Menu functions
class self:
    Tutorial = False
    keyPressed = pygame.key.get_pressed()
    switch = True
    event = None
    middleOfTitle = (150,50)
    font = pygame.font.SysFont('Courier New',45)
    def Title():
        title = self.font.render("RUBIX PUZZLE",10,(255,255,0))
        scr.blit(title,self.middleOfTitle)
        pygame.display.update()
    def PlayButton():
        Mpos = pygame.mouse.get_pos()
        if Mpos[0] > 250 and Mpos[0] < 350 and Mpos[1] > 150 and Mpos[1] < 200:
            pygame.draw.rect(scr,(0,255,0),pygame.Rect(250,150,100,50))
            font2 = pygame.font.SysFont('Agency FB',35)
            text = font2.render("Play",35,(0,255,255))
            scr.blit(text,(275,150))
            pygame.display.update()
            gh = self.event
            if gh.type == 5:
                players = 1
                self.switch = False
        else:
            pygame.draw.rect(scr,(0,0,255),pygame.Rect(250,150,100,50))
            font2 = pygame.font.SysFont('Agency FB',35)
            text = font2.render("Play",35,(0,255,255))
            scr.blit(text,(275,150))
            pygame.display.update()
            Mpos = pygame.mouse.get_pos()
    def QuitButton():
        Mpos = pygame.mouse.get_pos()
        if Mpos[0] > 250 and Mpos[0] < 350 and Mpos[1] > 250 and Mpos[1] < 300:
            pygame.draw.rect(scr,(255,0,255),pygame.Rect(250,250,100,50))
            font2 = pygame.font.SysFont('Agency FB',35)
            text = font2.render("Quit",35,(100,255,100))
            scr.blit(text,(275,250))
            pygame.display.update()
            gh = self.event
            if gh.type == 5:
                quit()
        else:
            pygame.draw.rect(scr,(0,0,255),pygame.Rect(250,250,100,50))
            font2 = pygame.font.SysFont('Agency FB',35)
            text = font2.render("Quit",35,(100,255,100))
            scr.blit(text,(275,250))
            pygame.display.update()
    def InstructionsButton():
        Mpos = pygame.mouse.get_pos()
        if Mpos[0] > 250 and Mpos[0] < 350 and Mpos[1] > 350 and Mpos[1] < 400:
            pygame.draw.rect(scr,(0,255,255),pygame.Rect(250,350,100,50))
            font2 = pygame.font.SysFont('Agency FB',35)
            text = font2.render("Rules",35,(100,255,100))
            scr.blit(text,(268,350))
            pygame.display.update()
            gh = self.event
            if gh.type == 5:
                scr.fill((0,0,0))
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        self.keyPressed = pygame.key.get_pressed()
                    font2 = pygame.font.SysFont('Agency FB',25)
                    text = font2.render('Goal: duplicate the Pattern onto the Board in the middle from the Goal Board',25,(0,255,0))
                    scr.blit(text,(0,0))
                    text = font2.render('How to play:Use arrow keys to move the color tiles around the blank tile ',25,(0,255,0))
                    scr.blit(text,(0,35))
                    text = font2.render('Press B to go back',25,(0,255,0))
                    scr.blit(text,(0,70))
                    pygame.display.update()
                    
                    if self.keyPressed[pygame.K_b]:
                        break
                scr.fill((0,0,0))
                self.Title()
                pygame.display.update()
        else:
            font2 = pygame.font.SysFont('Agency FB',35)
            pygame.draw.rect(scr,(0,0,255),pygame.Rect(250,350,100,50))
            text = font2.render("Rules",35,(100,255,100))
            scr.blit(text,(268,350))
            pygame.display.update()
    def TutorialButton():
        Mpos = pygame.mouse.get_pos()
        if Mpos[0] > 250 and Mpos[0] < 350 and Mpos[1] > 450 and Mpos[1] < 500:
            pygame.draw.rect(scr,(255,0,255),pygame.Rect(250,450,100,50))
            font2 = pygame.font.SysFont('Agency FB',35)
            text = font2.render("Tutorial",35,(100,255,100))
            scr.blit(text,(257,450))
            pygame.display.update()
            gh = self.event
            if gh.type == 5:
                self.Tutorial = True
                self.switch = False
        else:
            font2 = pygame.font.SysFont('Agency FB',35)
            pygame.draw.rect(scr,(0,0,255),pygame.Rect(250,450,100,50))
            text = font2.render("Tutorial",35,(100,255,100))
            scr.blit(text,(257,450))
            pygame.display.update()

#-----------------------------------------------------------class main------------------------------------------------------------------------------
#Menu function            
class main(self):
    def Menu():
        self.Title()
        while self.switch:
            for self.event in pygame.event.get():
                self.PlayButton()
                self.QuitButton()
                self.InstructionsButton()
                self.TutorialButton()
            self.PlayButton()
            self.QuitButton()
            self.InstructionsButton()
            self.TutorialButton()
#------------------------------------------------------------class: selfGame-------------------------------------------------------------------------
#All functions required repeatedly for Rubix Slide Puzzle ( this game wasn't sponsored by RUBIX but the logic was sponsored by RUBIX so... yeah)
class selfGame(self):
    keyPressed = None
    moves = 0
    IdentifyAimBlock = []
    IdentifyBlock = []
    blockMissingPos = []
    positions = [(0,0),(0,120),(0,240),(0,360),(0,480),
                 (120,0),(120,120),(120,240),(120,360),(120,480),
                 (240,0),(240,120),(240,240),(240,360),(240,480),
                 (360,0),(360,120),(360,240),(360,360),(360,480),
                 (480,0),(480,120),(480,240),(480,360),(480,480)]
    SquareIds = list(range(1,26))
    def loading():
        l1 = pygame.image.load('C:/Users/Guest/Desktop/PythonProjects/loading images/loading1.jpg')
        l2 = pygame.image.load('C:/Users/Guest/Desktop/PythonProjects/loading images/loading2.jpg')
        l3 = pygame.image.load('C:/Users/Guest/Desktop/PythonProjects/loading images/loading3.jpg')
        l4 = pygame.image.load('C:/Users/Guest/Desktop/PythonProjects/loading images/loading4.jpg')
        l1 = pygame.transform.smoothscale(l1,(100,100))
        l2 = pygame.transform.smoothscale(l2,(100,100))
        l3 = pygame.transform.smoothscale(l3,(100,100))
        l4 = pygame.transform.smoothscale(l4,(100,100))
        font2 = pygame.font.SysFont('OCR A Extended',33)
        text = font2.render("Loading..",10,(0,255,255))
        scr.blit(text,(225,350))
        pygame.display.update()
        scr.blit(l1,(250,250))
        pygame.display.update()
        time.sleep(1)
        scr.blit(l2,(250,250))
        pygame.display.update()
        time.sleep(1)
        scr.blit(l2,(250,250))
        pygame.display.update()
        time.sleep(1)
        scr.blit(l3,(250,250))
        pygame.display.update()
        time.sleep(1)
        scr.blit(l4,(250,250))
        pygame.display.update()
        time.sleep(1)
    def makeBar():
        pygame.draw.line(scr,(255,0,0),(600.1,1),(600,600),5)

        pygame.draw.rect(scr,(100,100,100),pygame.Rect(600,1,200,600))

        text = font2.render("Goal Board",23,(255,255,0))
        scr.blit(text,(603,200))
        text = font3.render("Randomize Pattern(R)",8,(0,255,255))
        scr.blit(text,(605,300))
        text = font3.render("Randomize Board(B)",10,(0,255,255))
        scr.blit(text,(605,400))
        text = font3.render("Sound->",10,(0,255,255))
        scr.blit(text,(650,580))
        pygame.display.update()
    def lines():
            pygame.draw.line(scr,(0,0,0),(120,1),(120,600),5)
            pygame.draw.line(scr,(0,0,0),(240,1),(240,600),5)
            pygame.draw.line(scr,(0,0,0),(360,1),(360,600),5)
            pygame.draw.line(scr,(0,0,0),(480,1),(480,600),5)

            pygame.draw.line(scr,(0,0,0),(1,120),(600,120),5)
            pygame.draw.line(scr,(0,0,0),(1,240),(600,240),5)
            pygame.draw.line(scr,(0,0,0),(1,360),(600,360),5)
            pygame.draw.line(scr,(0,0,0),(1,480),(600,480),5)

            pygame.draw.rect(scr,(0,0,0),pygame.Rect(120,120,360,360),10)
    def makeBoard():
        random.shuffle(selfGame.SquareIds)
        i = 1
        Ids = selfGame.SquareIds
        while i != 6:
            index = Ids.index(i)
            pygame.draw.rect(scr,(0,0,255),pygame.Rect(selfGame.positions[index][0],selfGame.positions[index][1],120,120))
            selfGame.IdentifyBlock += [[(0,0,255),[selfGame.positions[index][0],selfGame.positions[index][1]]]]
            i += 1
        while i != 11:
            index = Ids.index(i)
            pygame.draw.rect(scr,(255,0,0),pygame.Rect(selfGame.positions[index][0],selfGame.positions[index][1],120,120))
            selfGame.IdentifyBlock += [[(255,0,0),[selfGame.positions[index][0],selfGame.positions[index][1]]]]
            i += 1
        while i != 16:
            index = Ids.index(i)
            pygame.draw.rect(scr,(0,255,0),pygame.Rect(selfGame.positions[index][0],selfGame.positions[index][1],120,120))
            selfGame.IdentifyBlock += [[(0,255,0),[selfGame.positions[index][0],selfGame.positions[index][1]]]]
            i += 1
        while i != 21:
            index = Ids.index(i)
            pygame.draw.rect(scr,(0,255,255),pygame.Rect(selfGame.positions[index][0],selfGame.positions[index][1],120,120))
            selfGame.IdentifyBlock += [[(0,255,255),[selfGame.positions[index][0],selfGame.positions[index][1]]]]
            i += 1
        while i != 25:
            index = Ids.index(i)
            pygame.draw.rect(scr,(255,255,0),pygame.Rect(selfGame.positions[index][0],selfGame.positions[index][1],120,120))
            selfGame.IdentifyBlock += [[(255,255,0),[selfGame.positions[index][0],selfGame.positions[index][1]]]]
            i += 1
        selfGame.blockMissingPos = [selfGame.positions[Ids.index(25)][0],selfGame.positions[Ids.index(25)][1]]
        selfGame.lines()
        pygame.display.update()
    def divideSpace():
        pygame.draw.rect(scr,(0,0,0),pygame.Rect(600,0,200,200),5)
        pygame.display.update()
    def leftOfMB():
        IB = selfGame.IdentifyBlock
        try:
            IB.index([(0,0,255),[selfGame.blockMissingPos[0]-120,selfGame.blockMissingPos[1]]])
            return (0,0,255)
        except ValueError:
            pass
        try:
            IB.index([(0,255,0),[selfGame.blockMissingPos[0]-120,selfGame.blockMissingPos[1]]])
            return (0,255,0)
        except ValueError:
            pass
        try:
            IB.index([(255,0,0),[selfGame.blockMissingPos[0]-120,selfGame.blockMissingPos[1]]])
            return (255,0,0)
        except ValueError:
            pass  
        try:
            IB.index([(0,255,255),[selfGame.blockMissingPos[0]-120,selfGame.blockMissingPos[1]]])
            return (0,255,255)
        except ValueError:
            pass
        try:
            IB.index([(255,255,0),[selfGame.blockMissingPos[0]-120,selfGame.blockMissingPos[1]]])
            return (255,255,0)
        except ValueError:
            pass
    def rightOfMB():
        IB = selfGame.IdentifyBlock
        try:
            IB.index([(0,0,255),[selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1]]])
            return (0,0,255)
        except ValueError:
            pass
        try:
            IB.index([(0,255,0),[selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1]]])
            return (0,255,0)
        except ValueError:
            pass
        try:
            IB.index([(255,0,0),[selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1]]])
            return (255,0,0)
        except ValueError:
            pass  
        try:
            IB.index([(0,255,255),[selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1]]])
            return (0,255,255)
        except ValueError:
            pass
        try:
            IB.index([(255,255,0),[selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1]]])
            return (255,255,0)
        except ValueError:
            pass
    def upOfMB():
        IB = selfGame.IdentifyBlock
        try:
            IB.index([(0,0,255),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]-120]])
            return (0,0,255)
        except ValueError:
            pass
        try:
            IB.index([(0,255,0),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]-120]])
            return (0,255,0)
        except ValueError:
            pass
        try:
            IB.index([(255,0,0),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]-120]])
            return (255,0,0)
        except ValueError:
            pass  
        try:
            IB.index([(0,255,255),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]-120]])
            return (0,255,255)
        except ValueError:
            pass
        try:
            IB.index([(255,255,0),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]-120]])
            return (255,255,0)
        except ValueError:
            pass   
    def downOfMB():
        IB = selfGame.IdentifyBlock
        try:
            IB.index([(0,0,255),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]+120]])
            return (0,0,255)
        except ValueError:
            pass
        try:
            IB.index([(0,255,0),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]+120]])
            return (0,255,0)
        except ValueError:
            pass
        try:
            IB.index([(255,0,0),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]+120]])
            return (255,0,0)
        except ValueError:
            pass  
        try:
            IB.index([(0,255,255),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]+120]])
            return (0,255,255)
        except ValueError:
            pass
        try:
            IB.index([(255,255,0),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]+120]])
            return (255,255,0)
        except ValueError:
            pass
    def AimBoard():
        pygame.draw.line(scr,(0,0,0),(666,0),(666,200),5)
        pygame.draw.line(scr,(0,0,0),(732,0),(732,200),5)
        pygame.draw.line(scr,(0,0,0),(798,0),(798,200),5)

        pygame.draw.line(scr,(0,0,0),(600,66),(800,66),5)
        pygame.draw.line(scr,(0,0,0),(600,132),(800,132),5)
        pygame.draw.line(scr,(0,0,0),(600,198),(800,198),5)

        pygame.display.update()
    def createRandom():
        def randomColor():
            g = random.randint(1,5)
            if g == 1:
                return (0,0,255)
            if g == 2:
                return (0,255,0)
            if g == 3:
                return (255,0,0)
            if g == 4:
                return (0,255,255)
            if g == 5:
                return (255,255,0)
        i = 0
        while i != 198:
            gha = randomColor()
            selfGame.IdentifyAimBlock.append(gha)
            pygame.draw.rect(scr,gha,pygame.Rect(600+i,0,66,66))
            i += 66
        i = 0
        while i != 198:
            gha = randomColor()
            selfGame.IdentifyAimBlock.append(gha)
            pygame.draw.rect(scr,gha,pygame.Rect(600+i,66,66,66))
            i += 66
        i = 0
        while i != 198:
            gha = randomColor()
            selfGame.IdentifyAimBlock.append(gha)
            pygame.draw.rect(scr,gha,pygame.Rect(600+i,132,66,66))
            i += 66
        f = open('com.txt','w')
        f.write(str(selfGame.IdentifyAimBlock))
        f.close()
        pygame.display.update()
    def makeSoundIcon():
        sound = pygame.image.load('C:/Users/Guest/Desktop/PythonProjects/sound.jpg')
        sound = pygame.transform.smoothscale(sound,(50,50))
        scr.blit(sound,(750,550))
        pygame.display.update()
    def makeNoSoundIcon():
        sound = pygame.image.load('C:/Users/Guest/Desktop/PythonProjects/nosound.jpg')
        sound = pygame.transform.smoothscale(sound,(50,50))
        scr.blit(sound,(750,550))
        pygame.display.update()
    def Moves():
        font2 = pygame.font.SysFont('Agency FB',25,bold = False)
        pygame.draw.rect(scr,(100,100,100),pygame.Rect(600,450,200,80))
        text = font2.render("Moves: " + str(selfGame.moves),10,(0,255,255))
        scr.blit(text,(609,450))
        pygame.display.update()
    def Win():
        scr.fill((0,0,0))
        font2 = pygame.font.SysFont('OCR A Extended',15,bold = True)
        text = font2.render("Congrats!!You have solved the puzzle in " + str(selfGame.moves) + " moves-",10,(0,255,255))
        scr.blit(text,(0,0))
        text = font2.render("Press P to play again,Press M to go to menu",10,(0,255,255))
        scr.blit(text,(0,50))
        pygame.display.update()
    def RefreshTutorialScreen():
        pygame.draw.rect(scr,(100,100,100),pygame.Rect(605,350,200,53))
    def TutorialPrint(string,pos):
        font2 = pygame.font.SysFont('Courier New',15,bold = False)
        text = font2.render(string,10,(0,255,255))
        scr.blit(text,pos)
        pygame.display.update()
#---------------------------------------------------------------------GAME---------------------------------------------------------------------------
main.Menu()
scr.fill((0,0,0))
selfGame.loading()
pygame.display.update()
time.sleep(2)
scr = pygame.display.set_mode((800,600))
selfGame.makeBoard()
selfGame.divideSpace()
selfGame.makeBar()
selfGame.createRandom()
selfGame.AimBoard()
selfGame.makeSoundIcon()
selfGame.Moves()
pygame.draw.line(scr,(0,0,0),(600.1,1),(600,600),10)
pygame.display.update()
switch = True
stage = 1
while players == 1:
    #TUTORIAL
    if self.Tutorial == True:
        if stage == 1:
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Welcome to Rubix Slide",(605,350))
            selfGame.TutorialPrint("Puzzle.Press c to go ",(605,365))
            selfGame.TutorialPrint("ahead in the tutorial",(605,375))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("This is Tutorial mode",(605,350))
            Fusion.waitSeconds(2)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("I will teach you to",(605,350))
            selfGame.TutorialPrint("how to solve a puzzle",(605,360))
            selfGame.TutorialPrint("in Rubix Slide Puzzle",(605,370))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("First:How to play",(605,350))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Press c to continue",(605,350))
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            stage = 2
        if stage == 2:
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Press RIGHT button of",(605,350))
            selfGame.TutorialPrint("your keyboard.",(605,360))
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_RIGHT]:
                    jk = selfGame.rightOfMB()
                    try:
                        pygame.draw.rect(scr,jk,pygame.Rect(selfGame.blockMissingPos[0],selfGame.blockMissingPos[1],120,120))
            
                        pygame.draw.rect(scr,(0,0,0),pygame.Rect(selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1],120,120))
                        ID = selfGame.IdentifyBlock
                        ID[ID.index([selfGame.rightOfMB(),[selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1]]])][1][0] -= 120
                        selfGame.blockMissingPos[0] += 120
                        pygame.display.update()
                        selfGame.moves += 1
                        selfGame.Moves()
                        time.sleep(0.3)
                        if switch:
                            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/shift.wav')
                    except TypeError:
                        pass
                    break
            
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Good.You moved a tile",(605,350))
            selfGame.TutorialPrint("to the left.",(605,360))
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            Fusion.waitSeconds(1)
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Now you can also do ",(605,350))
            selfGame.TutorialPrint("the same with other",(605,360))
            selfGame.TutorialPrint("keys,there are four.",(605,370))
            selfGame.TutorialPrint("keys.UP,DOWN,LEFT",(605,380))
            selfGame.TutorialPrint("RIGHT",(605,390))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("these keys are used",(605,350))
            selfGame.TutorialPrint("to move tiles",(605,360))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Let see what is our",(605,350))
            selfGame.TutorialPrint("goal to achieve.",(605,360))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Press c To Continue",(605,350))
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage= 3
                    break
        if stage == 3:
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Our goal is to",(605,350))
            selfGame.TutorialPrint("copy the 9 blocks",(605,360))
            selfGame.TutorialPrint("in the middle from",(605,370))
            selfGame.TutorialPrint("the goal board.",(605,380))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("And in order to do",(605,350))
            selfGame.TutorialPrint("that we need to use",(605,360))
            selfGame.TutorialPrint("the skills we learnt.",(605,370))
            selfGame.TutorialPrint("In Other ways,we need",(605,380))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("to move the tiles to",(605,350))
            selfGame.TutorialPrint("make the same pattern",(605,360))
            selfGame.TutorialPrint("in the 9 blocks in the",(605,370))
            selfGame.TutorialPrint("board from the Goal",(605,380))
            selfGame.TutorialPrint("Board",(605,390))
            Fusion.waitSeconds(1)
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            selfGame.RefreshTutorialScreen()
            selfGame.TutorialPrint("Now,Good luck with ",(605,350))
            selfGame.TutorialPrint("that,Press c to ",(605,360))
            selfGame.TutorialPrint("Exit tutorial.",(605,370))
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    stage = 2
                    break
            while True:
                for event in pygame.event.get():
                    keyPressed = pygame.key.get_pressed()
                if keyPressed[pygame.K_c]:
                    self.Tutorial = False
                    break
        pygame.draw.line(scr,(0,0,0),(600.1,1),(600,600),10)
        pygame.display.update()
        #Tutorial ends
    for event in pygame.event.get():
        keyPressed = pygame.key.get_pressed()
        selfGame.keyPressed = keyPressed
    if keyPressed[pygame.K_RIGHT]:
        #Move piece
        jk = selfGame.rightOfMB()
        try:
            pygame.draw.rect(scr,jk,pygame.Rect(selfGame.blockMissingPos[0],selfGame.blockMissingPos[1],120,120))
            
            pygame.draw.rect(scr,(0,0,0),pygame.Rect(selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1],120,120))
            ID = selfGame.IdentifyBlock
            #update values 
            ID[ID.index([selfGame.rightOfMB(),[selfGame.blockMissingPos[0]+120,selfGame.blockMissingPos[1]]])][1][0] -= 120
            selfGame.blockMissingPos[0] += 120
            pygame.display.update()
            selfGame.moves += 1
            selfGame.Moves()
            time.sleep(0.3)
            if switch:
                Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/shift.wav')
        except TypeError:
            pass
        pygame.draw.line(scr,(0,0,0),(600.1,1),(600,600),10)
        pygame.display.update()
    if keyPressed[pygame.K_LEFT]:
        try:
            jk = selfGame.leftOfMB()
            pygame.draw.rect(scr,jk,pygame.Rect(selfGame.blockMissingPos[0],selfGame.blockMissingPos[1],120,120))
            pygame.draw.rect(scr,(0,0,0),pygame.Rect(selfGame.blockMissingPos[0]-120,selfGame.blockMissingPos[1],120,120))
            ID = selfGame.IdentifyBlock
            ID[ID.index([selfGame.leftOfMB(),[selfGame.blockMissingPos[0]-120,selfGame.blockMissingPos[1]]])][1][0] += 120
            selfGame.blockMissingPos[0] -= 120
            pygame.display.update()
            selfGame.moves += 1
            selfGame.Moves()
            time.sleep(0.3)
            if switch:
                Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/shift.wav')
        except TypeError:
            pass
        pygame.draw.line(scr,(0,0,0),(600.1,1),(600,600),10)
        pygame.display.update()
    if keyPressed[pygame.K_UP]:
        try:
            jk = selfGame.upOfMB()
            pygame.draw.rect(scr,jk,pygame.Rect(selfGame.blockMissingPos[0],selfGame.blockMissingPos[1],120,120))
            pygame.draw.rect(scr,(0,0,0),pygame.Rect(selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]-120,120,120))
            ID = selfGame.IdentifyBlock
            ID[ID.index([selfGame.upOfMB(),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]-120]])][1][1] += 120
            selfGame.blockMissingPos[1] -= 120
            pygame.display.update()
            selfGame.moves += 1
            selfGame.Moves()
            time.sleep(0.3)
            if switch:
                Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/shift.wav')
        except TypeError:

            pass
        pygame.draw.line(scr,(0,0,0),(600.1,1),(600,600),10)
        pygame.display.update()
    if keyPressed[pygame.K_DOWN]:
        try:
            jk = selfGame.downOfMB()
            pygame.draw.rect(scr,jk,pygame.Rect(selfGame.blockMissingPos[0],selfGame.blockMissingPos[1],120,120))
            pygame.draw.rect(scr,(0,0,0),pygame.Rect(selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]+120,120,120))
            ID = selfGame.IdentifyBlock
            ID[ID.index([selfGame.downOfMB(),[selfGame.blockMissingPos[0],selfGame.blockMissingPos[1]+120]])][1][1] -= 120
            selfGame.blockMissingPos[1] += 120
            pygame.display.update()
            selfGame.moves += 1
            selfGame.Moves()
            time.sleep(0.3)
            if switch:
                Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/shift.wav')
        except TypeError:
            pass
        pygame.draw.line(scr,(0,0,0),(600.1,1),(600,600),10)
        pygame.display.update()
    if keyPressed[pygame.K_r]:
        selfGame.IdentifyAimBlock = []
        selfGame.createRandom()
        selfGame.AimBoard()
        time.sleep(0.3)
        if switch:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/shift.wav')
        selfGame.moves = 0
        selfGame.Moves()
    if keyPressed[pygame.K_b]:
        selfGame.SquareIds = list(range(1,26))
        selfGame.IdentifyBlock = []
        selfGame.blockMissingPos = []
        selfGame.makeBoard()
        pygame.draw.rect(scr,(0,0,0),pygame.Rect(selfGame.blockMissingPos[0],selfGame.blockMissingPos[1],120,120))
        pygame.display.update()
        selfGame.lines()
        time.sleep(0.3)
        if switch:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/shift.wav')
        selfGame.moves = 0
        selfGame.Moves()
    if pygame.mouse.get_pos()[0] > 750 and pygame.mouse.get_pos()[0] < 800 and pygame.mouse.get_pos()[1] > 550 and pygame.mouse.get_pos()[1] < 600 and event.type == 5 and switch == True:
        switch = False
        selfGame.makeNoSoundIcon()
        time.sleep(0.3)
        continue
    if pygame.mouse.get_pos()[0] > 750 and pygame.mouse.get_pos()[0] < 800 and pygame.mouse.get_pos()[1] > 550 and pygame.mouse.get_pos()[1] < 600 and event.type == 5 and switch == False:
        switch = True
        selfGame.makeSoundIcon()
        time.sleep(0.3)
    if keyPressed[pygame.K_i]:
        print(selfGame.IdentifyBlock)
        print(selfGame.IdentifyAimBlock)
#check if the puzzle is solved
    try:
        ID = selfGame.IdentifyBlock
        ID.index([selfGame.IdentifyAimBlock[0],[120,120]])
        ID.index([selfGame.IdentifyAimBlock[1],[240,120]])
        ID.index([selfGame.IdentifyAimBlock[2],[360,120]])
        
        ID.index([selfGame.IdentifyAimBlock[3],[120,240]])
        ID.index([selfGame.IdentifyAimBlock[4],[240,240]])
        ID.index([selfGame.IdentifyAimBlock[5],[360,240]])

        ID.index([selfGame.IdentifyAimBlock[6],[120,360]])
        ID.index([selfGame.IdentifyAimBlock[7],[240,360]])
        ID.index([selfGame.IdentifyAimBlock[8],[360,360]])
        #show that the player has won
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        time.sleep(1)
        pygame.draw.rect(scr,(0,0,0),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        if switch == True:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/rotate.wav')
        time.sleep(1)
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        if switch == True:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/rotate.wav')
        time.sleep(1)
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        if switch == True:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/rotate.wav')
        time.sleep(1)
        pygame.draw.rect(scr,(0,0,0),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        if switch == True:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/rotate.wav')
        time.sleep(1)
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        if switch == True:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/rotate.wav')
        time.sleep(1)
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        if switch == True:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/rotate.wav')
        time.sleep(1)
        pygame.draw.rect(scr,(0,0,0),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        if switch == True:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/rotate.wav')
        time.sleep(1)
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(120,120,360,360),10)
        pygame.display.update()
        if switch == True:
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/rotate.wav')
        time.sleep(1)
        #Win screen
        selfGame.Win()
        while True:
            for event in pygame.event.get():
                keyPressed = pygame.key.get_pressed()
                selfGame.keyPressed = keyPressed
            if keyPressed[pygame.K_p]:
                #restarts game with no data about the last game you played (initializes)
                self.Tutorial = False
                stage = 1
                scr.fill((0,0,0))
                pygame.display.update()
                selfGame.loading()
                selfGame.keyPressed = None
                selfGame.moves = 0
                selfGame.IdentifyAimBlock = []
                selfGame.IdentifyBlock = []
                selfGame.blockMissingPos = []
                selfGame.positions = [(0,0),(0,120),(0,240),(0,360),(0,480),
                                      (120,0),(120,120),(120,240),(120,360),(120,480),
                                      (240,0),(240,120),(240,240),(240,360),(240,480),
                                      (360,0),(360,120),(360,240),(360,360),(360,480),
                                      (480,0),(480,120),(480,240),(480,360),(480,480)]
                selfGame.SquareIds = list(range(1,26))
                scr.fill((0,0,0))
                pygame.display.update()
                time.sleep(2)
                scr = pygame.display.set_mode((800,600))
                selfGame.makeBoard()
                selfGame.divideSpace()
                selfGame.makeBar()
                selfGame.createRandom()
                selfGame.AimBoard()
                selfGame.makeSoundIcon()
                selfGame.Moves()
                pygame.draw.line(scr,(0,0,0),(600.1,1),(600,600),10)
                break
            if keyPressed[pygame.K_m]:
                #initializes menu and game and starts it
                self.Tutorial = False
                stage = 1
                scr.fill((0,0,0))
                pygame.display.update()
                selfGame.loading()
                scr = pygame.display.set_mode((600,500))

                keyPressed = pygame.key.get_pressed()
                self.switch = True
                self.event = None
                self.middleOfTitle = (150,50)
                self.font = pygame.font.SysFont('Courier New',45)
                main.Menu()
                selfGame.keyPressed = None
                selfGame.moves = 0
                selfGame.IdentifyAimBlock = []
                selfGame.IdentifyBlock = []
                selfGame.blockMissingPos = []
                selfGame.positions = [(0,0),(0,120),(0,240),(0,360),(0,480),
                                      (120,0),(120,120),(120,240),(120,360),(120,480),
                                      (240,0),(240,120),(240,240),(240,360),(240,480),
                                      (360,0),(360,120),(360,240),(360,360),(360,480),
                                      (480,0),(480,120),(480,240),(480,360),(480,480)]
                selfGame.SquareIds = list(range(1,26))
                scr.fill((0,0,0))
                pygame.display.update()
                time.sleep(2)
                scr = pygame.display.set_mode((800,600))
                selfGame.makeBoard()
                selfGame.divideSpace()
                selfGame.makeBar()
                selfGame.createRandom()
                selfGame.AimBoard()
                selfGame.makeSoundIcon()
                
                selfGame.Moves()
                pygame.draw.line(scr,(0,0,0),(600.1,1),(600,600),10)
                break
    except ValueError:# All above would only happen if Value Error hadn't caused (or checking didn't go well and some color tiles were missing from the middle)
        
        pass
    # refresh the lines so the squares wouldn't overlap over them
    selfGame.lines()                   
    selfGame.divideSpace()

# self is the parent class of main and selfGame

#end;THANK YOU,.....................
#copyright RUBIX Slide Puzzle, All rights reserved.
#WARNING : Do not edit code or copy this code
#-------------------------------------------------------------FUSION GAMES.co (not a real life company, at least not mine)-----------------------------------------------------------------------
#members : 1.Shaurya(the one who made this game)
#thats all, Thank YOU!for playing this game, and spread the words RUBIX Slide Puzzle.

#                                                            hI,YoU aRe gOnna DiE
#                                                                |                       HELP...   ME!!!!! 
#                                                   ROBOT-->     O                              \  / 
#                                                              |-|-|                             O    
#                                                              || ||                        -- /---\/
#                                                              || ||                        -- \ |  
#                                                               | |                            _/ /
#                                                               | |                              /
"#################################################################################################################################################"
##################################################################################################################################################
##################################################################################################################################################


# I sometimes get that dream.






















































































































































































































































































































