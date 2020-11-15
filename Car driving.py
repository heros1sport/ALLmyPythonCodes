import pygame
import time
import math
pygame.init()
scr = pygame.display.set_mode((1000,600))

class Car:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.vel = 0
        self.angle = 0
    def show(self):
        pygame.draw.rect(scr,(255,0,0),pygame.Rect(self.x,self.y,25,25))
    def right(self):
        self.angle += 5
    def left(self):
        self.angle -= 5
    def forward(self):
        if self.vel < 15:
            self.vel += 1
    def backward(self):
        if self.vel > -15:
            self.vel -= 1
car = Car()
while True:
    scr.fill((0,0,0))
    for event in pygame.event.get():
        pass
    keyPressed = pygame.key.get_pressed()
    car.show()
    if keyPressed[pygame.K_UP]:
        car.forward()
        if keyPressed[pygame.K_RIGHT]:
            car.right()
        if keyPressed[pygame.K_LEFT]:
            car.left()
    else:
        if car.vel > 0:
            car.vel -= 1
    if keyPressed[pygame.K_DOWN]:
        car.backward()
        if keyPressed[pygame.K_RIGHT]:
            car.right()
        if keyPressed[pygame.K_LEFT]:
            car.left()
    else:
        if car.vel < 0:
            car.vel += 1
    if car.x <= 0 or car.x+25 >= 1000 or car.y <= 0 or car.y+25 >= 600:
        car.vel -= car.vel + car.vel
        car.x = car.x + car.vel * math.cos(math.radians(car.angle))
        car.y = car.y + car.vel * math.sin(math.radians(car.angle))
    car.x = car.x + car.vel * math.cos(math.radians(car.angle))
    car.y = car.y + car.vel * math.sin(math.radians(car.angle))
    if car.angle > 360:
        car.angle -= 360
    if car.angle < 0:
        car.angle += 360
    pygame.display.update()
    time.sleep(0.03)
