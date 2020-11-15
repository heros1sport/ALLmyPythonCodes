from Fusion import *
import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((600,500))
screen.fill((255,255,255))
pygame.display.update()
class Menu:
    def __init__(self,Menu_State):
        Menu.Menu_State = True
    def Title():
        font_title = pygame.font.SysFont('italic',45)
        a = font_title.render("Racing Game",10,(255,0,0))
        screen.blit(a,(200,50))
        pygame.display.update()
    def Play_button():
        font = pygame.font.SysFont('italic',45)
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(50,250,100,50))
        Mpos = pygame.mouse.get_pos()
        if Mpos[0] > 50 and Mpos[0] < 150 and Mpos[1] > 250 and Mpos[1] < 300:
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(50,250,100,50))
            if event.type == 5:
                screen.fill((255,255,255))
                pygame.display.update()
                pygame.draw.rect(screen,(0,255,0),pygame.Rect(450,250,100,50))
                font2 = pygame.font.SysFont('italic',45)
                a2 = font2.render("Quit",20,(0,0,255))
                screen.blit(a2,(467,260))
                Menu.Title()
                
                pygame.draw.rect(screen,(255,0,0),pygame.Rect(65,262,70,23))
                a = font.render("Play",20,(0,0,255))
                screen.blit(a,(67,260))
                pygame.display.update()
                time.sleep(1)
                pygame.draw.rect(screen,(255,0,0),pygame.Rect(50,250,100,50))
                a = font.render("Play",45,(0,0,255))
                screen.blit(a,(67,260))
                
        a = font.render("Play",45,(0,0,255))
        screen.blit(a,(67,260))
        pygame.display.update()
    def Quit_button():
        font2 = pygame.font.SysFont('italic',45)
        a2 = font2.render("Quit",45,(0,0,255))
        Mpos2 = pygame.mouse.get_pos()
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(450,250,100,50))
        if Mpos2[0] > 450 and Mpos2[0] < 550 and Mpos2[1] > 250 and Mpos2[1] < 300:
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(450,250,100,50))
            if event.type == 5:
                screen.fill((255,255,255))
                pygame.display.update()
                pygame.draw.rect(screen,(255,0,0),pygame.Rect(465,262,70,23))
                Menu.Play_button()
                Menu.Title()
                a2 = font2.render("Quit",20,(0,0,255))
                screen.blit(a2,(467,260))
                pygame.display.update()
                time.sleep(1)
                pygame.draw.rect(screen,(255,0,0),pygame.Rect(450,250,100,50))
                a2 = font2.render("Quit",45,(0,0,255))
                screen.blit(a2,(467,260))
                quit()
        if Mpos2[0] > 50 and Mpos2[0] < 150 and Mpos2[1] > 250 and Mpos2[1] < 300:
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(450,250,100,50))
        screen.blit(a2,(467,260))
        pygame.display.update()
Menu.Title()
Menu.Play_button()
bah = 0
while True:
    
    for event in pygame.event.get():
        Mpos = pygame.mouse.get_pos()
        Mpos2 = pygame.mouse.get_pos()
        if Mpos[0] > 50 and Mpos[0] < 150 and Mpos[1] > 250 and Mpos[1] < 300:
            Menu.Play_button()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bah = 1
                break
        if Mpos2[0] > 50 and Mpos2[0] < 150 and Mpos2[1] > 250 and Mpos2[1] < 300:
            Menu.Quit_button()
    Menu.Title()
    Menu.Play_button()
    Menu.Quit_button()
    pygame.display.update()
    if bah == 1:
        break
Main_Game = True
screen.fill((255,255,255))
font = pygame.font.SysFont('italic',75)
a = font.render("1",45,(255,0,0))
screen.blit(a,(265,250))
pygame.display.update()
time.sleep(1)
screen.fill((255,255,255))
font = pygame.font.SysFont('italic',75)
a = font.render("2",45,(255,0,0))
screen.blit(a,(265,250))
pygame.display.update()
time.sleep(1)
screen.fill((255,255,255))
font = pygame.font.SysFont('italic',75)
a = font.render("3",45,(255,0,0))
screen.blit(a,(265,250))
pygame.display.update()
time.sleep(1)
screen.fill((255,255,255))
RaceCar = pygame.image.load('Racing Car.jpg')
RaceCar = pygame.transform.smoothscale(RaceCar,(100,100))
x = 300
y = 400
x2 = random.randint(1,600)
y2 = 0
x3 = random.randint(1,600)
y3 = 0
x4 = random.randint(1,600)
y4 = 0
clock = pygame.time.Clock()
screen.blit(RaceCar,(x,y))
pygame.display.update()
font = pygame.font.SysFont('italic',25)
score = 1
while Main_Game:
    y2 = 0
    y3 = 0
    y4 = 0
    x2 = random.randint(1,500)
    x3 = random.randint(1,500)
    x4 = random.randint(1,500)
    while y2 != 600:
        score += 1
        a = font.render("score : " + str(score),10,(0,255,0))
        screen.blit(a,(1,1))
        for event in pygame.event.get():
            keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_RIGHT]:
            x += 1
        if keyPressed[pygame.K_LEFT]:
            x -= 1

        y2 += 1
        y3 += 1
        y4 += 1
        if x2 <= x and (x2+50) >= x and (y2+50) == y or x2 <= (x + 100) and (x2+100) >= (x + 100) and (y2+50)== y:
            Fusion.playSound("C:/Users/Guest/Desktop/python projects and pygame games/clear.wav")
            screen.fill((255,255,255))
            pygame.display.update()
            Main_Game = False
        if x3 <= x and (x3+50) >= x and (y3+50) == y or x3 <= (x + 100) and (x3+100) >= (x + 100) and (y3+50)== y:
            Fusion.playSound("C:/Users/Guest/Desktop/python projects and pygame games/clear.wav")
            screen.fill((255,255,255))
            pygame.display.update()
            Main_Game = False
        if x4 <= x and (x4+50) >= x and (y4+50) == y or x4 <= (x + 100) and (x4+100) >= (x + 100) and (y4+50)== y:
            Fusion.playSound("C:/Users/Guest/Desktop/python projects and pygame games/clear.wav")
            screen.fill((255,255,255))
            pygame.display.update()
            Main_Game = False                
        screen.blit(RaceCar,(x,y))    
        pygame.draw.rect(screen,(0,0,255),pygame.Rect(x2,y2,50,50))
        pygame.draw.rect(screen,(0,0,255),pygame.Rect(x3,y3,50,50))
        pygame.draw.rect(screen,(0,0,255),pygame.Rect(x4,y4,50,50))
        pygame.display.update()
        screen.fill((255,255,255))
        clock.tick(200)
    screen.blit(RaceCar,(x,y))    
    pygame.display.update()
    clock.tick(200)
screen.fill((255,255,255))
pygame.display.update()
font_title = pygame.font.SysFont('italic',45)
a = font_title.render("Oh no! YOU HAVE CRASHED",10,(0,0,255))
screen.blit(a,(75,50))
pygame.display.update()
time.sleep(1)
screen.fill((255,255,255))
pygame.display.update()
a = font_title.render("Your score : " + str(score),10,(0,0,255))
screen.blit(a,(75,50))
pygame.display.update()
time.sleep(3)
