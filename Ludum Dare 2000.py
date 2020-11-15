import random
import math
import time
import pygame
pygame.init()
scr = pygame.display.set_mode((700,700))
enemies = []
#music = pygame.mixer.music.load('ENERGETIC CHIPTUNE Thermal - Evan King.mp3')
#pygame.mixer.music.play(-1)
hit = []
class Player:
    def __init__(self):
        self.x = 275
        self.y = 275
        self.image = pygame.image.load('player.jpg')
        self.image1 = pygame.image.load('hearts.png')
        self.lives = 5
    def draw(self):
        scr.blit(self.image,(self.x,self.y))
    def rotate(self, x, y):
        oppos = math.fabs(y - self.y)
        adjac = math.fabs(x - self.x)
        hypot = math.hypot(oppos,adjac)
        sin = oppos/hypot
        radians = math.asin(sin)
        angle = radians * (180/3.14)
        if x > self.x:            
            if y > self.y:
                angle -= angle + angle
        if x < self.x:
            angle = 180 + (angle - (angle + angle))
            if y > self.y:
                angle -= angle + angle
        return angle - 90
class Bullet:
    def __init__(self, color):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.color = color
    def draw(self):
        pygame.draw.rect(scr,self.color,pygame.Rect(self.x,self.y,5,5))
class Gun:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bullets = []
        self.bullets2 = []
    def shoot1(self,x,y,angle):
        self.bullets.append(Bullet((0,255,255)))
        self.bullets[-1].x = x
        self.bullets[-1].y = y
        self.bullets[-1].angle = angle
    def shoot2(self,x,y,angle):
        self.bullets2.append(Bullet((255,255,0)))
        self.bullets2[-1].x = x
        self.bullets2[-1].y = y
        self.bullets2[-1].angle = angle
class Enemy:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 2
        self.hearts = 3
        self.image = pygame.image.load('enemy.png')
    def draw(self):
        scr.blit(self.image,(self.x,self.y))
    def rotate(self, x, y):
        oppos = math.fabs(y - self.y)
        adjac = math.fabs(x - self.x)
        hypot = math.hypot(oppos,adjac)
        sin = oppos/hypot
        radians = math.asin(sin)
        angle = radians * (180/3.14)
        if x > self.x:            
            if y > self.y:
                angle -= angle + angle
        if x < self.x:
            angle = 180 + (angle - (angle + angle))
            if y > self.y:
                angle -= angle + angle
        return angle - 90
    def distance(self,x,y):
        oppos = math.fabs(y - self.y)
        adjac = math.fabs(x - self.x)
        hypot = math.hypot(oppos,adjac)
        return hypot
    def spawn(self):
        enemies.append(Enemy())
        enemies[-1].x = random.randint(0,600)
        enemies[-1].y = random.randint(0,600)
cmd = Enemy()
gun = Gun()    
player = Player()
cmd.spawn()
cmd.spawn()
last = 0
frames = 0
fro = 1
while True:
    frames += 1
    scr.fill((0,0,0))
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        Mpos = pygame.mouse.get_pos()
        if event.type == 5:
            gun.shoot1(player.x + 12.5,player.y + 12.5,angle)
    for i in range(0,player.lives):
        scr.blit(player.image1,(i*35,1))
    
    for i in range(len(gun.bullets)):
        try:
            gun.bullets[i].x = gun.bullets[i].x + 4 * math.cos(math.radians(gun.bullets[i].angle + 90))
            gun.bullets[i].y = gun.bullets[i].y + 4 * math.sin(math.radians(gun.bullets[i].angle - 90))
            if gun.bullets[i].x > 600:
                del gun.bullets[i]
            if gun.bullets[i].x < 0:
                del gun.bullets[i]
            if gun.bullets[i].y > 600:
                del gun.bullets[i]
            if gun.bullets[i].y < 0:
                del gun.bullets[i]
            gun.bullets[i].draw()
        except IndexError:
            pass
    for i in range(len(gun.bullets2)):
        try:
            gun.bullets2[i].x = gun.bullets2[i].x + 4 * math.cos(math.radians(gun.bullets2[i].angle + 90))
            gun.bullets2[i].y = gun.bullets2[i].y + 4 * math.sin(math.radians(gun.bullets2[i].angle - 90))
            if gun.bullets2[i].x > 600:
                del gun.bullets2[i]
            if gun.bullets2[i].x < 0:
                del gun.bullets2[i]
            if gun.bullets2[i].y > 600:
                del gun.bullets2[i]
            if gun.bullets2[i].y < 0:
                del gun.bullets2[i]
            gun.bullets2[i].draw()
        except IndexError:
            pass
    for i in range(len(enemies)):
        if enemies[i].distance(player.x,player.y) > 100:
            enemies[i].x = enemies[i].x + enemies[i].speed * math.cos(math.radians(enemies[i].rotate(player.x,player.y) + 90))
            enemies[i].y = enemies[i].y + enemies[i].speed * math.sin(math.radians(enemies[i].rotate(player.x,player.y) - 90))
        enemies[i].image = pygame.image.load("enemy.png").convert()
        enemies[i].image = enemies[i].image.copy()
        enemies[i].image = pygame.transform.rotate(enemies[i].image,enemies[i].rotate(player.x,player.y))
        angle2 = enemies[i].rotate(player.x,player.y)
        if frames % 100 == 0:
            gun.shoot2(enemies[i].x + 12.5,enemies[i].y + 12.5,angle2)
        enemies[i].draw()
    for j in range(len(gun.bullets)):
        for i in range(len(gun.bullets)):
            try:
                if gun.bullets[j].x > enemies[i].x and gun.bullets[j].x < enemies[i].x+25 and gun.bullets[j].y > enemies[i].y and gun.bullets[j].y < enemies[i].y + 25:
                    del enemies[i]
            except IndexError:
                pass
    for j in range(len(gun.bullets2)):
        for i in range(len(gun.bullets2)):
            try:
                if gun.bullets2[j].x > player.x and gun.bullets2[j].x < player.x+25 and gun.bullets2[j].y > player.y and gun.bullets2[j].y < player.y + 25:
                    for i in range(len(hit)-1):
                        if not (hit[i].x > player.x or hit[i].x < player.x+25 or hit[i].y > player.y or hit[i].y < player.y):
                            del hit[i]
                    if hit.count(gun.bullets2[j]) == 0:
                        hit.append(gun.bullets2[j])
                        player.lives = 5 - len(hit)
            except IndexError:
                pass
    if key[pygame.K_a]:
        player.x -= 3
    if key[pygame.K_d]:
        player.x += 3
    if key[pygame.K_w]:
        player.y -= 3
    if key[pygame.K_s]:
        player.y += 3
    if frames % 150 == 0:
        cmd.spawn()
    if player.lives < 1:
        pygame.quit()
        break
    player.image = pygame.image.load("player.jpg").convert()
    player.image = player.image.copy()
    player.image = pygame.transform.rotate(player.image,player.rotate(Mpos[0],Mpos[1]))
    angle = player.rotate(Mpos[0],Mpos[1])
    player.draw()
    pygame.display.update()
    time.sleep(0.005)
quit()

