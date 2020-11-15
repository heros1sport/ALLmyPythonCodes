import pygame
import time
import os
import random
from Fusion import *
pygame.init()
screen = pygame.display.set_mode((200,100))
screen.fill((255,255,255))
pygame.display.update()
font = pygame.font.SysFont('Courier New',25)
text = ""
mousePos = ()
try:
    Fusion.makeLocalStorageVariable('Calender Alarms','Smart Watch.py',"")
except FileExistsError:
    print(None)
try:
    Fusion.makeLocalStorageVariable('Calender Alarm Name','Smart Watch.py',"")
except FileExistsError:
    print(None)

class Watch:
    state = 1
    def Buttons():
        pygame.draw.rect(screen,(0,0,255),pygame.Rect(0,25,20,50))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(180,25,20,50))
        pygame.display.update()
    def ClickButton():
        if mousePos[0] < 20 and mousePos[0] > 0 and event.type == pygame.MOUSEBUTTONDOWN:
            Watch.state -= 1
            if Watch.state < 0:
                Watch.state = 3
            
        if mousePos[0] < 200 and mousePos[0] > 180 and event.type == pygame.MOUSEBUTTONDOWN:
            Watch.state += 1
            if Watch.state > 4:
                Watch.state = 0
while True:
    if Watch.state == 1:
        font = pygame.font.SysFont('Courier New',25)
        text = font.render(Fusion.getTimeHours() + ":" + Fusion.getTimeMinutes() + ":" + Fusion.getTimeSec(),15,(0,255,0))
        screen.blit(text,(20,40))
        Watch.Buttons()
        pygame.display.update()
    if Watch.state == 2:
        font = pygame.font.SysFont('Courier New',25)
        text = font.render(Fusion.getTimeWeekDay() + " " + Fusion.getTimeDate() + " " + Fusion.getTimeMonth(),15,(0,255,0))
        screen.fill((255,255,255))
        screen.blit(text,(25,40))
        Watch.Buttons()
        pygame.display.update()
    if Watch.state == 3:
        font = pygame.font.SysFont('Courier New',15)
        text = font.render("set alarm mode",9,(0,255,0))
        screen.fill((255,255,255))
        screen.blit(text,(25,40))
        Watch.Buttons()
        pygame.display.update()
        Fusion.waitSeconds(2)
        font = pygame.font.SysFont('Courier New',13)
        text = font.render("press enter to exit",7,(0,255,0))
        screen.fill((255,255,255))
        screen.blit(text,(20,40))
        Watch.Buttons()
        pygame.display.update()
        a = input("Enter time here ((Day of the week) (Month) (Date) (Year))")
        if a == "":
            Watch.state += 1
        b = input("Alarm Name: ")
        f = open("C:/Users/Guest/Desktop/Smart Watch.py's Local Variables/variable-name Calender Alarms.txt",'w')
        f.write(b)
        f.close()
        f = open("C:/Users/Guest/Desktop/Smart Watch.py's Local Variables/variable-name Calender Alarms.txt",'w')
        f.write(a)
        f.close()
        pygame.display.update()
        Watch.state += 1
    if Watch.state == 4:
        font = pygame.font.SysFont('Courier New',15)
        text = font.render("Alarms Inbox",9,(0,255,0))
        screen.fill((255,255,255))
        screen.blit(text,(25,40))
        Watch.Buttons()
        pygame.display.update()
        Fusion.waitSeconds(2)
        font = pygame.font.SysFont('Courier New',15)
        text = font.render("Alarm: " + Fusion.getLocalStorageVariable('Calender Alarm Name','Smart Watch.py'),9,(0,255,0))
        screen.fill((255,255,255))
        screen.blit(text,(25,40))
        Watch.Buttons()
        pygame.display.update()
        Fusion.waitSeconds(2)
        font = pygame.font.SysFont('Courier New',15)
        if Fusion.getTimeWeekDay() + " " + Fusion.getTimeMonth() + " " + Fusion.getTimeDate() + " " + Fusion.getTimeYear() == Fusion.getLocalStorageVariable('Calendar Alarms','Smart Watch.py'):
            font = pygame.font.SysFont('Courier New',15)
            text = font.render("Alarm Today:Yes",9,(0,255,0))
            screen.fill((255,255,255))
            screen.blit(text,(25,40))
            Watch.Buttons()
            pygame.display.update()
            Fusion.waitSeconds(2)
        else:
            font = pygame.font.SysFont('Courier New',15)
            text = font.render("Alarm Today:No",9,(0,255,0))
            screen.fill((255,255,255))
            screen.blit(text,(25,40))
            Watch.Buttons()
            pygame.display.update()
            Fusion.waitSeconds(2)
            Watch.state += 1
        text = font.render("",9,(0,255,0))
        screen.fill((255,255,255))
        screen.blit(text,(25,40))
        Watch.Buttons()
        pygame.display.update()
        Fusion.waitSeconds(2)
    for event in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        Watch.ClickButton()
    screen.fill((255,255,255))

