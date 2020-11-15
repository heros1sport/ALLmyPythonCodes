import pygame
import time
pygame.init()
scr = pygame.display.set_mode((200,200))
global event
event = pygame.event.get()
class Board:
    def __init__(self):
        pass
    def board(self):
        x = 0
        y = 0
        for i in range(0,200,25):
            x = 0
            for j in range(0,100,25):
                pygame.draw.rect(scr,(255,255,255),pygame.Rect(x,y,25,25))
                pygame.draw.rect(scr,(0,255,0),pygame.Rect(x+25,y,25,25))
                x += 50
            x = 0
            y += 25
            for j in range(0,100,25):
                pygame.draw.rect(scr,(0,255,0),pygame.Rect(x,y,25,25))
                pygame.draw.rect(scr,(255,255,255),pygame.Rect(x+25,y,25,25))
                x += 50
            y += 25
class Mouse:
    def __init__(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
    def select(self):
        for i in range(0,200,25):
            for j in range(0,200,25):
                if self.y > i and self.y < i+25 and self.x > j and self.x < j+25:
                    pygame.draw.rect(scr,(255,0,0),pygame.Rect(j,i,25,25),2)
    
class White:
    class pawn:
        def __init__(self):
            self.pawns = [[0,150],[25,150],[50,150],[75,150],[100,150],[125,150],[150,150],[175,150]]
        def show_all(self):
            image = pygame.image.load("white_pawn.png")
            for i in self.pawns:
                scr.blit(image,(i[0],i[1]))

    class rook_left:
        def __init__(self):
            self.x = 0
            self.y = 175
            self.squares = []
        def show(self):
            image = pygame.image.load("white_rook.png")
            scr.blit(image,(self.x,self.y))            
    class rook_right:
        def __init__(self):
            self.x = 175
            self.y = 175
        def show(self):
            image = pygame.image.load("white_rook.png")
            scr.blit(image,(self.x,self.y))
    class horse_left:
        def __init__(self):
            self.x = 25
            self.y = 175
        def show(self):
            image = pygame.image.load("white_horse.png")
            scr.blit(image,(self.x,self.y))
    class horse_right:
        def __init__(self):
            self.x = 150
            self.y = 175
        def show(self):
            image = pygame.image.load("white_horse.png")
            scr.blit(image,(self.x,self.y))    
    class bishop_left:
        def __init__(self):
            self.x = 50
            self.y = 175
        def show(self):
            image = pygame.image.load("white_bishop.png")
            scr.blit(image,(self.x,self.y))
    class bishop_right:
        def __init__(self):
            self.x = 125
            self.y = 175
        def show(self):
            image = pygame.image.load("white_bishop.png")
            scr.blit(image,(self.x,self.y))
    class queen:
        def __init__(self):
            self.x = 100
            self.y = 175
        def show(self):
            image = pygame.image.load("white_queen.png")
            scr.blit(image, (self.x,self.y))
    class king:
        def __init__(self):
            self.x = 75
            self.y = 175
        def show(self):
            image = pygame.image.load("white_queen.png")
            scr.blit(image, (self.x,self.y))
board = Board()
mouse = Mouse()
white_pawns = White.pawn()
white_rookleft = White.rook_left()
white_rookright = White.rook_right()
white_horseleft = White.horse_left()
white_horseright = White.horse_right()
white_bishopleft = White.bishop_left()
white_bishopright = White.bishop_right()
white_king = White.king()
white_queen = White.queen()
while True:
    for event in pygame.event.get():
        mouse.x = pygame.mouse.get_pos()[0]
        mouse.y = pygame.mouse.get_pos()[1]
        if event.type == 5:
            #for pawns
            for i in range(len(white_pawns.pawns)):
                if mouse.x > white_pawns.pawns[i][0] and mouse.x < white_pawns.pawns[i][0]+25 and mouse.y > white_pawns.pawns[i][1] and mouse.y < white_pawns.pawns[i][1]+25:                    
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_pawns.pawns[i][0],white_pawns.pawns[i][1],25,25),5)
                    if white_pawns.pawns[i][1] == 150:
                        if [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-25] != [white_rookright.x,white_rookright.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-25] != [white_rookleft.x,white_rookleft.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-25] != [white_bishopleft.x,white_bishopleft.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-25] != [white_bishopright.x,white_bishopright.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-25] != [white_horseleft.x,white_horseleft.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-25] != [white_horseright.x,white_horseright.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-25] != [white_queen.x,white_queen.y]:
                            
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_pawns.pawns[i][0],white_pawns.pawns[i][1]-25,25,25),2)
                        if [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-50] != [white_rookright.x,white_rookright.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-50] != [white_rookleft.x,white_rookleft.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-50] != [white_bishopleft.x,white_bishopleft.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-50] != [white_bishopright.x,white_bishopright.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-50] != [white_horseleft.x,white_horseleft.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-50] != [white_horseright.x,white_horseright.y] or [white_pawns.pawns[i][0],white_pawns.pawns[i][1]-50] != [white_queen.x,white_queen.y]:
        
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_pawns.pawns[i][0],white_pawns.pawns[i][1]-50,25,25),2)
                    time.sleep(0.5)
                    pygame.display.update()
                    finished = False
                    while not finished:
                        for event in pygame.event.get():
                            mouse.x = pygame.mouse.get_pos()[0]
                            mouse.y = pygame.mouse.get_pos()[1]    
                        if event.type == 5:
                            if mouse.x > white_pawns.pawns[i][0] and mouse.x < white_pawns.pawns[i][0]+25 and mouse.y > white_pawns.pawns[i][1]-25 and mouse.y < white_pawns.pawns[i][1]:
                                white_pawns.pawns[i][1] -= 25
                                finished = True
                            if mouse.x > white_pawns.pawns[i][0] and mouse.x < white_pawns.pawns[i][0]+25 and mouse.y > white_pawns.pawns[i][1]-50 and mouse.y < white_pawns.pawns[i][1]-25:
                                white_pawns.pawns[i][1] -= 50
                                finished = True
                            finished = True
            #for rooks
            if mouse.x > white_rookleft.x and mouse.x < white_rookleft.x + 25 and mouse.y > white_rookleft.y and mouse.y < white_rookleft.y+25:
                pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_rookleft.x,white_rookleft.y,25,25),5)
                j = 0
                squares = []
                Blocked = False
                x = white_rookleft.x
                y = white_rookleft.y
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x,y-j]:
                        Blocked = True
                        break
                    if y-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x,y-j,25,25),2)
                    squares.append([x,y-j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x,y+j]:
                        Blocked = True
                        break
                    if y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x,y+j,25,25),2)
                    squares.append([x,y+j])
                    j += 25
                
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x+j,y]:
                        Blocked = True
                        break
                    if x+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y,25,25),2)
                    squares.append([x+j,y])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x-j,y]:
                        Blocked = True
                        break
                    if x-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y,25,25),2)
                    squares.append([x-j,y])
                    j += 25
                time.sleep(0.5)
                pygame.display.update()
                finished = False
                while not finished:
                    for event in pygame.event.get():
                        mouse.x = pygame.mouse.get_pos()[0]
                        mouse.y = pygame.mouse.get_pos()[1]
                    if event.type == 5:
                        for i in squares:
                            if mouse.x > i[0] and mouse.x < i[0]+25 and mouse.y > i[1] and mouse.y < i[1]+25:
                                white_rookleft.x = i[0]
                                white_rookleft.y = i[1]
                        break
            if mouse.x > white_rookright.x and mouse.x < white_rookright.x + 25 and mouse.y > white_rookright.y and mouse.y < white_rookright.y+25:
                pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_rookright.x,white_rookright.y,25,25),5)
                j = 0
                squares = []
                Blocked = False
                x = white_rookright.x
                y = white_rookright.y
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x,y-j]:
                        Blocked = True
                        break
                    if y-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x,y-j,25,25),2)
                    squares.append([x,y-j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x,y+j]:
                        Blocked = True
                        break
                    if y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x,y+j,25,25),2)
                    squares.append([x,y+j])
                    j += 25
                
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x+j,y]:
                        Blocked = True
                        break
                    if x+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y,25,25),2)
                    squares.append([x+j,y])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x-j,y]:
                        Blocked = True
                        break
                    if x-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y,25,25),2)
                    squares.append([x-j,y])
                    j += 25
                time.sleep(0.5)
                pygame.display.update()
                finished = False
                while not finished:
                    for event in pygame.event.get():
                        mouse.x = pygame.mouse.get_pos()[0]
                        mouse.y = pygame.mouse.get_pos()[1]
                    if event.type == 5:
                        for i in squares:
                            if mouse.x > i[0] and mouse.x < i[0]+25 and mouse.y > i[1] and mouse.y < i[1]+25:
                                white_rookright.x = i[0]
                                white_rookright.y = i[1]
                        break
            #for horses
            if mouse.x > white_horseleft.x and mouse.x < white_horseleft.x + 25 and mouse.y > white_horseleft.y and mouse.y < white_horseleft.y+25 and event.type == 5:
                pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x,white_horseleft.y,25,25),5)
                squares = []
                x = 25
                y = 50
                val = [int(white_horseleft.x) + int(x),int(white_horseleft.y) - int(y)]
                ne = False
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseright.x,white_horseright.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x+x,white_horseleft.y-y,25,25),2)
                            squares.append(val)
                    
                x = -25
                y = 50
                val = [int(white_horseleft.x) + int(x),int(white_horseleft.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseright.x,white_horseright.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x+x,white_horseleft.y-y,25,25),2)
                            squares.append(val)
                x = 50
                y = 25
                val = [int(white_horseleft.x) + int(x),int(white_horseleft.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseright.x,white_horseright.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x+x,white_horseleft.y-y,25,25),2)
                            squares.append(val)
                    
                    
                x = -50
                y = 25
                val = [int(white_horseleft.x) + int(x),int(white_horseleft.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseright.x,white_horseright.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x+x,white_horseleft.y-y,25,25),2)
                            squares.append(val)
                y = -25
                val = [int(white_horseleft.x) + int(x),int(white_horseleft.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseright.x,white_horseright.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x+x,white_horseleft.y-y,25,25),2)
                            squares.append(val)
                x = 50
                y = -25
                val = [int(white_horseleft.x) + int(x),int(white_horseleft.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseright.x,white_horseright.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x+x,white_horseleft.y-y,25,25),2)
                            squares.append(val)
                y = -50
                x = -25
                val = [int(white_horseleft.x) + int(x),int(white_horseleft.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseright.x,white_horseright.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x+x,white_horseleft.y-y,25,25),2)
                            squares.append(val)
                x = 25
                val = [int(white_horseleft.x) + int(x),int(white_horseleft.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseright.x,white_horseright.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseleft.x+x,white_horseleft.y-y,25,25),2)
                            squares.append(val)
                    
                pygame.display.update()
                time.sleep(0.7)
                finished = False
                while not finished:
                    for event in pygame.event.get():
                        mouse.x = pygame.mouse.get_pos()[0]
                        mouse.y = pygame.mouse.get_pos()[1]
                    if event.type == 5:
                        for i in squares:
                            if mouse.x > i[0] and mouse.x < i[0]+25 and mouse.y > i[1] and mouse.y < i[1]+25:
                                white_horseleft.x = i[0]
                                white_horseleft.y = i[1]
                        break
                        
            if mouse.x > white_horseright.x and mouse.x < white_horseright.x + 25 and mouse.y > white_horseright.y and mouse.y < white_horseright.y+25 and event.type == 5:
                pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x,white_horseright.y,25,25),5)
                squares = []
                x = 25
                y = 50
                val = [int(white_horseright.x) + int(x),int(white_horseright.y) - int(y)]
                ne = False
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseleft.x,white_horseleft.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x+x,white_horseright.y-y,25,25),2)
                            squares.append(val)
                    
                x = -25
                y = 50
                val = [int(white_horseright.x) + int(x),int(white_horseright.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseleft.x,white_horseleft.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x+x,white_horseright.y-y,25,25),2)
                            squares.append(val)
                x = 50
                y = 25
                val = [int(white_horseright.x) + int(x),int(white_horseright.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseleft.x,white_horseleft.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x+x,white_horseright.y-y,25,25),2)
                            squares.append(val)
                    
                    
                x = -50
                y = 25
                val = [int(white_horseright.x) + int(x),int(white_horseright.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseleft.x,white_horseleft.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x+x,white_horseright.y-y,25,25),2)
                            squares.append(val)
                y = -25
                val = [int(white_horseright.x) + int(x),int(white_horseright.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseleft.x,white_horseleft.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x+x,white_horseright.y-y,25,25),2)
                            squares.append(val)
                x = 50
                y = -25
                val = [int(white_horseright.x) + int(x),int(white_horseright.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseleft.x,white_horseleft.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x+x,white_horseright.y-y,25,25),2)
                            squares.append(val)
                y = -50
                x = -25
                val = [int(white_horseright.x) + int(x),int(white_horseright.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseleft.x,white_horseleft.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x+x,white_horseright.y-y,25,25),2)
                            squares.append(val)
                x = 25
                val = [int(white_horseright.x) + int(x),int(white_horseright.y) - int(y)]
                if val != [white_rookleft.x,white_rookleft.y] and val != [white_rookright.x,white_rookright.y] and val != [white_bishopleft.x,white_bishopleft.y] and val != [white_bishopright.x,white_bishopright.y] and val != [white_horseleft.x,white_horseleft.y] and val != [white_queen.x,white_queen.y]:
                    if val[0] >= 0 and val[0] <= 200 and val[1] >= 0 and val[1] <= 200:
                        ne = False
                        for i in white_pawns.pawns:
                            if val == [i[0],i[1]]:
                                ne = True
                        if ne == False:
                            pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_horseright.x+x,white_horseright.y-y,25,25),2)
                            squares.append(val)
                    
                pygame.display.update()
                time.sleep(0.7)
                finished = False
                while not finished:
                    for event in pygame.event.get():
                        mouse.x = pygame.mouse.get_pos()[0]
                        mouse.y = pygame.mouse.get_pos()[1]
                    if event.type == 5:
                        for i in squares:
                            if mouse.x > i[0] and mouse.x < i[0]+25 and mouse.y > i[1] and mouse.y < i[1]+25:
                                white_horseright.x = i[0]
                                white_horseright.y = i[1]
                        break
            #for bishop
            if mouse.x > white_bishopleft.x and mouse.x < white_bishopleft.x + 25 and mouse.y > white_bishopleft.y and mouse.y < white_bishopleft.y+25 and event.type == 5:
                pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_bishopleft.x,white_bishopleft.y,25,25),5)
                j = 0
                squares = []
                Blocked = False
                x = white_bishopleft.x
                y = white_bishopleft.y
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if y-j < 0 or x-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y-j,25,25),2)
                    squares.append([x-j,y-j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if y-j < 0 or x+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y-j,25,25),2)
                    squares.append([x+j,y-j])
                    j += 25
                
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if x+j > 200 or y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y+j,25,25),2)
                    squares.append([x+j,y+j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if x-j < 0 or y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y+j,25,25),2)
                    squares.append([x-j,y+j])
                    j += 25
                time.sleep(0.5)
                pygame.display.update()
                finished = False
                while not finished:
                    for event in pygame.event.get():
                        mouse.x = pygame.mouse.get_pos()[0]
                        mouse.y = pygame.mouse.get_pos()[1]
                    if event.type == 5:
                        for i in squares:
                            if mouse.x > i[0] and mouse.x < i[0]+25 and mouse.y > i[1] and mouse.y < i[1]+25:
                                white_bishopleft.x = i[0]
                                white_bishopleft.y = i[1]
                        break
            if mouse.x > white_bishopright.x and mouse.x < white_bishopright.x + 25 and mouse.y > white_bishopright.y and mouse.y < white_bishopright.y+25 and event.type == 5:
                pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_bishopright.x,white_bishopright.y,25,25),5)
                j = 0
                squares = []
                Blocked = False
                x = white_bishopright.x
                y = white_bishopright.y
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if y-j < 0 or x-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y-j,25,25),2)
                    squares.append([x-j,y-j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if y-j < 0 or x+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y-j,25,25),2)
                    squares.append([x+j,y-j])
                    j += 25
                
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if x+j > 200 or y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y+j,25,25),2)
                    squares.append([x+j,y+j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_queen.x,white_queen.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if x-j < 0 or y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y+j,25,25),2)
                    squares.append([x-j,y+j])
                    j += 25
                time.sleep(0.5)
                pygame.display.update()
                finished = False
                while not finished:
                    for event in pygame.event.get():
                        mouse.x = pygame.mouse.get_pos()[0]
                        mouse.y = pygame.mouse.get_pos()[1]
                    if event.type == 5:
                        for i in squares:
                            if mouse.x > i[0] and mouse.x < i[0]+25 and mouse.y > i[1] and mouse.y < i[1]+25:
                                white_bishopright.x = i[0]
                                white_bishopright.y = i[1]
                        break
            if mouse.x > white_queen.x and mouse.x < white_queen.x+25 and mouse.y > white_queen.y and mouse.y < white_queen.y+25:
                pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_queen.x,white_queen.y,25,25),5)
                j = 0
                squares = []
                Blocked = False
                x = white_queen.x
                y = white_queen.y
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_rookright.x,white_rookright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if y-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x,y-j,25,25),2)
                    squares.append([x,y-j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_rookright.x,white_rookright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x,y+j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x,y+j]:
                        Blocked = True
                        break
                    if y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x,y+j,25,25),2)
                    squares.append([x,y+j])
                    j += 25
                
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_rookright.x,white_rookright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x+j,y]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x+j,y]:
                        Blocked = True
                        break
                    if x+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y,25,25),2)
                    squares.append([x+j,y])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_rookright.x,white_rookright.y] == [x,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x-j,y]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y]:
                        Blocked = True
                        break
                    if x-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y,25,25),2)
                    squares.append([x-j,y])
                    j += 25
                j = 0
                Blocked = False
                x = white_queen.x
                y = white_queen.y
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if y-j < 0 or x-j < 0:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y-j,25,25),2)
                    squares.append([x-j,y-j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y-j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x+j,y-j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if y-j < 0 or x+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y-j,25,25),2)
                    squares.append([x+j,y-j])
                    j += 25
                
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x+j == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x+j,y+j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if x+j > 200 or y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x+j,y+j,25,25),2)
                    squares.append([x+j,y+j])
                    j += 25
                j = 25
                Blocked = False
                while not Blocked:
                    for i in white_pawns.pawns:
                        if x-j == i[0] and y+j == i[1]:
                            Blocked = True
                            break
                    if Blocked == True:
                        break
                    if [white_rookright.x,white_rookright.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_horseleft.x,white_horseleft.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_horseright.x,white_horseright.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_rookleft.x,white_rookleft.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_bishopleft.x,white_bishopleft.y] == [x-j,y+j]:
                        Blocked = True
                        break
                    if [white_bishopright.x,white_bishopright.y] == [x-j,y-j]:
                        Blocked = True
                        break
                    if x-j < 0 or y+j > 200:
                        Blocked = True
                        break
                    pygame.draw.rect(scr,(0,0,255),pygame.Rect(x-j,y+j,25,25),2)
                    squares.append([x-j,y+j])
                    j += 25
                time.sleep(0.5)
                pygame.display.update()
                finished = False
                while not finished:
                    for event in pygame.event.get():
                        mouse.x = pygame.mouse.get_pos()[0]
                        mouse.y = pygame.mouse.get_pos()[1]
                    if event.type == 5:
                        for i in squares:
                            if mouse.x > i[0] and mouse.x < i[0]+25 and mouse.y > i[1] and mouse.y < i[1]+25:
                                white_queen.x = i[0]
                                white_queen.y = i[1]
                        break
            
            if mouse.x > white_king.x and mouse.x < white_king.x+25 and mouse.y > white_king.y and mouse.y < white_king.y+25:    
                pygame.draw.rect(scr,(0,0,255),pygame.Rect(white_king.x,white_king.y,25,25),5)
                                    
                    
                                
    board.board()
    white_pawns.show_all()
    white_rookleft.show()
    white_rookright.show()
    white_horseleft.show()
    white_horseright.show()
    white_bishopleft.show()
    white_bishopright.show()
    white_queen.show()
    white_king.show()
    mouse.select()
    pygame.display.update()
