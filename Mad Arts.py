import pygame
pygame.init()
screen = pygame.display.set_mode((1350,700))
r = 255
g = 0
b = 0
screen.fill((255,255,255))
pygame.display.update()
while True:
    for event in pygame.event.get():
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_d]:
            pygame.draw.circle(screen,(r,g,b), pygame.mouse.get_pos(),5,0)
            a = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(180,0,b), (a[0],screen.get_width() - a[1]),5,0)
            pygame.draw.circle(screen,(r,255,b), (screen.get_width() - a[0],a[1]),5,0)
            b2 = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(100,100,255), (b2[0],500 - b2[1]),5,0)
            c = (b2[0],500 - b2[1])
            pygame.draw.circle(screen,(100,255,100), (screen.get_width() - c[0],c[1]),5,0)
            pygame.display.update()
        if keyPressed[pygame.K_c]:
            screen.fill((255,255,255))
            pygame.display.update()
        if event.type == pygame.QUIT:
            break
quit()
                
