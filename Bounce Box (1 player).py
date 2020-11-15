print("""HEY,My name is Shaurya,i am in 6th grade, and I am 11 years old.I made this on 15th of August(three days before my birthday)
And I would like to say that i would be really cool if you appreciated this game(or project,whatever),It would really give me a booster, so yeah.
And if any companies like Google or Apple take notice of me, please tell me immediately..It is my dream to work in a famous company(like Google and
Apple).Hope you like this game.
Peace from India.""")
import random
import math
import time
import pygame
import winsound
pygame.init()
scr = pygame.display.set_mode((600,500))
pygame.display.set_caption("Bounce Box - By Fusion ( 11 year old )")
color = (255,0,0)
x = 0
y = 0
global powerup_score_multiplier
#----------------------------------------------------------------------class : self----------------------------------------------------------------
class self:
    x1 = 100
    y1 = 450
    xb = 490
    yb = 450
    xb2 = 0
    yb2 = 0
    angle = -135
    angle2 = angle
    font = pygame.font.SysFont('Agency FB',25)
    score = 0
    def makeRect(x,y,width,height,color):
        pygame.draw.rect(scr,color,pygame.Rect(x,y,width,height))
    def blueColor():
        g = random.randint(1,5)
        return (150,0,150)
    def init():
        color = (255,0,0)
        global s1
        global s2
        global s3
        global s4
        global s5
        global s6
        global s7
        global s8
        global s9
        global s10
        global s11
        global s12
        global s13
        global s14
        global s15
        global s16
        global s17
        global s18
        global s19
        global s20
        global tim2
        s1 = [x,y,random.randint(5,10),random.randint(0,360)]# x, y , size, angle
        s2 = [x,y,random.randint(5,10),random.randint(0,360)]
        s3 = [x,y,random.randint(5,10),random.randint(0,360)]
        s4 = [x,y,random.randint(5,10),random.randint(0,360)]
        s5 = [x,y,random.randint(5,10),random.randint(0,360)]
        s6 = [x,y,random.randint(5,10),random.randint(0,360)]
        s7 = [x,y,random.randint(5,10),random.randint(0,360)]
        s8 = [x,y,random.randint(5,10),random.randint(0,360)]
        s9 = [x,y,random.randint(5,10),random.randint(0,360)]
        s10 = [x,y,random.randint(5,10),random.randint(0,360)]
        s11 = [x,y,random.randint(5,10),random.randint(0,360)]
        s12 = [x,y,random.randint(5,10),random.randint(0,360)]
        s13 = [x,y,random.randint(5,10),random.randint(0,360)]
        s14 = [x,y,random.randint(5,10),random.randint(0,360)]
        s15 = [x,y,random.randint(5,10),random.randint(0,360)]
        s16 = [x,y,random.randint(5,10),random.randint(0,360)]
        s17 = [x,y,random.randint(5,10),random.randint(0,360)]
        s18 = [x,y,random.randint(5,10),random.randint(0,360)]
        s19 = [x,y,random.randint(5,10),random.randint(0,360)]
        s20 = [x,y,random.randint(5,10),random.randint(0,360)]
        tim2 = 0.03
    def LabelScore():
        text = self.font.render("Score : " + str(self.score),30,(255,255,0))
        scr.blit(text,(0,0))
    def Label(x,y,colorO,gainedPoints):
        if powerup_score_multiplier == True:
            text1 = self.font.render(str(gainedPoints) + " (x2)",30,colorO)
        else:
            text1 = self.font.render(str(gainedPoints),30,colorO)
        scr.blit(text1,(x,y))
    def showParticles():
        global tim2
        angle = s1[3]
        s1[0] = s1[0] + r * math.cos(math.radians(angle))
        s1[1] = s1[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s1[0],s1[1],s1[2],s1[2]))
        angle += s2[3]
        s2[0] = s2[0] + r * math.cos(math.radians(angle))
        s2[1] = s2[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s2[0],s2[1],s2[2],s2[2]))
        angle = s3[3]
        s3[0] = s3[0] + r * math.cos(math.radians(angle))
        s3[1] = s3[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s3[0],s3[1],s3[2],s3[2]))
        angle += s4[3]
        s4[0] = s4[0] + r * math.cos(math.radians(angle))
        s4[1] = s4[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s4[0],s4[1],s4[2],s4[2]))
        angle += s5[3]
        s5[0] = s5[0] + r * math.cos(math.radians(angle))
        s5[1] = s5[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s5[0],s5[1],s5[2],s5[2]))
        angle += s6[3]
        s6[0] = s6[0] + r * math.cos(math.radians(angle))
        s6[1] = s6[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s6[0],s6[1],s6[2],s6[2]))
        angle += s7[3]
        s7[0] = s7[0] + r * math.cos(math.radians(angle))
        s7[1] = s7[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s7[0],s7[1],s7[2],s7[2]))
        angle += s8[3]
        s8[0] = s8[0] + r * math.cos(math.radians(angle))
        s8[1] = s8[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s8[0],s8[1],s8[2],s8[2]))
        angle += s9[3]
        s9[0] = s9[0] + r * math.cos(math.radians(angle))
        s9[1] = s9[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s9[0],s9[1],s9[2],s9[2]))
        angle += s10[3]
        s10[0] = s10[0] + r * math.cos(math.radians(angle))
        s10[1] = s10[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s10[0],s10[1],s10[2],s10[2]))
        angle += s11[3]
        s11[0] = s11[0] + r * math.cos(math.radians(angle))
        s11[1] = s11[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s11[0],s11[1],s11[2],s11[2]))
        angle += s12[3]
        s12[0] = s12[0] + r * math.cos(math.radians(angle))
        s12[1] = s12[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s12[0],s12[1],s12[2],s12[2]))
        angle += s13[3]
        s13[0] = s13[0] + r * math.cos(math.radians(angle))
        s13[1] = s13[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s13[0],s13[1],s13[2],s13[2]))
        angle += s14[3]
        s14[0] = s14[0] + r * math.cos(math.radians(angle))
        s14[1] = s14[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s14[0],s14[1],s14[2],s14[2]))
        angle += s15[3]
        s15[0] = s15[0] + r * math.cos(math.radians(angle))
        s15[1] = s15[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s15[0],s15[1],s15[2],s15[2]))
        angle += s16[3]
        s16[0] = s16[0] + r * math.cos(math.radians(angle))
        s16[1] = s16[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s16[0],s16[1],s16[2],s16[2]))
        angle += s17[3]
        s17[0] = s17[0] + r * math.cos(math.radians(angle))
        s17[1] = s17[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s17[0],s17[1],s17[2],s17[2]))
        angle += s18[3]
        s18[0] = s18[0] + r * math.cos(math.radians(angle))
        s18[1] = s18[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s18[0],s18[1],s18[2],s18[2]))
        angle += s19[3]
        s19[0] = s19[0] + r * math.cos(math.radians(angle))
        s19[1] = s19[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s19[0],s19[1],s19[2],s19[2]))
        angle += s20[3]
        s20[0] = s20[0] + r * math.cos(math.radians(angle))
        s20[1] = s20[1] + r * math.sin(math.radians(angle))
        pygame.draw.rect(scr,color,pygame.Rect(s20[0],s20[1],s20[2],s20[2]))

        s1[2] -= 0.250
        s2[2] -= 0.250
        s3[2] -= 0.250
        s4[2] -= 0.250
        s5[2] -= 0.250
        s6[2] -= 0.250
        s7[2] -= 0.250
        s8[2] -= 0.250
        s9[2] -= 0.250
        s10[2] -= 0.250
        s11[2] -= 0.250
        s12[2] -= 0.250
        s13[2] -= 0.250
        s14[2] -= 0.250
        s15[2] -= 0.250
        s16[2] -= 0.250
        s17[2] -= 0.250
        s18[2] -= 0.250
        s19[2] -= 0.250
        s20[2] -= 0.250
        time.sleep(0.015)
    def showPowerups():
        text = self.font.render("Powerups : ",30,(0,255,255))
        scr.blit(text,(150,0))
        if powerup_laser:
            pygame.draw.rect(scr,(0,255,0),pygame.Rect(250,10,25,25))
        if powerup_slowball:
            pygame.draw.rect(scr,(0,0,255),pygame.Rect(300,10,25,25))
        if powerup_fastball:
            pygame.draw.rect(scr,(255,0,0),pygame.Rect(350,10,25,25))
        if powerup_paddles:
            pygame.draw.rect(scr,(0,255,255),pygame.Rect(400,10,25,25))
        if powerup_score_multiplier:
            pygame.draw.rect(scr,(255,255,0),pygame.Rect(450,10,25,25))
    def Sound():
        winsound.PlaySound('clear.wav',winsound.SND_ASYNC)
    def Sound2():
        winsound.PlaySound('shift.wav',winsound.SND_ASYNC)

