import math
import pygame
import time
pygame.init()
scr = pygame.display.set_mode((200,200))
Total = int(input("Total value:"))
val1 = (input("value 1 name:"),int(input("value out of total:")))
val2 = (input("value 2 name:"),int(input("value out of total:")))
val3 = (input("value 3 name:"),int(input("value out of total:")))
val4 = (input("value 4 name:"),int(input("value out of total:")))
val5 = (input("value 5 name:"),int(input("value out of total:")))
class PieChart:
    angle = 0
    coord = [100,0]
    def makeCircle():
        pygame.draw.circle(scr,(255,255,255),(100,100),100,5)
    def makeLine(rotate = 0,color = None):
        PieChart.angle += 1
        PieChart.coord[0] = PieChart.coord[0] + 1.75 * math.cos(math.radians(PieChart.angle))
        PieChart.coord[1] = PieChart.coord[1] + 1.75 * math.sin(math.radians(PieChart.angle))
        pygame.draw.line(scr,color,(100,100),(PieChart.coord[0],PieChart.coord[1]),5)
#                                                                      |----------------| 
#______________________________________________________________________|Calculation Area|__________________________________________________________
#Calculation to calculate values under value 360:                      |----------------|
# x = trimmed value of under 360
# c = total no. of degrees
# t = total value
# v = value

#c = 360
#Equation:
# x/c = v/t
# x = (t / c) * v


#Simply said: 360 divided by Total value multiplied by value
#___________________________________________________________________________________________________________________________________________________
scr.fill((0,0,0))
PieChart.makeCircle()
v1 = (360 / Total)
for i in range(int(float(v1)*(int(val1[1])+1))):
    PieChart.makeLine(1,(0,255,255))
    
for i in range(int(float(v1)*(int(val2[1])+1))):
    PieChart.makeLine(1,(0,0,255))
    
for i in range(int(float(v1)*(int(val3[1])+1))):
    PieChart.makeLine(1,(255,255,0))
    
for i in range(int(float(v1)*(int(val4[1])+1))):
    PieChart.makeLine(1,(0,255,0))
    
for i in range(int(float(v1)*(int(val5[1])+1))):
    PieChart.makeLine(1,(255,255,255))

pygame.display.update()
print("\n\n Total : "+str(Total)+"\n\n\n")
print("Name: " + val1[0])
print("Colour: light blue")
print("Value: " + str(val1[1]) + "\n")
print("Name: " + val2[0])
print("Colour: blue")
print("Value: " + str(val2[1]) + "\n")
print("Name: " + val3[0])
print("Colour: yellow")
print("Value: " + str(val3[1]) + "\n")
print("Name: " + val4[0])
print("Colour: green")
print("Value: " + str(val4[1]) + "\n")
print("Name: " + val5[0])
print("Colour: white")
print("Value: " + str(val5[1]) + "\n")
print("Space Left : " + str(Total - (val1[1]+val2[1]+val3[1]+val4[1]+val5[1])))
pygame.display.update()
