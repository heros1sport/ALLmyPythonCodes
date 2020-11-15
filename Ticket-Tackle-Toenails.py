print("""HEY,My name is Shaurya,i am in 6th grade, and I am 11 years old.I completed this on 15th of November,2019
And I would like to say that i would be really cool if you appreciated this game,It would really give me a booster, so yeah.
And if any companies like Google or Apple take notice of me, please tell me immediately..It is my dream to work in a famous company(like Google and
Apple).Hope you like this game.
Peace from India.""")
import time
import pygame
pygame.init()
font = pygame.font.SysFont('OCR A Extended',35)
width = 600
height = 500 
scr = pygame.display.set_mode((600,600))
global event
event = pygame.event.get()
Mpos = pygame.mouse.get_pos()
pygame.display.set_caption("Tickle-Tackle-Toenails - By Fusion (11 year old)")
#if this code was hard to make, it should be hard to understand.
#---------------------------------------------------------------------------class : Menu------------------------------------------------------------
class Menu:
    def Label(left,top,text,size,color):
        font = pygame.font.SysFont('OCR A Extended',size)
        text = font.render(text,size,color)
        scr.blit(text,(left,top))
    def Title():
        Menu.Label(130,0,"Tic-Tac-Toe (2 player)!!!",25,(0,255,255))
        pygame.display.update()
    def buttonPlay():
        if Mpos[0] > 240 and Mpos[0] < 340 and Mpos[1] > 150 and Mpos[1] < 200:
            pygame.draw.rect(scr,(0,255,0),pygame.Rect((width//2)-60,(height//2)-100,100,50))
            Menu.Label(((width//2)-60)+10,((height//2)-100)+5,"Play",35,(0,255,255))
            pygame.display.update()
            return True
        else:
            pygame.draw.rect(scr,(0,0,255),pygame.Rect((width//2)-60,(height//2)-100,100,50))
            Menu.Label(((width//2)-60)+10,((height//2)-100)+5,"Play",35,(0,255,255))
            pygame.display.update()
    def buttonExit():
        if Mpos[0] > 240 and Mpos[0] < 340 and Mpos[1] > 250 and Mpos[1] < 300:
            pygame.draw.rect(scr,(0,255,0),pygame.Rect((width//2)-60,(height//2),100,50))
            Menu.Label(((width//2)-60)+10,((height//2))+5,"Exit",35,(0,255,255))
            pygame.display.update()
            return True
        else:
            pygame.draw.rect(scr,(0,0,255),pygame.Rect((width//2)-60,(height//2),100,50))
            Menu.Label(((width//2)-60)+10,((height//2))+5,"Exit",35,(0,255,255))
            pygame.display.update()
Menu.Title()
while True:
    Mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        pass
    Menu.buttonPlay()
    if Menu.buttonPlay() == True and event.type == 5:
        break
    Menu.buttonExit()
    if Menu.buttonExit() == True and event.type == 5:
        quit()
scr.fill((0,0,0))
#------------------------------------------------------------------------class : selfGame----------------------------------------------------------
class TTT(Menu):
    positions = [(5,5),(205,5),(405,5),
                 (5,205),(205,205),(405,205),
                 (5,405),(205,405),(405,405)]
    XO = ["","","",
          "","","",
          "","",""]
    turn = "X"
    win = ""
    def makeBoard():
        pygame.draw.line(scr,(0,255,255),(200,0),(200,600),10)
        pygame.draw.line(scr,(0,255,255),(400,0),(400,600),10)

        pygame.draw.line(scr,(0,255,255),(0,200),(600,200),10)
        pygame.draw.line(scr,(0,255,255),(0,400),(600,400),10)
    def makeX(x,y):
        img = pygame.image.load('X.jpg')
        img = pygame.transform.smoothscale(img, (190,190))
        scr.blit(img,(x,y))
    def makeO(x,y):
        img = pygame.image.load('O.jpg')
        img = pygame.transform.smoothscale(img, (190,190))
        scr.blit(img,(x,y))
    def placeX():
        a = 0
        if event.type == 5:
            for i in range(4):
                if Mpos[0] > 5 and Mpos[0] < 200 and Mpos[1] > a and Mpos[1] < a+200 and TTT.XO[TTT.positions.index((5,a+5))] == "":
                    TTT.makeX(5,a+5)
                    TTT.XO[TTT.positions.index((5,a+5))] = "X"
                    pygame.display.update()
                    TTT.turn = "O"
                if Mpos[0] > 200 and Mpos[0] < 400 and Mpos[1] > a and Mpos[1] < a+200 and TTT.XO[TTT.positions.index((205,a+5))] == "":
                    TTT.makeX(205,a+5)
                    TTT.XO[TTT.positions.index((205,a+5))] = "X"
                    pygame.display.update()
                    TTT.turn = "O"
                if Mpos[0] > 400 and Mpos[0] < 600 and Mpos[1] > a and Mpos[1] < a+200 and TTT.XO[TTT.positions.index((405,a+5))] == "":
                    TTT.makeX(405,a+5)
                    TTT.XO[TTT.positions.index((405,a+5))] = "X"
                    pygame.display.update()
                    TTT.turn = "O"
                a += 200
        
    def placeO():
        a = 0
        if event.type == 5:
            for i in range(4):
                if Mpos[0] > 5 and Mpos[0] < 200 and Mpos[1] > a and Mpos[1] < a+200 and TTT.XO[TTT.positions.index((5,a+5))] == "":
                    TTT.makeO(5,a+5)
                    TTT.XO[TTT.positions.index((5,a+5))] = "O"
                    pygame.display.update()
                    TTT.turn = "X"
                if Mpos[0] > 200 and Mpos[0] < 400 and Mpos[1] > a and Mpos[1] < a+200 and TTT.XO[TTT.positions.index((205,a+5))] == "":
                    TTT.makeO(205,a+5)
                    TTT.XO[TTT.positions.index((205,a+5))] = "O"
                    pygame.display.update()
                    TTT.turn = "X"
                if Mpos[0] > 400 and Mpos[0] < 600 and Mpos[1] > a and Mpos[1] < a+200 and TTT.XO[TTT.positions.index((405,a+5))] == "":
                    TTT.makeO(405,a+5)
                    TTT.XO[TTT.positions.index((405,a+5))] = "O"
                    pygame.display.update()
                    TTT.turn = "X"
                a += 200
    def CheckWinForX():
        if TTT.XO[0] == "X" and TTT.XO[1] == "X" and TTT.XO[2] == "X":
            TTT.win = "X"
            TTT.Case1()
        if TTT.XO[3] == "X" and TTT.XO[4] == "X" and TTT.XO[5] == "X":
            TTT.win = "X"
            TTT.Case2()
        if TTT.XO[6] == "X" and TTT.XO[7] == "X" and TTT.XO[8] == "X":
            TTT.win = "X"
            TTT.Case3()
        if TTT.XO[0] == "X" and TTT.XO[3] == "X" and TTT.XO[6] == "X":
            TTT.win = "X"
            TTT.yCase1()
        if TTT.XO[1] == "X" and TTT.XO[4] == "X" and TTT.XO[7] == "X":
            TTT.win = "X"
            TTT.yCase2()
        if TTT.XO[2] == "X" and TTT.XO[5] == "X" and TTT.XO[8] == "X":
            TTT.win = "X"
            TTT.yCase3()
        if TTT.XO[0] == "X" and TTT.XO[4] == "X" and TTT.XO[8] == "X":
            TTT.win = "X"
            TTT.Case4()
        if TTT.XO[2] == "X" and TTT.XO[4] == "X" and TTT.XO[6] == "X":
            TTT.win = "X"
            TTT.Case5()
    def CheckWinForO():
        if TTT.XO[0] == "O" and TTT.XO[1] == "O" and TTT.XO[2] == "O":
            TTT.win = "O"
            TTT.Case1()
        if TTT.XO[3] == "O" and TTT.XO[4] == "O" and TTT.XO[5] == "O":
            TTT.win = "O"
            TTT.Case2()
        if TTT.XO[6] == "O" and TTT.XO[7] == "O" and TTT.XO[8] == "O":
            TTT.win = "O"
            TTT.Case3()
        if TTT.XO[0] == "O" and TTT.XO[3] == "O" and TTT.XO[6] == "O":
            TTT.win = "O"
            TTT.yCase1()
        if TTT.XO[1] == "O" and TTT.XO[4] == "O" and TTT.XO[7] == "O":
            TTT.win = "O"
            TTT.yCase2()
        if TTT.XO[2] == "O" and TTT.XO[5] == "O" and TTT.XO[8] == "O":
            TTT.win = "O"
            TTT.yCase3()
        if TTT.XO[0] == "O" and TTT.XO[4] == "O" and TTT.XO[8] == "O":
            TTT.win = "O"
            TTT.Case4()
        if TTT.XO[2] == "O" and TTT.XO[4] == "O" and TTT.XO[6] == "O":
            TTT.win = "O"
            TTT.Case5()
    def Case1():
        pygame.draw.line(scr,(255,255,0),(0,100),(600,100),15)
        pygame.display.update()
        TTT.Win()
    def Case2():
        pygame.draw.line(scr,(255,255,0),(0,300),(600,300),15)
        pygame.display.update()
        TTT.Win()
    def Case3():
        pygame.draw.line(scr,(255,255,0),(0,500),(600,500),15)
        pygame.display.update()
        TTT.Win()
    def yCase1():
        pygame.draw.line(scr,(255,255,0),(100,0),(100,600),15)
        pygame.display.update()
        TTT.Win()
    def yCase2():
        pygame.draw.line(scr,(255,255,0),(300,0),(300,600),15)
        pygame.display.update()
        TTT.Win()
    def yCase3():
        pygame.draw.line(scr,(255,255,0),(500,0),(500,600),15)
        pygame.display.update()
        TTT.Win()
    def Case4():
        pygame.draw.line(scr,(255,255,0),(0,0),(600,600),15)
        pygame.display.update()
        TTT.Win()
    def Case5():
        pygame.draw.line(scr,(255,255,0),(0,600),(600,0),15)
        pygame.display.update()
        TTT.Win()
    def Win():
        time.sleep(3)
        scr.fill((0,0,0))
        Menu.Label(10,10,TTT.win + " has won.",25,(0,255,255))
        pygame.display.update()
#----------------------------------------------------------------------------GAME------------------------------------------------------------------
time.sleep(2)
TTT.makeBoard()
pygame.display.update()
while True:
    for event in pygame.event.get():
        Mpos = pygame.mouse.get_pos()
        if TTT.turn == "X":
            TTT.placeX()
            TTT.CheckWinForX()
        else:
            TTT.placeO()
            TTT.CheckWinForO()
