import pygame
pygame.init()
scr = pygame.display.set_mode((600,500))
r = 1
color = (255,0,0)
lastpos = pygame.mouse.get_pos()
width = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        Ke = pygame.key.get_pressed()
        if Ke[pygame.K_RIGHT]:
            r += 1
        if Ke[pygame.K_LEFT]:
            r -= 1
        if Ke[pygame.K_UP]:
            width += 1
        if Ke[pygame.K_LEFT]:
            width -= 1
        if Ke[pygame.K_c]:
            scr.fill((0,0,0))
    Mpos = pygame.mouse.get_pos()
    Ke = pygame.key.get_pressed()
    if pygame.mouse.get_pressed() == (1,0,0):
        lastpos = Mpos
        while pygame.mouse.get_pressed() != (0,0,0):
            for event in pygame.event.get():
                pass
            Mpos = pygame.mouse.get_pos()
            pygame.draw.line(scr,color,(lastpos[0],lastpos[1]),(Mpos[0],Mpos[1]),width)
            pygame.display.update()
            lastpos = Mpos
    if r == 1:
        color = (255,0,0)
    if r == 2:
        color = (0,255,0)
    if r == 3:
        color = (0,0,255)
    if r == 4:
        color = (255,255,0)
    if r == 5:
        color = (0,255,255)
    if r == 6:
        color = (255,0,255)
    if r == 7:
        color = (100,100,100)
    if r > 7:
        r = 1
    if r < 0:
        r = 7
    
    pygame.display.update()
