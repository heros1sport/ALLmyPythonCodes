import pygame, math
import time
 
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
global a
a = 180
t = 0.02
def drawTree(x1, y1, angle, depth, division,color,width):
    
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)
        drawTree(x2, y2, angle - a, depth - 1, a, (0,((255/10)*(10-depth))+50,0),int(depth+5))
        drawTree(x2, y2, angle + a, depth - 1, a,(0,((255/10)*(10-depth))+50,0),int(depth+5))
 
while True:
    for event in pygame.event.get():
        pass
    screen.fill((0,0,0))
    drawTree(400, 550, -90, 10, a, (0,25,0),20)
    a += 1
    pygame.display.flip()
    time.sleep(t)