#-----------------------------------------------------------------initializing variables------------------------------------------------------------
global r
global angle
self.init()
angle = 0
r = 7
eff = False
pygame.draw.line(scr,(255,255,255),(300,500),(300,400),5)
pygame.display.update()
Obj = False
pos = [0,0]
color1 = [random.randint(100,255),random.randint(100,255),random.randint(100,255)]
Obj2 = False
pos2 = [0,0]
color2 = [random.randint(100,255),random.randint(100,255),random.randint(100,255)]
Obj3 = False
pos3 = [0,0]
color3 = [random.randint(100,255),random.randint(100,255),random.randint(100,255)]
Obj4 = False
pos4 = [0,0]
color4 = [random.randint(100,255),random.randint(100,255),random.randint(100,255)]
Obj5 = False
pos5 = [0,0]
color5 = [random.randint(100,255),random.randint(100,255),random.randint(100,255)]
Obj6 = False
pos6 = [0,0]
color6 = [random.randint(100,255),random.randint(100,255),random.randint(100,255)]
Obj7 = False
pos7 = [0,0]
color7 = (255,255,0)
powerup_slowball = False
powerup_fastball = False
powerup_laser = False
powerup_paddles = False
powerup_score_multiplier = False
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
killedx = 0
killedy = 0
killed = False
timei = 250
speedi = 0
speed = 3
Game_speed = 0.0099
effect = False
gained = 0
#------------------------------------------------------------------------------GAME-----------------------------------------------------------------
while True:
    scr.fill((0,0,0))
    self.showPowerups()
    pygame.draw.line(scr,(255,255,255),(300,500),(300,400),5)
    
    self.makeRect(self.x1,self.y1,50,50,(255,0,0))
    self.makeRect(self.x1+300,self.y1,50,50,(255,0,0))
    if powerup_paddles == True:
        self.makeRect(self.x1+100,self.y1,50,50,(0,255,255))
        self.makeRect(self.x1+200,self.y1,50,50,(0,255,255))
    self.makeRect(self.xb,self.yb,10,10,(0,0,255))
    
    self.xb = self.xb + speed * math.cos(math.radians(self.angle))
    self.yb = self.yb + speed * math.sin(math.radians(self.angle))                      
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        if self.x1+350 < 600:
            self.x1 += 3
        else:
            self.x1 -= 3
    if key[pygame.K_LEFT]:
        if self.x1 > 0:
            self.x1 -= 3
        else:
            self.x1 += 3



    if self.xb > 590:
        self.angle += self.angle + self.angle
        self.angle2 = self.angle       
    if self.xb < 0:
        self.angle += self.angle + self.angle
        self.angle2 = self.angle
    if self.yb < 0:
        self.angle -= self.angle + self.angle
        self.angle2 = self.angle

        
    if self.xb > self.x1 and self.xb < self.x1+50 and self.yb > 440:
        self.angle -= self.angle + self.angle
        while self.yb > 440:
            self.xb = self.xb + speed * math.cos(math.radians(self.angle))
            self.yb = self.yb + speed * math.sin(math.radians(self.angle))
            self.angle2 = self.angle
    if self.xb > self.x1+300 and self.xb < self.x1+350 and self.yb > 440:
        self.angle -= self.angle + self.angle
        while self.yb > 440:
            self.xb = self.xb + speed * math.cos(math.radians(self.angle))
            self.yb = self.yb + speed * math.sin(math.radians(self.angle))
            self.angle2 = self.angle
    if self.xb > self.x1+100 and self.xb < self.x1+150 and self.yb > 440 and powerup_paddles == True:
        self.angle -= self.angle + self.angle
        while self.yb > 440:
            self.xb = self.xb + speed * math.cos(math.radians(self.angle))
            self.yb = self.yb + speed * math.sin(math.radians(self.angle))
            self.angle2 = self.angle
    if self.xb > self.x1+200 and self.xb < self.x1+250 and self.yb > 440 and powerup_paddles == True:
        self.angle -= self.angle + self.angle
        while self.yb > 440:
            self.xb = self.xb + speed * math.cos(math.radians(self.angle))
            self.yb = self.yb + speed * math.sin(math.radians(self.angle))
            self.angle2 = self.angle


    
    if random.randint(0,50) == 4 and Obj == False:
        Obj = True
        pos[0] = random.randint(100,500)
        pos[1] = random.randint(100,300)
        pos[0] = random.randint(100,500)
        pos[1] = random.randint(100,300)
        color1 = self.blueColor()
    if Obj == True:
        self.makeRect(pos[0],pos[1],50,50,color1)
        if self.xb > pos[0] and self.xb < pos[0] + 50 and self.yb > pos[1] and self.yb < pos[1] + 50:
            self.angle += self.angle + self.angle
            x = pos[0]
            y = pos[1]
            color = self.blueColor()
            self.init()
            eff = True
            if powerup_score_multiplier == False:
                self.score += 100
                gained = 100
            else:
                self.score += 200
                gained = 200
            killedx = pos[0]
            killedy = pos[1]
            killed = True
            self.Sound()
            while self.xb > pos[0] and self.xb < pos[0] + 50 and self.yb > pos[1] and self.yb < pos[1] + 50:
                self.xb = self.xb + speed * math.cos(math.radians(self.angle))
                self.yb = self.yb + speed * math.sin(math.radians(self.angle))
                self.angle2 = self.angle
            Obj = False
            
    if random.randint(0,50) == 4 and Obj2 == False:
        Obj2 = True
        pos2[0] = random.randint(100,500)
        pos2[1] = random.randint(100,300)
        pos2[0] = random.randint(100,500)
        pos2[1] = random.randint(100,300)
        pos2[0] = random.randint(100,500)
        pos2[1] = random.randint(100,300)
        color2 = self.blueColor()
    if Obj2 == True:
        self.makeRect(pos2[0],pos2[1],50,50,color2)
        if self.xb > pos2[0] and self.xb < pos2[0] + 50 and self.yb > pos2[1] and self.yb < pos2[1] + 50:
            self.angle += self.angle + self.angle
            x = pos2[0]
            y = pos2[1]
            color = self.blueColor()
            self.init()
            eff = True
            if powerup_score_multiplier == False:
                self.score += 100
                gained = 100
            else:
                self.score += 200
                gained = 200
            killedx = pos2[0]
            killedy = pos2[1]
            killed = True
            gained = 100
            self.Sound()
            while self.xb > pos2[0] and self.xb < pos2[0] + 50 and self.yb > pos2[1] and self.yb < pos2[1] + 50:
                self.xb = self.xb + speed * math.cos(math.radians(self.angle))
                self.yb = self.yb + speed * math.sin(math.radians(self.angle))
                self.angle2 = self.angle
            Obj2 = False
            
    if random.randint(0,50) == 4 and Obj3 == False and powerup_laser == False:
        Obj3 = True
        pos3[0] = random.randint(100,500)
        pos3[1] = random.randint(100,300)
        pos3[0] = random.randint(100,500)
        pos3[1] = random.randint(100,300)
        pos3[0] = random.randint(100,500)
        pos3[1] = random.randint(100,300)
        pos3[0] = random.randint(100,500)
        pos3[1] = random.randint(100,300)
        color3 = (0,255,0)
        i1 = 0
        self.xb2 = self.xb
        self.yb2 = self.yb
        self.angle2 = self.angle
    if Obj3 == True:
        self.makeRect(pos3[0],pos3[1],50,50,color3)
        if self.xb > pos3[0] and self.xb < pos3[0] + 50 and self.yb > pos3[1] and self.yb < pos3[1] + 50:
            self.angle += self.angle + self.angle
            x = pos3[0]
            y = pos3[1]
            self.init()
            color = (0,255,0)
            eff = True
            if powerup_score_multiplier == False:
                self.score += 50
                gained = 50
            else:
                self.score += 100
                gained = 100
            killedx = pos3[0]
            killedy = pos3[1]
            killed = True
            self.Sound2()
            while self.xb > pos3[0] and self.xb < pos3[0] + 50 and self.yb > pos3[1] and self.yb < pos3[1] + 50:
                self.xb = self.xb + speed * math.cos(math.radians(self.angle))
                self.yb = self.yb + speed * math.sin(math.radians(self.angle))
                self.angle2 = self.angle
            Obj3 = False
            powerup_laser = True
    if powerup_laser == True:
        if i1 != 1000:
            self.xb2 = self.xb + 8000 * math.cos(math.radians(self.angle2))
            self.yb2 = self.yb + 8000 * math.sin(math.radians(self.angle2))
            pygame.draw.line(scr,(0,255,0),(self.xb,self.yb),(self.xb2 + 8000 * math.cos(math.radians(self.angle)),self.yb2 + 8000 * math.sin(math.radians(self.angle))),5)
            i1 += 1
        else:
            powerup_laser = False
            
    if random.randint(0,50) == 4 and Obj4 == False and powerup_slowball == False:
        Obj4 = True
        pos4[0] = random.randint(100,500)
        pos4[1] = random.randint(100,300)
        pos4[0] = random.randint(100,500)
        pos4[1] = random.randint(100,300)
        pos4[0] = random.randint(100,500)
        pos4[1] = random.randint(100,300)
        pos4[0] = random.randint(100,500)
        pos4[1] = random.randint(100,300)
        pos4[0] = random.randint(100,500)
        pos4[1] = random.randint(100,300)
        color4 = (0,0,255)
        i2 = 0
    if Obj4 == True:
        self.makeRect(pos4[0],pos4[1],50,50,color4)
        if self.xb > pos4[0] and self.xb < pos4[0] + 50 and self.yb > pos4[1] and self.yb < pos4[1] + 50:
            self.angle += self.angle + self.angle
            x = pos4[0]
            y = pos4[1]
            self.init()
            color = (0,0,255)
            eff = True
            if powerup_score_multiplier == False:
                self.score += 100
                gained = 100
            else:
                self.score += 200
                gained = 200
            killedx = pos4[0]
            killedy = pos4[1]
            killed = True
            self.Sound2()
            while self.xb > pos4[0] and self.xb < pos4[0] + 50 and self.yb > pos4[1] and self.yb < pos4[1] + 50:
                self.xb = self.xb + speed * math.cos(math.radians(self.angle))
                self.yb = self.yb + speed * math.sin(math.radians(self.angle))
                self.angle2 = self.angle
            Obj4 = False
            powerup_slowball = True
    if powerup_slowball == True:
        if i2 != 1000:
            speed = 2
            i2 += 1
        else:
            powerup_slowball = False
            i2 = 0
            speed = 2.5

    if random.randint(0,50) == 4 and Obj5 == False and powerup_fastball == False:
        Obj5 = True
        pos5[0] = random.randint(100,500)
        pos5[1] = random.randint(100,300)
        pos5[0] = random.randint(100,500)
        pos5[1] = random.randint(100,300)
        pos5[0] = random.randint(100,500)
        pos5[1] = random.randint(100,300)
        pos5[0] = random.randint(100,500)
        pos5[1] = random.randint(100,300)
        pos5[0] = random.randint(100,500)
        pos5[1] = random.randint(100,300)
        pos5[0] = random.randint(100,500)
        pos5[1] = random.randint(100,300)
        pos5[0] = random.randint(100,500)
        pos5[1] = random.randint(100,300)
        color5 = (255,0,0)
        i3 = 0
    if Obj5 == True:
        self.makeRect(pos5[0],pos5[1],50,50,color5)
        if self.xb > pos5[0] and self.xb < pos5[0] + 50 and self.yb > pos5[1] and self.yb < pos5[1] + 50:
            self.angle += self.angle + self.angle
            x = pos5[0]
            y = pos5[1]
            self.init()
            color = (255,0,0)
            eff = True
            if powerup_score_multiplier == False:
                self.score += 200
                gained = 200
            else:
                self.score += 400
                gained = 400
            killedx = pos5[0]
            killedy = pos5[1]
            killed = True
            self.Sound2()
            while self.xb > pos5[0] and self.xb < pos5[0] + 50 and self.yb > pos5[1] and self.yb < pos5[1] + 50:
                self.xb = self.xb + speed * math.cos(math.radians(self.angle))
                self.yb = self.yb + speed * math.sin(math.radians(self.angle))
                self.angle2 = self.angle
            Obj5 = False
            powerup_fastball = True
    if powerup_fastball == True:
        if i3 != 1000:
            speed = 4
            i3 += 1
        else:
            powerup_fastball = False
            i3 = 0
            speed = 3

    if random.randint(0,50) == 4 and Obj6 == False and powerup_paddles == False:
        Obj6 = True
        pos6[0] = random.randint(100,500)
        pos6[1] = random.randint(100,300)
        pos6[0] = random.randint(100,500)
        pos6[1] = random.randint(100,300)
        pos6[0] = random.randint(100,500)
        pos6[1] = random.randint(100,300)
        pos6[0] = random.randint(100,500)
        pos6[1] = random.randint(100,300)
        pos6[0] = random.randint(100,500)
        pos6[1] = random.randint(100,300)
        pos6[0] = random.randint(100,500)
        pos6[1] = random.randint(100,300)
        color6 = (0,255,255)
        i4 = 0
    if Obj6 == True:
        self.makeRect(pos6[0],pos6[1],50,50,color6)
        if self.xb > pos6[0] and self.xb < pos6[0] + 50 and self.yb > pos6[1] and self.yb < pos6[1] + 50:
            self.angle += self.angle + self.angle
            x = pos6[0]
            y = pos6[1]
            self.init()
            color = (0,255,255)
            eff = True
            if powerup_score_multiplier == False:
                self.score += 100
                gained = 100
            else:
                self.score += 200
                gained = 200
            killedx = pos6[0]
            killedy = pos6[1]
            killed = True
            self.Sound2()
            while self.xb > pos6[0] and self.xb < pos6[0] + 50 and self.yb > pos6[1] and self.yb < pos6[1] + 50:
                self.xb = self.xb + speed * math.cos(math.radians(self.angle))
                self.yb = self.yb + speed * math.sin(math.radians(self.angle))
                self.angle2 = self.angle
            Obj6 = False
            powerup_paddles = True
    if powerup_paddles == True:
        if i4 != 1000:
            i4 += 1
        else:
            powerup_paddles = False
            i4 = 0

    if random.randint(0,50) == 4 and Obj7 == False and powerup_score_multiplier == False:
        Obj7 = True
        pos7[0] = random.randint(100,500)
        pos7[1] = random.randint(100,300)
        color7 = (255,255,0)
        i7 = 0
    if Obj7 == True:
        self.makeRect(pos7[0],pos7[1],50,50,color7)
        if self.xb > pos7[0] and self.xb < pos7[0] + 50 and self.yb > pos7[1] and self.yb < pos7[1] + 50:
            self.angle += self.angle + self.angle
            x = pos7[0]
            y = pos7[1]
            self.init()
            color = (255,255,0)
            eff = True
            self.score += 400
            gained = 400
            killedx = pos7[0]
            killedy = pos7[1]
            killed = True
            self.Sound2()
            while self.xb > pos7[0] and self.xb < pos7[0] + 50 and self.yb > pos7[1] and self.yb < pos7[1] + 50:
                self.xb = self.xb + speed * math.cos(math.radians(self.angle))
                self.yb = self.yb + speed * math.sin(math.radians(self.angle))
                self.angle2 = self.angle
            Obj7 = False
            powerup_score_multiplier = True
    if powerup_score_multiplier == True:
        if i5 != 1000:
            i5 += 1
        else:
            powerup_score_multiplier = False
            i5 = 0

    if eff == True and r > 0:
        self.showParticles()
        r -= 0.2
    else:
        r = 7
        eff = False

    self.LabelScore()
    if speedi != 400:
        speedi += 9
    else:
        Game_speed -= 0.0001
        speedi = 250
    if self.angle > 360:
        self.angle -= 360
    if self.angle < -360:
        self.angle += 360
    time.sleep(Game_speed)
    self.makeRect(self.xb,self.yb,10,10,(0,0,255))    
    self.angle2 = self.angle
    if self.yb > 500:
        break
    if killed == True:
        if timei != 0:
            self.Label(killedx,killedy,(255,255,0),gained)
            timei -= 1
        else:
            killed = False
            timei = 150
            gained = 0
    pygame.display.update()
scr.fill((0,0,0))
text = self.font.render("GAME OVER; YOUR SCORE : " + str(self.score),40,(0,0,255))
scr.blit(text,(100,100))
#------------------------------------------------------------------------uninitializing--------------------------------------------------------------
del self
del r
del angle
del eff 
del Obj
del pos
del color1
del Obj2
del pos2
del color2
del Obj3
del pos3
del color3
del Obj4
del pos4
del color4
del Obj5
del pos5
del color5
del Obj6
del pos6
del color6
del Obj7
del pos7
del color7
del powerup_slowball
del powerup_fastball
del powerup_laser
del powerup_paddles
del powerup_score_multiplier
del i1
del i2
del i3
del i4
del i5
del killedx
del killedy
del killed
del timei
del speedi
del speed
del Game_speed
del effect
del gained

pygame.display.update()
input()

