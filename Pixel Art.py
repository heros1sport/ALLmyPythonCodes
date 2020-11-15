import time
import pygame
import ast
pygame.init()
scr = pygame.display.set_mode((700,600))
pygame.display.set_caption("Pixel Art - Squares of Imagination - by Fusion ( 11 yr old )")
global Mpos
Mpos = pygame.mouse.get_pos()
global event
for event in pygame.event.get():
    pass
global key
key = pygame.key.get_pressed()
gr = False
# IF THIS CODE WAS PRETTY FREAKIN' HARD TO WRITE, IT SHOULD BE HELLA HARD TO UNDERSTAND.
#--------------------------------------------------------------------------class : self-------------------------------------------------------------
class self:
    color = [0,0,0]
    boxes = []
    gridpos = []
    no = 0
    FileOpened = False
    FileName = ''
    def init():
        for i in range(0,600,20):
            for j in range(0,600,20):
                self.gridpos.append([i,j])
    def grid():
        for i in range(0,600,20):
            pygame.draw.line(scr,(255,255,255),(i,0),(i,600))
        for j in range(0,600,20):
            pygame.draw.line(scr,(255,255,255),(0,j),(600,j))
    def colorRect():
        pygame.draw.rect(scr,(255,255,255),pygame.Rect(600,200,100,100),5)
        pygame.draw.rect(scr,(self.color[0],self.color[1],self.color[2]),pygame.Rect(600,200,100,100))
    def nextcolor():
        self.no += 1
    def prevcolor():
        self.no -= 1
    def setColor():
        if self.no > 15:
            self.no = 0
        if self.no == 1:
            self.color = [255,0,0]
        if self.no == 2:
            self.color = [0,255,0]
        if self.no == 3:
            self.color = [0,0,255]
        if self.no == 4:
            self.color = [255,255,0]
        if self.no == 5:
            self.color = [0,255,255]
        if self.no == 6:
            self.color = [255,0,255]
        if self.no == 7:
            self.color = [255,128,0]
        if self.no == 8:
            self.color = [255,255,255]
        if self.no == 9:
            self.color = [255,229,204]
        if self.no == 10:
            self.color = [204,0,102]
        if self.no == 11:
            self.color = [51,102,0]
        if self.no == 12:
            self.color = [96,96,96]
        if self.no == 13:
            self.color = [220,20,60]
        if self.no == 14:
            self.color = [34,139,34]
        if self.no == 15:
            self.color = [0,139,139]
    def showImg():
        if self.boxes != []:
            for i in self.boxes:
                pygame.draw.rect(scr,i[1],pygame.Rect(i[0][0],i[0][1],20,20))
    def select():
        global event
        gr = False
        for event in pygame.event.get():
            pass
        for i in range(len(self.gridpos)):
            if Mpos[0] >= self.gridpos[i][0] and Mpos[0] <= self.gridpos[i][0]+20 and Mpos[1] > self.gridpos[i][1] and Mpos[1] < self.gridpos[i][1] + 20:
                pygame.draw.rect(scr,(self.color[0],self.color[1],self.color[2]),pygame.Rect(self.gridpos[i][0],self.gridpos[i][1],20,20))
                for event in pygame.event.get():
                    if event.type == 6 and event.button == 4:
                        self.nextcolor()
                        self.setColor()
                        time.sleep(0.23)
                    if event.type == 6 and event.button == 5:
                        self.prevcolor()
                        self.setColor()
                        time.sleep(0.23)
                if pygame.mouse.get_pressed() == (0,1,0):
                    self.File.MakeFile()
                if pygame.mouse.get_pressed() == (0,0,1):
                    self.File.OpenFile()
                if key[pygame.K_u]:
                    try:
                        del self.boxes[-1]
                        time.sleep(0.3)
                    except:
                        pass
                if pygame.mouse.get_pressed() == (1,0,0):
                    gr = False
                    for a in self.boxes:
                        if a == [[self.gridpos[i][0],self.gridpos[i][1]],(self.color[0],self.color[1],self.color[2])]:
                            gr = True
                    if gr == False:
                        self.boxes.append([[self.gridpos[i][0],self.gridpos[i][1]],(self.color[0],self.color[1],self.color[2])])
                        if self.FileOpened == True:
                            self.File.ModifyFile()
                    time.sleep(0.03)
    class File:
        def MakeFile():
            a = input("Your Project's name (NOTE : This Project will be saved in the form of a text file with the name you are going to choose and in the same directory) : ")
            try:
                f = open(a + ".txt",'x')
            except FileExistsError:
                print("A text file with the same name is in the same directory in which this project was going to be saved")
            f.close()
        def OpenFile():
            a = input(" FILE NAME : ")
            f = open(a + ".txt",'rt')
            self.FileOpened = True
            self.FileName = a + ".txt"
            a = f.read()
            try:
                b = ast.literal_eval(a)
            except SyntaxError:
                b = []
            self.boxes = b
            f.close()
        def ModifyFile():
            try:
                f = open(self.FileName,'w')
                f.write(str(self.boxes))
            except FileExistsError:
                pass
        
    
                            
                             
                
        
#--------------------------------------------------------------------------GAME---------------------------------------------------------------------                           
self.init()
pygame.display.update()
while True:
    for event in pygame.event.get():
        Mpos = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()
    scr.fill((0,0,0))
    if key[pygame.K_s]:
        pass
    else:
        self.grid()
    
    self.colorRect()
    self.showImg()
    pygame.draw.line(scr,(255,255,255),(600,0),(600,600),5)
    self.select()
    pygame.display.update()
#-----------------------------------------------------------------------THE END----------------------------------------------------------------------
# copyright Pixel Art! all rights reserved ! Maybe ! Maybe not ! Ok, fine not reserved !
# Wait you thought that was the end? you're learning.





# Fusion.co has loads of fun games and projects for you to discover:
#
#
#
#
#
#
#
#                               * EMPTY *
#
#
#
#
#
#
#
#
#
#
# Damn, so many games i forgot

















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# What????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? YOU WANA FIGHT ME???????????

