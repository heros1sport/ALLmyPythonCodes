import ast
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostbyname(socket.gethostname()),int(input())))
print("CONNECTED")
import pygame
pygame.init()
scr = pygame.display.set_mode((600,600))
x = 100
y = 100

while True:
    scr.fill((0,0,0))
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        x += 1
    if key[pygame.K_LEFT]:
        x -= 1
    if key[pygame.K_DOWN]:
        y += 1
    if key[pygame.K_UP]:
        y -= 1
    pygame.draw.rect(scr,(255,0,0),pygame.Rect(x,y,25,25))
    s.send(bytes("[" + str(x) + ","+ str(y)+"]",'utf-8'))
    player2 = s.recv(1024).decode("utf-8")
    pygame.draw.rect(scr,(255,0,0),pygame.Rect(ast.literal_eval(player2)[0],ast.literal_eval(player2)[1],25,25))
    pygame.display.update()
