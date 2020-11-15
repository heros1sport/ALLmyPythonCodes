#-----------------------------------------------------------------------initialize game tools----------------------------------------------------------
import pygame
import time
pygame.init()
scr = pygame.display.set_mode((600,600))
pygame.display.set_caption("Galaxy Alienic War Shooter - Fusion ( 11 year old )")
#-----------------------------------------------------------------------initialize classes----------------------------------------------------------
#These classes are practically a blueprint or are objects which contains the state of the current object itself; These are blueprints for making inst
#-ances of the following titles they carry. They can be used to create as many instances of the class without having to define each one of them
#seperately in the middle of the program by yourself.
class Player:
    def __init__(self):
        self.x = 225
        self.y = 550
    def show(self):
        pygame.draw.rect(scr,(0,255,255),pygame.Rect(self.x,self.y,50,50))
    def moveRight(self):
        self.x += 12
    def moveLeft(self):
        self.x -= 12
class Rocket:
    def __init__(self):
        self.x = 255
        self.y = 550
        
    def show(self):
        pygame.draw.rect(scr,(255,255,0),pygame.Rect(self.x,self.y,10,10))
    def move(self):
        self.y -= 12
class Enemy:
    def __init__(self):
        self.x = 255
        self.y = 0
        self.direction = 5
    def show(self):
        pygame.draw.rect(scr,(0,255,0),pygame.Rect(self.x,self.y,50,50))
    def moveRight(self):
        self.x += self.direction
    def moveLeft(self):
        self.x += self.direction
class Bomb:
    def __init__(self):
        self.x = 255
        self.y = 0
        
    def show(self):
        pygame.draw.rect(scr,(100,100,0),pygame.Rect(self.x,self.y,10,10))
    def move(self):
        self.y += 12
#---------------------------------------------------------------------------Initialize variables-------------------------------------------------------------------
player = Player()
rockets = []
enemies = []
bombs = []
last = 0
frames = 0
running = True
gun_reload_start_frame = 0
bomb_reload_start_frame = 0
#------------------------------------------------------------------------------GAME-----------------------------------------------------------------
# fps : 0.03s per frame
# 
while running:
#   clear screen
    scr.fill((0,0,0))
#   event loop
    for event in pygame.event.get():
#       keep key events updated
        keyPressed = pygame.key.get_pressed()
#       if a rocket is shot and 30 frames have passed from the frame at which the rocket was shot (if the reloading has been done)
        if keyPressed[pygame.K_SPACE] and frames > gun_reload_start_frame + 13:
#           add a rocket to the game
            rockets.append([Rocket(),player.x + 20])
#           mark the frame at which the rocket was shot (for keeping time between 2 shots)
            gun_reload_start_frame = frames
#   if bomb or rocket go beyond the boundaries;        
    if len(rockets) > 0:
        if rockets[0][0].y < -10:
            del rockets[0]
    if len(bombs) > 0:
        if bombs[0][0].y > 600:
            del bombs[0]
#   This script will keep updating the movement of the rockets and bombs along with their state and property;
    for i in range(len(rockets)):
        try:
            rockets[i][0].x = rockets[i][1]
            rockets[i][0].show()
            rockets[i][0].move()
        except IndexError:
            break
    for i in range(len(bombs)):
        try:
            bombs[i][0].x = bombs[i][1]
            bombs[i][0].show()
            bombs[i][0].move()
            if bombs[i][0].x > player.x and bombs[i][0].x + 10 < player.x + 50 and bombs[i][0].y > 550:
                running = False
        except IndexError:
            break
#   This is order what enemies have to do using their functions of their classes (blueprint);
    for i in range(len(enemies)):
        try:
            enemies[i].show()
            if enemies[i].direction == 5:
                enemies[i].moveRight()
                if enemies[i].x > 550:
                    enemies[i].direction = -5
                    enemies[i].y += 50
            if enemies[i].direction == -5:
                enemies[i].moveLeft()
                if enemies[i].x < 0:
                    enemies[i].direction = 5
                    enemies[i].y += 50
            if enemies[i].x > player.x and enemies[i].x + 10 < player.x + 50 and bomb_reload_start_frame + 20 < frames:
                bombs.append([Bomb() , enemies[i].x + 20, enemies[i].y + 50])
                bombs[-1][0].y = bombs[-1][2]
                bomb_reload_start_frame = frames
            for j in range(len(rockets)):
                if rockets[j][0].x > enemies[i].x and rockets[j][0].x + 10 < enemies[i].x + 50 and rockets[j][0].y < enemies[i].y + 50:
                    del enemies[i]
                    del rockets[j]
        except IndexError:
            break
#   movement of the player;
    if keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d]:
        player.moveRight()
    if keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]:
        player.moveLeft()
#   enemy is added every 80 times this loop reaches the end;
    if frames % 80 == 0:
        enemies.append(Enemy())

#   update the screen;
    player.show()
    pygame.display.update()
#   give time between each frame or each time the loop reaches the end;
    time.sleep(0.03)
#   add to how many frames have been passed
    frames += 1
pygame.quit()
