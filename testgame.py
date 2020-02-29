'''
Michael Talaga
Advanced Computer Technology
Mr. Wolf
11/18/15
'''
import pygame, sys, pygame.mixer
from sys import exit
import random
from pygame import *
import time

h = 700
w = 700
m = 0
health = 100
score = 0
pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
done = False
x = 400
y = 400

w1, w2, w3, w4, w5 = 0, 0, 0, 0, 0


white = (255, 255, 255)
myfont = font.SysFont('arial', 20)
s_g = myfont.render(str(score), 1, (55, 255, 55))

g = 0

gameover = pygame.image.load('GameOver.png')
lside = pygame.image.load('lside.png')
lside2 = pygame.image.load('lside2.png')
background = pygame.image.load('water.png')
wave = pygame.image.load('wave.png')
number1 = pygame.image.load('number1.png')
number2 = pygame.image.load('number2.png')
number3 = pygame.image.load('number3.png')
number4 = pygame.image.load('number4.png')
number5 = pygame.image.load('number5.png') 

pygame.init()

ee1, ee2, ee3, ee4, ee5, ee6, ee7, ee8, ee9, ee10, ee11, ee12, ee13, ee14, ee15, ee16, ee17, ee18 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
ee19, ee20, ee21, ee22, ee23, ee24, ee25, ee26, ee27, ee28, ee29, ee30, ee31, ee32, ee33, ee34, ee35, ee36, ee37, ee38, ee39, ee40, ee41, ee42, ee43, ee44, ee45, ee46, ee47, ee48, ee49 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 

bb1 = 0
bb2 = 0
bb3 = 0
bb4 = 0
bb5 = 0
bb6 = 0
bb7 = 0
bb8 = 0
bb9 = 0
bb10 = 0
bb11 = 0
bb12 = 0
bb13 = 0
bb14 = 0
bb15 = 0
bb16 = 0
bb17 = 0
bb18 = 0
bb19, bb20, bb21, bb22, bb23, bb24, bb25 = 0, 0, 0, 0, 0, 0, 0



cc1 = 0
cc2 = 0
cn1 = False

ecount = 0

e1 = -10
e2 = -10
e3 = -10
e4 = -10
e5 = -10
e6 = -10
e7 = -10
e8 = -10
e9 = -10
e10 = -10
e11 = -10
e12 = -10
e13 = -10
e14 = -10
e15 = -10
e16 = -10
e17 = -10
e18 = -10
e19 = -10
e19, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40, e41, e42, e43, e44, e45, e46, e47, e48, e49 = -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10 

hppn1, hppn2, hppn3 = -10, -10, -10



b1 = -13
b2 = -13 
b3 = -13
b4 = -17
b5 = -17
b6 = -17
b7 = -17
b8 = -17
b9 = -17
b10 = -17
b11 = -17
b12 = -17
b13 = -17
b14 = -17
b15 = -17
b16 = -17
b17 = -17
b18 = -17
b19, b20, b21, b22, b23, b24, b25 = -17, -17, -17, -17, -17, -17, -17

hp1n, hp2n, hp3n = -20, -20, -20

wave1 = False
wave2 = False
wave3 = False
wave4 = False
wave5 = False
wave6 = False

show_laser = True
show_e1, show_e2, show_e3, show_e4, show_e5, show_e6, show_e7, show_e8, show_e9, show_e10, show_e11, show_e12, show_e13, show_e14, show_e15, show_e16, show_e17, show_e18 = True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True
show_e19, show_e20, show_e21, show_e22, show_e23, show_e24, show_e25, show_e26, show_e27, show_e28, show_e29, show_e30, show_e31, show_e32, show_e33, show_e34, show_e35, show_e36, show_e37, show_e38, show_e39, show_e40, show_e41, show_e42, show_e43, show_e44, show_e45, show_e46, show_e47, show_e48, show_e49 = True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True

show_t1 = True
show_t2 = True


show_b, show_b2, show_b3, show_b4, show_b5, show_b6, show_b7, show_b8, show_b9, show_b10, show_b11, show_b12, show_b13, show_b14, show_b15, show_b16, show_b17, show_b18, show_b19, show_b20, show_b21, show_b22, show_b23, show_b24, show_b25 = True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True


show_hp1, show_hp2, show_hp3 = True, True, True
collide1 = False
collide2 = False
'''
if show_e1 == False:
    ke1 == True
if show_e2 == False:
    ke2 == True
if show_e3 == False:
    ke3 == True
if show_e4 == False:
    ke4 == True        
'''
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.velocity = 0
        self.image = pygame.image.load('speeder.png')
        self.numImages = 6
        self.cImage = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.speedx = 0
        self.speedy = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.speedx -= 14
        if pressed[pygame.K_RIGHT]:
            self.speedx += 14  
        self.x += self.speedx
        if pressed[pygame.K_DOWN]:
            self.cImage = 0
            self.y += 4
        if pressed[pygame.K_UP] and (self.cImage <= self.numImages - 1):
            self.cImage += 1
            self.y -= 10  
        if self.cImage >= 5:
            self.cImage = 5 
   
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y), (self.cImage * self.width, 0, self.width, self.height)) 

class Health:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.width = 300
        self.height = 96
        self.velocity = 0
        self.images = pygame.image.load('health.png') 
        self.numimages = 20    
        self.cImage = 0
        self.health = 100  
        
    def update(self):  
        
        #if collide1 == True:
        #self.health -= 25 
        if self.health > 96:
            self.cImage = 0    
        if self.health >= 92 and self.health <= 96:
            self.cImage = 1
        if self.health >= 88 and self.health <= 92:
            self.cImage = 2
        if self.health >= 84 and self.health <= 88:
            self.cImage = 3    
        if self.health >= 80 and self.health <= 84:
            self.cImage = 4    
        if self.health >= 76 and self.health <= 80:
            self.cImage = 5    
        if self.health >= 72 and self.health <= 76:
            self.cImage = 6    
        if self.health >= 68 and self.health <= 72:
            self.cImage = 7    
        if self.health >= 64 and self.health <= 68:
            self.cImage = 8
        if self.health >= 60 and self.health <= 64:
            self.cImage = 9    
        if self.health >= 56 and self.health <= 60:
            self.cImage = 10    
        if self.health >= 52 and self.health <= 56:
            self.cImage = 11    
        if self.health >= 48 and self.health <= 52:
            self.cImage = 12
        if self.health >= 44 and self.health <= 48:
            self.cImage = 13
        if self.health >= 39 and self.health <= 44:
            self.cImage = 14    
        if self.health >= 34 and self.health <= 39:
            self.cImage = 15    
        if self.health >= 29 and self.health <= 34:
            self.cImage = 16    
        if self.health >= 24 and self.health <= 29:
            self.cImage = 17    
        if self.health >= 18 and self.health <= 24:
            self.cImage = 18    
        if self.health >= 5 and self.health <= 18:
            self.cImage = 19    
        if self.health < 5:
            self.cImage = 19 
       
                
        ##Health^^
            
    def render(self, screen):
        screen.blit(self.images, (self.x, self.y), (self.cImage * self.width, 0, self.width, self.height))   

class HealthPowerup(pygame.sprite.Sprite):
    def __init__(self, x, y, id):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.velocity = 0
        self.image = pygame.image.load('healthpowerup.png')
        self.id = id
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        self.rect.y += 3
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
                   
class Enemy1(pygame.sprite.Sprite):
    def __init__(self, x, y, id):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.id = id
        self.velocity = 0
        self.image = pygame.image.load('enemy1.png')
        self.cImage = 0
        self.z = 0
        self.j = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.j += 1
        self.speedx = 0
        self.speedy = 0
        self.rect.y += 2.2
        if self.rect.y <= 701:
            if self.z <= 100:
                self.rect.x += random.randint(1, 2)
            elif self.z > 100 and self.z < 200:
                self.rect.x += random.randint(-2, -1)  
            if self.z >= 200:
                self.z = 0
            if self.rect.y <= 700:        
                self.z += random.randint(0, 5)
        if self.rect.x >= 620:
            self.rect.x = 621
        if self.rect.x <= 50:
            self.rect.x = 51 
               
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, id):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.id = id
        self.velocity = 0
        self.image = pygame.image.load('tank.png')
        self.z = 0
        self.j = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.j += 1
        self.speedx = 0
        self.speedy = 0
        self.rect.y += 1
        if self.rect.y <= 701:
            if self.z <= 100:
                self.rect.x += random.randint(0, 1)
            elif self.z > 100 and self.z < 200:
                self.rect.x += random.randint(-1, 0)  
            if self.z >= 200:
                self.z = 0
            if self.rect.y <= 700:        
                self.z += random.randint(0, 5)
        if self.rect.x >= 620:
            self.rect.x = 621
        if self.rect.x <= 50:
            self.rect.x = 51 
               
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))  
              
        
class Laser(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('lazer.png')
        self.rect = self.image.get_rect() 
        self.m = 0
        
    def update(self):
        self.m += 1
        if (self.m % 5) != 0 or self.m % 4 != 1:
            self.rect.y -= 30
        if self.rect.y <= -10:
            self.rect.y = -100000000
            self.rect.x = 500    
class RLaser(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('lazer.png')
        self.rect = self.image.get_rect() 
        self.m = 0
        
    def update(self):
        self.m += 1
        if (self.m % 5) != 0 or self.m % 4 != 1:
            self.rect.y += 13
        if self.rect.y <= 5:
            self.rect.y = -10000000    
        
            
class Boss(pygame.sprite.Sprite):
    
    def __init__(self, x, y, id):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.id = id
        self.width = 38
        self.height = 86
        self.velocity = 0
        self.image = pygame.image.load('boss.png')
        #self.numImages = 5
        self.cImage = 0
        self.z = 0
        #self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.speedx = 0
        self.speedy = 0
        if self.rect.y <= 800:
            self.rect.y += 7
        if self.z <= 100:
            self.rect.x += random.randint(1, 2)
        elif self.z > 100 and self.z < 200:
            self.rect.x += random.randint(-2, -1)  
        #self.cImage += 1
        if self.z >= 200:
            self.z = 0 
        #if self.cImage == 5:
        #    self.cImage = 4
        self.z += random.randint(0, 5)
        
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y), (self.cImage * self.width, 0, self.width, self.height))                         

pygame.init()                          

all_sprites_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
Rlaser_list = pygame.sprite.Group()
boss_list = pygame.sprite.Group()
##sprite creation
health = Health(200, 0, 100)
player = Player(400, 590)


#wave1
enemy = Enemy1(random.randint(25, 575), -280, 1)
enemy2 = Enemy1(random.randint(25, 575), -420, 2)
enemy3 = Enemy1(random.randint(25, 575), -540, 3)
enemy4 = Enemy1(random.randint(25, 575), -680, 4)


enemy_list.add(enemy)
enemy_list.add(enemy2)
enemy_list.add(enemy3)
enemy_list.add(enemy4)

#wave2
enemy5 = Enemy1(random.randint(25, 575), -1700, 5)
enemy6 = Enemy1(random.randint(25, 575), -1800, 6)
enemy7 = Enemy1(random.randint(25, 575), -1870, 7)
enemy8 = Enemy1(random.randint(25, 575), -1970, 8)
enemy9 = Enemy1(random.randint(25, 575), -2100, 9)
boss2 = Boss(random.randint(150, 600), -7000, -2)
boss = Boss(random.randint(150, 600), -6000, -1) 
    
enemy_list.add(enemy5)
enemy_list.add(enemy6)
enemy_list.add(enemy7)
enemy_list.add(enemy8)
enemy_list.add(enemy9)
enemy_list.add(boss)
enemy_list.add(boss2)
boss_list.add(boss)
boss_list.add(boss2)


#wave3
tank1 = Tank(random.randint(250, 450), -1080, 10)
boss3 = Boss(random.randint(150, 600), -9200 - 150, -3)
enemy11 = Enemy1(random.randint(25, 575), -2800 - 300, 11)
enemy12 = Enemy1(random.randint(25, 575), -2880 - 300, 12)
enemy13 = Enemy1(random.randint(25, 575), -2970 - 300, 13)
enemy14 = Enemy1(random.randint(25, 575), -3100 - 300, 14)
enemy15 = Enemy1(random.randint(25, 575), -3190 - 300, 15)
enemy16 = Enemy1(random.randint(25, 575), -3280 - 300, 16)
enemy17 = Enemy1(random.randint(25, 575), -3380 - 300, 17)
enemy18 = Enemy1(random.randint(25, 575), -3460 - 300, 18)

healthpowerup1 = HealthPowerup(random.randint(25, 575), -7500, -500)

enemy_list.add(enemy11)
enemy_list.add(enemy12)
enemy_list.add(enemy13)
enemy_list.add(enemy14)
enemy_list.add(enemy15)
enemy_list.add(enemy16)
enemy_list.add(enemy17)
enemy_list.add(enemy18)
enemy_list.add(tank1)
boss_list.add(boss3)
enemy_list.add(healthpowerup1)

#wave 4
boss4 = Boss(random.randint(150, 600), -17000 + 1320, -4)
boss5 = Boss(random.randint(150, 600), -17150 + 1320, -5)
boss6 = Boss(random.randint(150, 600), -17350 + 1320, -6)
boss7 = Boss(random.randint(150, 600), -17500 + 1320, -7)
boss8 = Boss(random.randint(150, 600), -17630 + 1320, -8)
boss9 = Boss(random.randint(150, 600), -17800 + 1320, -9)
boss10 = Boss(random.randint(150, 600), -17920 + 1320, -10)
boss11 = Boss(random.randint(150, 600), -18020 + 1320, -11)
boss12 = Boss(random.randint(150, 600), -18190 + 1320, -12)
boss13 = Boss(random.randint(150, 600), -18320 + 1320, -13)
boss14 = Boss(random.randint(150, 600), -18500 + 1320, -14)
boss15 = Boss(random.randint(150, 600), -18630 + 1320, -15)
boss16 = Boss(random.randint(150, 600), -18800 + 1320, -16)
boss17 = Boss(random.randint(150, 600), -18950 + 1320, -17)
boss18 = Boss(random.randint(150, 600), -19120 + 1320, -18)
boss19 = Boss(random.randint(150, 600), -19300 + 1320, -19)

enemy_list.add(boss4)
enemy_list.add(boss5)
enemy_list.add(boss6)
enemy_list.add(boss7)
enemy_list.add(boss8)
enemy_list.add(boss9)
enemy_list.add(boss10)
enemy_list.add(boss11)
enemy_list.add(boss12)
enemy_list.add(boss13)
enemy_list.add(boss14)
enemy_list.add(boss15)
enemy_list.add(boss16)
enemy_list.add(boss17)
enemy_list.add(boss18)
enemy_list.add(boss19)
boss_list.add(boss4)
boss_list.add(boss5)
boss_list.add(boss6)
boss_list.add(boss7)
boss_list.add(boss8)
boss_list.add(boss9)
boss_list.add(boss10)
boss_list.add(boss11)
boss_list.add(boss12)
boss_list.add(boss13)
boss_list.add(boss14)
boss_list.add(boss15)
boss_list.add(boss16)
boss_list.add(boss17)
boss_list.add(boss18)
boss_list.add(boss19)

#wave5
enemy19 = Enemy1(random.randint(25, 575), -4100 - 1990 - 2000, 19)
enemy20 = Enemy1(random.randint(25, 575), -4190 - 1990 - 2000, 20)
enemy21 = Enemy1(random.randint(25, 575), -4300 - 1990 - 2000, 21)
enemy22 = Enemy1(random.randint(25, 575), -4390 - 2010 - 2000, 22)
enemy23 = Enemy1(random.randint(25, 575), -4490 - 2030 - 2000, 23)
enemy24 = Enemy1(random.randint(25, 575), -4600 - 2050 - 2000, 24)
enemy25 = Enemy1(random.randint(25, 575), -4680 - 2070 - 2000, 25)
enemy26 = Enemy1(random.randint(25, 575), -4750 - 2090 - 2000, 26)
enemy27 = Enemy1(random.randint(25, 575), -4840 - 2110 - 2000, 27)
enemy28 = Enemy1(random.randint(25, 575), -4900 - 2130 - 2000, 28)
enemy29 = Enemy1(random.randint(25, 575), -4980 - 2150 - 2000, 29)
enemy30 = Enemy1(random.randint(25, 575), -5060 - 2170 - 2000, 30)
enemy31 = Enemy1(random.randint(25, 575), -5140 - 2190 - 2000, 31)
enemy32 = Enemy1(random.randint(25, 575), -5200 - 2210 - 2000, 32)
enemy33 = Enemy1(random.randint(25, 575), -5300 - 2230 - 2000, 33)
enemy34 = Enemy1(random.randint(25, 575), -5430 - 2250 - 2000, 34)
enemy35 = Enemy1(random.randint(25, 575), -5590 - 2270 - 2000, 35)
enemy36 = Enemy1(random.randint(25, 575), -5720 - 2290 - 2000, 36)
enemy37 = Enemy1(random.randint(25, 575), -5840 - 2310 - 2000, 37)
enemy38 = Enemy1(random.randint(25, 575), -5970 - 2330 - 2000, 38)
enemy39 = Enemy1(random.randint(25, 575), -6100 - 2350 - 2000, 39)
enemy40 = Enemy1(random.randint(25, 575), -6200 - 2370 - 2000, 40)
enemy41 = Enemy1(random.randint(25, 575), -6310 - 2380 - 2000, 41)
enemy42 = Enemy1(random.randint(25, 575), -6420 - 2390 - 2000, 42)
enemy43 = Enemy1(random.randint(25, 575), -6600 - 2390 - 2000, 43)
enemy44 = Enemy1(random.randint(25, 575), -6660 - 2400 - 2000, 44)
enemy45 = Enemy1(random.randint(25, 575), -6800 - 2400 - 2000, 45)
enemy46 = Enemy1(random.randint(25, 575), -6800 - 2400 - 2000, 46)
boss22 = Boss(random.randint(150, 600), -22300, -22)
boss23 = Boss(random.randint(150, 600), -24300, -23)
boss24 = Boss(random.randint(150, 600), -26300, -24)
boss25 = Boss(random.randint(150, 600), -28300, -25)
healthpowerup2 = HealthPowerup(random.randint(25, 575), -9100 - 2000, -501)

enemy_list.add(enemy19)
enemy_list.add(enemy20)
enemy_list.add(enemy21)
enemy_list.add(enemy22)
enemy_list.add(enemy23)
enemy_list.add(enemy24)
enemy_list.add(enemy25)
enemy_list.add(enemy26)
enemy_list.add(enemy27)
enemy_list.add(enemy28)
enemy_list.add(enemy29)
enemy_list.add(enemy30)
enemy_list.add(enemy31)
enemy_list.add(enemy32)
enemy_list.add(enemy33)
enemy_list.add(enemy34)
enemy_list.add(enemy35)
enemy_list.add(enemy36)
enemy_list.add(enemy37)
enemy_list.add(enemy38)
enemy_list.add(enemy39)
enemy_list.add(enemy40)
enemy_list.add(enemy41)
enemy_list.add(enemy42)
enemy_list.add(enemy43)
enemy_list.add(enemy44)
enemy_list.add(enemy45)
enemy_list.add(enemy46)
enemy_list.add(boss22)
enemy_list.add(boss23)
enemy_list.add(boss24)
enemy_list.add(boss25)
boss_list.add(boss22)
boss_list.add(boss23)
boss_list.add(boss24)
boss_list.add(boss25)
enemy_list.add(healthpowerup2)


#wave6
tank2 = Tank(random.randint(25, 500), -4600, 47)
tank3 = Tank(random.randint(25, 500), -4800, 48)
tank4 = Tank(random.randint(25, 500), -5000, 49)
boss20 = Boss(random.randint(150, 500), -35700 - 2000 + 1510, -20)
boss21 = Boss(random.randint(150, 520), -35000 - 2000 + 1510, -21)
enemy_list.add(tank2)
enemy_list.add(tank3)
enemy_list.add(tank4)
enemy_list.add(boss20)
enemy_list.add(boss21)
boss_list.add(boss20)
boss_list.add(boss21)

j = 0   

pygame.mixer.music.load('Reptiles Theme.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(0)
pygame.mixer.music.load('Reptiles Theme.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(1)

##======================================================


while not done:
    j += 1
    
    screen.blit(background, (0, (-900 * 18) + j))
    screen.blit(background, (0, (-900 * 17) + j))
    screen.blit(background, (0, (-900 * 16) + j))
    screen.blit(background, (0, (-900 * 15) + j))
    screen.blit(background, (0, (-900 * 14) + j))
    screen.blit(background, (0, (-900 * 13) + j))
    screen.blit(background, (0, (-900 * 12) + j))
    screen.blit(background, (0, (-900 * 11) + j))
    screen.blit(background, (0, (-900 * 10) + j))
    screen.blit(background, (0, (-900 * 9) + j))
    screen.blit(background, (0, (-900 * 8) + j))
    screen.blit(background, (0, (-900 * 7) + j))
    screen.blit(background, (0, (-900 * 6) + j))
    screen.blit(background, (0, (-900 * 5) + j))
    screen.blit(background, (0, (-900 * 4) + j))
    screen.blit(background, (0, (-900 * 3) + j))
    screen.blit(background, (0, (-900 * 2) + j))
    screen.blit(background, (0, -900 + j))
    screen.blit(background, (0, j))
    screen.blit(background, (0, 900 + j))

    '''
    if j == 135:
        fight = pygame.mixer.Sound('fight.wav')
        fight.play()
    '''    
    

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

    pressed = pygame.key.get_pressed()
    
    
    if pressed[pygame.K_SPACE]:
        m += 1
        if (m % 2) == 0:
            laser = Laser()
            laser.rect.x = (player.x + 14)
            laser.rect.y = (player.y - 6)
            all_sprites_list.add(laser)
            laser_list.add(laser)
    
    if pressed[pygame.K_SPACE] and (m % 2) == 0:
        l = Laser()
        l.rect.x = (player.x + 61)
        l.rect.y = (player.y - 6)
        all_sprites_list.add(l)
        laser_list.add(l)
        lsound = pygame.mixer.Sound("Laser.wav")
        lsound.play()
    '''    
    if j % 20 == 0 and boss.y <= 700:
        if show_boss == True:
            bl = RLaser()
            bl2 = RLaser()
            bl.rect.x = (boss.x + 1)
            bl.rect.y = (boss.y + 50)
            bl2.rect.x = (boss.x + 19)
            bl2.rect.y = (boss.y + 50)
            all_sprites_list.add(bl)
            all_sprites_list.add(bl2)
            Rlaser_list.add(bl)
            Rlaser_list.add(bl2)
            blsound = pygame.mixer.Sound("Laser.wav")
            blsound.play()
    '''    

    enemy_list.update()
    all_sprites_list.update()
    
    
    ##boundaries
    if player.y <= 400:
        player.y = 402
    if player.y >= 633:
        player.y = 631
    if player.x >= 623:
        player.x = 621
    if player.x <= 50:
        player.x = 51   
    collide1 = True

    #Collision_Detector(laser, l, boss)        
   # boss.render(screen)
   # boss.update()
    
    player.render(screen)
    player.update()
    health.render(screen)
    health.update()
    
    #first shot
    if w1 < 2:
        shot = pygame.mixer.Sound("gunfire.wav")
        shot.play() 
        w1 += 1 
    
    
    '''
    for laser in laser_list:
        player_rlaser = sprite.collide_rect(laser, player)
        for laser in player_rlaser:
            health.health -= 1
    '''
    '''     
    pe_list = pygame.sprite.spritecollide(player, enemy_list, False)
    for player in pe_list:
        pygame.QUIT
    '''
    '''
    for bl in Rlaser_list:
        player_hitlist = pygame.sprite.spritecollide(Rlaser_list, player, False)
        for bl in player_hitlist:
            health.health -= 10
    '''   
        
    for laser in laser_list:
        enemy_hit_list = pygame.sprite.spritecollide(laser, enemy_list, False)
            
        if len(enemy_hit_list) > 0:
            for enemy in enemy_hit_list:
                if enemy.id == -1:
                    b1 += 1
                    score += 1
                    if b1 == 1:
                        show_b = False
                elif enemy.id == -2:
                    b2 += 1
                    score += 1
                    if b2 == 1:
                        show_b2 = False  
                elif enemy.id == -3:
                    b3 += 1
                    score += 1
                    if b3 == 1:
                        show_b3 = False  
                elif enemy.id == -4:
                    b4 += 1
                    score += 1
                    if b4 == 1:
                        show_b4 = False  
                elif enemy.id == -5:
                    b5 += 1
                    score += 1
                    if b5 == 1:
                        show_b5 = False          
                elif enemy.id == -6:
                    b6 += 1
                    score += 1
                    if b6 == 1:
                        show_b6 = False          
                elif enemy.id == -7:
                    b7 += 1
                    score += 1
                    if b7 == 1:
                        show_b7 = False          
                elif enemy.id == -8:
                    b8 += 1
                    score += 1
                    if b8 == 1:
                        show_b8 = False          
                elif enemy.id == -9:
                    b9 += 1
                    score += 1
                    if b9 == 1:
                        show_b9 = False  
                elif enemy.id == -10:
                    b10 += 1
                    score += 1
                    if b10 == 1:
                        show_b10 = False         
                elif enemy.id == -11:
                    b11 += 1
                    score += 1
                    if b11 == 1:
                        show_b11 = False         
                elif enemy.id == -12:
                    b12 += 1
                    score += 1
                    if b12 == 1:
                        show_b12 = False         
                elif enemy.id == -13:
                    b13 += 1
                    score += 1
                    if b13 == 1:
                        show_b13 = False         
                elif enemy.id == -14:
                    b14 += 1
                    score += 1
                    if b14 == 1:
                        show_b14 = False         
                elif enemy.id == -15:
                    b15 += 1
                    score += 1
                    if b15 == 1:
                        show_b15 = False         
                elif enemy.id == -16:
                    b16 += 1
                    score += 1
                    if b16 == 1:
                        show_b16 = False         
                elif enemy.id == -17:
                    b17 += 1
                    score += 1
                    if b17 == 1:
                        show_b17 = False         
                elif enemy.id == -18:
                    b18 += 1
                    score += 1
                    if b18 == 1:
                        show_b18 = False         
                elif enemy.id == -19:
                    b19 += 1
                    score += 1
                    if b19 == 1:
                        show_b19 = False
                        if w4 < 9:
                            shot = pygame.mixer.Sound("gunfire.wav")
                            shot.play() 
                            w4 += 1   
                elif enemy.id == -20:
                    b20 += 1
                    score += 1
                    if b20 == 1:
                        show_b20 = False         
                elif enemy.id == -21:
                    b21 += 1
                    score += 1
                    if b21 == 1:
                        show_b21 = False
                elif enemy.id == -22:
                    b22 += 1
                    score += 1
                    if b22 == 1: 
                        show_b22 = False
                elif enemy.id == -23:
                    b23 += 1
                    score += 1
                    if b23 == 1:
                        show_b23 = False        
                elif enemy.id == -24:
                    b24 += 1
                    score += 1
                    if b24 == 1:
                        show_b24 = False        
                elif enemy.id == -25:
                    b25 += 1
                    score += 1
                    if b25 == 1:        
                        show_b25 = False                 
                elif enemy.id == -500:
                    hp1n += 1
                    score += 1
                    if hp1n == 2:
                        show_hp1 = False 
                elif enemy.id == -501:
                    hp2n += 1
                    score += 1
                    if hp2n == 2:
                        show_hp2 = False   
                                               
                elif enemy.id == 1:
                    e1 += 1
                    enemy.rect.y -= 2
                    score += 1
                    if e1 ==30:
                        show_e1 = False
                elif enemy.id == 2:
                    e2 += 1
                    enemy2.rect.y -= 2
                    score += 1
                    if e2 ==30:
                        show_e2 = False
                elif enemy.id == 3:
                    e3 += 1
                    enemy3.rect.y -= 2
                    score += 1
                    if e3 ==30:
                        show_e3 = False
                elif enemy.id == 4:
                    e4 += 1
                    enemy4.rect.y -= 2
                    score += 1
                    if e4 ==30:
                        show_e4 = False
                elif enemy.id == 5:
                    e5 += 1
                    enemy5.rect.y -= 2
                    score += 1
                    if e5 ==30:
                        show_e5 = False
                elif enemy.id == 6:
                    e6 += 1
                    enemy6.rect.y -= 2
                    score += 1
                    if e6 ==30:
                        show_e6 = False
                elif enemy.id == 7:
                    e7 += 1
                    enemy7.rect.y -= 2
                    score += 1
                    if e7 ==30:
                        show_e7 = False
                elif enemy.id == 8:
                    e8 += 1
                    enemy8.rect.y -= 2
                    score += 1
                    if e8 ==30:
                        show_e8 = False
                elif enemy.id == 9:
                    e9 += 1
                    enemy9.rect.y -= 2
                    score += 1
                    if e9 ==30:
                        show_e9 = False
                        if w2 < 4:
                            shot = pygame.mixer.Sound("gunfire.wav")
                            shot.play() 
                            w2 += 1  
                elif enemy.id == 10:
                    e10 += 1
                    score += 2
                    if e10 ==210:
                        show_e10 = False  
                        if w3 < 6:
                            shot = pygame.mixer.Sound("gunfire.wav")
                            shot.play() 
                            w3 += 1     
                elif enemy.id == 11:
                    e11 += 1
                    enemy11.rect.y -= 2
                    score += 1
                    if e11 ==30:
                        show_e11 = False
                elif enemy.id == 12:
                    e12 += 1
                    enemy12.rect.y -= 2
                    score += 1
                    if e12 ==30:
                        show_e12 = False
                elif enemy.id == 13:
                    e13 += 1
                    enemy13.rect.y -= 2
                    score += 1
                    if e13 ==30:
                        show_e13 = False        
                elif enemy.id == 14:
                    e14 += 1
                    enemy14.rect.y -= 2
                    score += 1
                    if e14 ==30:
                        show_e14 = False        
                elif enemy.id == 15:
                    e15 += 1
                    enemy15.rect.y -= 2
                    score += 1
                    if e15 ==30:
                        show_e15 = False        
                elif enemy.id == 16:
                    e16 += 1
                    enemy16.rect.y -= 2
                    score += 1
                    if e16 ==30:
                        show_e16 = False        
                elif enemy.id == 17:
                    e17 += 1
                    enemy17.rect.y -= 2
                    score += 1
                    if e17 ==30:
                        show_e17 = False        
                elif enemy.id == 18:
                    e18 += 1
                    enemy18.rect.y -= 2
                    score += 1
                    if e18 ==30:
                        show_e18 = False        
                elif enemy.id == 19:
                    e19 += 1
                    enemy19.rect.y -= 2
                    score += 1
                    if e19 ==30:
                        show_e19 = False  
                elif enemy.id == 20:
                    e20 += 1
                    enemy20.rect.y -= 2
                    score += 1
                    if e20 ==30:
                        show_e20 = False         
                elif enemy.id == 21:
                    e21 += 1
                    enemy21.rect.y -= 2
                    score += 1
                    if e21 ==30:
                        show_e21 = False      
                elif enemy.id == 22:
                    e22 += 1
                    enemy22.rect.y -= 2
                    score += 1
                    if e22 ==30:
                        show_e22 = False        
                elif enemy.id == 23:
                    e23 += 1
                    enemy23.rect.y -= 2
                    score += 1
                    if e23 ==30:
                        show_e23 = False        
                elif enemy.id == 24:
                    e24 += 1
                    enemy24.rect.y -= 2
                    score += 1
                    if e24 ==30:
                        show_e24 = False        
                elif enemy.id == 25:
                    e25 += 1
                    enemy25.rect.y -= 2
                    score += 1
                    if e25 ==30:
                        show_e25 = False              
                elif enemy.id == 26:
                    e26 += 1
                    enemy26.rect.y -= 2
                    score += 1
                    if e26 ==30:
                        show_e26 = False
                elif enemy.id == 27:
                    e27 += 1
                    enemy27.rect.y -= 2
                    score += 1
                    if e27 ==30:
                        show_e27 = False
                elif enemy.id == 28:
                    e28 += 1
                    enemy28.rect.y -= 2
                    score += 1
                    if e28 ==30:
                        show_e28 = False
                elif enemy.id == 29:
                    e29 += 1
                    enemy29.rect.y -= 2
                    score += 1
                    if e29 ==30:
                        show_e29 = False
                elif enemy.id == 30:
                    e30 += 1
                    enemy30.rect.y -= 2
                    score += 1
                    if e30 ==30:
                        show_e30 = False
                elif enemy.id == 31:
                    e31 += 1
                    enemy31.rect.y -= 2
                    score += 1
                    if e31 ==30:
                        show_e31 = False
                elif enemy.id == 32:
                    e32 += 1
                    enemy32.rect.y -= 2
                    score += 1
                    if e32 ==30:
                        show_e32 = False
                elif enemy.id == 33:
                    e33 += 1
                    enemy33.rect.y -= 2
                    score += 1
                    if e33 ==30:
                        show_e33 = False
                elif enemy.id == 34:
                    e34 += 1
                    enemy34.rect.y -= 2
                    score += 1
                    if e34 ==30:
                        show_e34 = False
                elif enemy.id == 35:
                    e35 += 1
                    enemy35.rect.y -= 2
                    score += 1
                    if e35 ==30:
                        show_e35 = False
                elif enemy.id == 36:
                    e36 += 1
                    enemy36.rect.y -= 2
                    score += 1
                    if e36 ==30:
                        show_e36 = False
                elif enemy.id == 37:
                    e37 += 1
                    enemy37.rect.y -= 2
                    score += 1
                    if e37 ==30:
                        show_e37 = False
                elif enemy.id == 38:
                    e38 += 1
                    enemy38.rect.y -= 2
                    score += 1
                    if e38 ==30:
                        show_e38 = False
                elif enemy.id == 39:
                    e39 += 1
                    enemy39.rect.y -= 2
                    score += 1
                    if e39 ==30:
                        show_e39 = False
                elif enemy.id == 40:
                    e40 += 1
                    enemy40.rect.y -= 2
                    score += 1
                    if e40 ==30:
                        show_e40 = False
                elif enemy.id == 41:
                    e41 += 1
                    enemy41.rect.y -= 2
                    score += 1
                    if e41 ==30:
                        show_e41 = False
                elif enemy.id == 42:
                    e42 += 1
                    enemy42.rect.y -= 2
                    score += 1
                    if e42 ==30:
                        show_e42 = False
                elif enemy.id == 43:
                    e43 += 1
                    enemy43.rect.y -= 2
                    score += 1
                    if e43 ==30:
                        show_e43 = False
                elif enemy.id == 44:
                    e44 += 1
                    enemy44.rect.y -= 2
                    score += 1
                    if e44 ==30:
                        show_e44 = False
                elif enemy.id == 45:
                    e45 += 1
                    enemy45.rect.y -= 2
                    score += 1
                    if e45 ==30:
                        show_e45 = False
                elif enemy.id == 46:
                    e46 += 1
                    enemy46.rect.y -= 2
                    score += 1
                    if e46 ==30:
                        show_e46 = False
                        if w5 < 12:
                            shot = pygame.mixer.Sound("gunfire.wav")
                            shot.play() 
                            w5 += 1  
                elif enemy.id == 47:
                    e47 += 1
                    score += 1
                    if e47 ==250:
                        show_e47 = False               
                elif enemy.id == 48:
                    e48 += 1
                    score += 1
                    if e48 ==250:
                        show_e48 = False 
                elif enemy.id == 49:
                    e49 += 1
                    score += 1
                    if e49 ==279:
                        show_e49 = False  
                                     
                ecount += 1            
                if ecount == 1:           
                    clack = pygame.mixer.Sound("metal1.wav")
                    clack.play()                      
                if ecount == 2:
                    clack = pygame.mixer.Sound("mf.wav")
                    clack.play() 
                if ecount == 3:
                    clack = pygame.mixer.Sound("sword.wav")
                    clack.play() 
                    ecount = 0                       
            laser.kill()

            

            
        
       
   
    ##collisions:
    '''
    if show_e1 == True:    
        if player.x in range ((enemy.rect.x - 20), (enemy.rect.x +44)) and player.y in range (enemy.rect.y - 5, (enemy.rect.y + 100)):
            player.x = player.x + 10
            player.y = player.y + 10
            health.health -= 2
            e1 += 1
        if (player.x + 50) in range ((enemy.rect.x - 20), (enemy.rect.x + 44)) and (player.y + 50) in range (enemy.rect.y - 5, (enemy.rect.y + 100)):
            player.x = player.x - 10
            player.y = player.y - 10
            health.health -= 2
            e1 += 1
        if player.x in range ((enemy.rect.x - 20), (enemy.rect.x + 44)) and (player.y + 50) in range (enemy.rect.y, (enemy.rect.y - 5 + 100)):  
            player.x = player.x + 10
            player.y = player.y - 10
            health.health -= 2
            e1 += 1
        if (player.x + 50) in range ((enemy.rect.x - 20), (enemy.rect.x +44)) and player.y in range (enemy.rect.y - 5, (enemy.rect.y + 100)):
            player.x = player.x - 10
            player.y = player.y + 10
            health.health -= 2
            e1 += 1
            
            
    if show_e2 == True:    
        if player.x in range ((enemy2.rect.x - 20), (enemy2.rect.x +44)) and player.y in range (enemy2.rect.y - 5, (enemy2.rect.y + 100)):
            player.x = player.x + 10
            player.y = player.y + 10
            health.health -= 2
            e2 += 1
        if (player.x + 50) in range ((enemy.rect.x - 20), (enemy2.rect.x + 44)) and (player.y + 50) in range (enemy2.rect.y - 5, (enemy2.rect.y + 100)):
            player.x = player.x - 10
            player.y = player.y - 10
            health.health -= 2
            e2 += 1
        if player.x in range ((enemy2.rect.x - 20), (enemy2.rect.x + 44)) and (player.y + 50) in range (enemy2.rect.y, (enemy2.rect.y - 5 + 100)):  
            player.x = player.x + 10
            player.y = player.y - 10
            health.health -= 2
            e2 += 1
        if (player.x + 50) in range ((enemy2.rect.x - 20), (enemy2.rect.x +44)) and player.y in range (enemy2.rect.y - 5, (enemy2.rect.y + 100)):
            player.x = player.x - 10
            player.y = player.y + 10
            health.health -= 2
            e2 += 1        
            
    #boss
    
    if wave1 == True:
        if show_b == True:
            if player.x in range ((boss.rect.x - 20), (boss.rect.x +20)) and player.y in range (boss.rect.y - 5, (boss.rect.y + 100)):
                show_b = False
                player.y = player.y - 5
                health.health -= 15
            if (player.x + 50) in range ((boss.rect.x - 20), (boss.rect.x + 20)) and (player.y + 50) in range (boss.rect.y - 5, (boss.rect.y + 100)):
                show_b = False
                player.y = player.y - 5
                health.health -= 15
            if player.x in range ((boss.rect.x - 20), (boss.rect.x + 20)) and (player.y + 50) in range (boss.rect.y, (boss.rect.y - 5 + 100)):  
                show_b = False
                player.y = player.y - 5
                health.health -= 15
            if (player.x + 50) in range ((boss.rect.x - 20), (boss.rect.x +20)) and player.y in range (boss.rect.y - 5, (boss.rect.y + 100)):
                player.y = player.y - 5  
                health.health -= 15
                show_b = False
                
        if show_b2 == True:        
            if player.x in range ((boss2.rect.x - 20), (boss2.rect.x +20)) and player.y in range (boss2.rect.y - 5, (boss2.rect.y + 100)):
                show_b2 = False
                player.y = player.y - 5
                health.health -= 15
            if (player.x + 50) in range ((boss2.rect.x - 20), (boss2.rect.x + 20)) and (player.y + 50) in range (boss2.rect.y - 5, (boss2.rect.y + 100)):
                show_b2 = False
                player.y = player.y - 5
                health.health -= 15
            if player.x in range ((boss2.rect.x - 20), (boss2.rect.x + 20)) and (player.y + 50) in range (boss2.rect.y, (boss2.rect.y - 5 + 100)):  
                show_b2 = False
                player.y = player.y - 5
                health.health -= 15
            if (player.x + 50) in range ((boss2.rect.x - 20), (boss2.rect.x +20)) and player.y in range (boss2.rect.y - 5, (boss2.rect.y + 100)):
                player.y = player.y - 5  
                health.health -= 15  
                show_b2 = False  
    '''
    ##updater    
  
    if show_hp1 == False and hppn1 < 1:
        healthpowerup1.kill()
        health.health += 15
        hppn1 += 1
    if show_hp2 == False and hppn2 < 1:
        healthpowerup2.kill()
        health.health += 15
        hppn2 += 1    
    if show_e1 == False and ee1 < 1:
        enemy.kill()
        score += 100
        ee1 += 1
    if show_e2 == False and ee2 < 1:
        enemy2.kill()
        score += 100
        ee2 += 1       
    if show_e3 == False and ee3 < 1:
        enemy3.kill()
        score += 100
        ee3 += 1
    if show_e4 == False and ee4 < 1:
        enemy4.kill()
        score += 100
        ee4 += 1
    if show_e5 == False and ee5 < 1:
        enemy5.kill()
        score += 100
        ee5 += 1
    if show_e6 == False and ee6 < 1:
        enemy6.kill()
        score += 100
        ee6 += 1
    if show_e7 == False and ee7 < 1:
        enemy7.kill()
        score += 100
        ee7 += 1
    if show_e8 == False and ee8 < 1:
        enemy8.kill()
        score += 100
        ee8 += 1
    if show_e9 == False and ee9 < 1:
        enemy9.kill()
        score += 100
        ee9 += 1  
    if show_e10 == False and ee10 < 1:
        tank1.kill()
        score += 10000
        ee10 += 1      
    if show_e11 == False and ee11 < 1:
        enemy11.kill()
        score += 100
        ee11 += 1  
    if show_e12 == False and ee12 < 1:
        enemy12.kill()
        score += 100
        ee12 += 1  
    if show_e13 == False and ee13 < 1:
        enemy13.kill()
        score += 100
        ee13 += 1  
    if show_e14 == False and ee14 < 1:
        enemy14.kill()
        score += 100
        ee14 += 1  
    if show_e15 == False and ee15 < 1:
        enemy15.kill()
        score += 100
        ee15 += 1  
    if show_e16 == False and ee16 < 1:
        enemy16.kill()
        score += 100
        ee16 += 1  
    if show_e17 == False and ee17 < 1:
        enemy17.kill()
        score += 100
        ee17 += 1  
    if show_e18 == False and ee18 < 1:
        enemy18.kill()
        score += 100
        ee18 += 1  
    if show_b2 == False and bb2 < 1:
        boss2.kill()
        score += 15 
        bb2 += 1       
    if show_b == False and bb1 < 1:
        boss.kill()
        score += 15
        bb1 += 1
    if show_b3 == False and bb3 < 1:
        boss3.kill()
        score += 15
        bb3 += 1    
    if show_b4 == False and bb4 < 1:
        boss4.kill()
        score += 15
        bb4 += 1 
    if show_b5 == False and bb5 < 1:
        boss5.kill()
        score += 15
        bb5 += 1     
    if show_b6 == False and bb6 < 1:
        boss6.kill()
        score += 15
        bb6 += 1     
    if show_b7 == False and bb7 < 1:
        boss7.kill()
        score += 15
        bb7 += 1     
    if show_b8 == False and bb8 < 1:
        boss8.kill()
        score += 15
        bb8 += 1     
    if show_b9 == False and bb9 < 1:
        boss9.kill()
        score += 15
        bb9 += 1 
    if show_b10 == False and bb10 < 1:
        boss10.kill()
        score += 15
        bb10 += 1     
    if show_b11 == False and bb11 < 1:
        boss11.kill()
        score += 15
        bb11 += 1     
    if show_b12 == False and bb12 < 1:
        boss12.kill()
        score += 15
        bb12 += 1     
    if show_b13 == False and bb13 < 1:
        boss13.kill()
        score += 15
        bb13 += 1     
    if show_b14 == False and bb14 < 1:
        boss14.kill()
        score += 15
        bb14 += 1     
    if show_b15 == False and bb15 < 1:
        boss15.kill()
        score += 15
        bb15 += 1       
    if show_b16 == False and bb16 < 1:
        boss16.kill()
        score += 15
        bb16 += 1       
    if show_b17 == False and bb17 < 1:
        boss17.kill()
        score += 15
        bb17 += 1       
    if show_b18 == False and bb18 < 1:
        boss18.kill()
        score += 15
        bb18 += 1       
    if show_b19 == False and bb19 < 1:
        boss19.kill()
        score += 15
        bb19 += 1 
    if show_b20 == False and bb20 < 1:
        boss20.kill()
        score += 15
        bb20 += 1          
    if show_b21 == False and bb21 < 1:
        boss21.kill()
        score += 15
        bb21 += 1  
    if show_b22 == False and bb22 < 1:
        boss22.kill()
        score += 15
        bb22 += 1    
    if show_b23 == False and bb23 < 1:
        boss23.kill()
        score += 15
        bb23 += 1    
    if show_b24 == False and bb24 < 1:
        boss24.kill()
        score += 15
        bb24 += 1    
    if show_b25 == False and bb24 < 1:
        boss25.kill()
        score += 15
        bb25 += 1    
    if show_e19 == False and ee19 < 1:
        enemy19.kill()
        score += 100
        ee19 += 1  
    if show_e20 == False and ee20 < 1:
        enemy20.kill()
        score += 100
        ee20 += 1     
    if show_e21 == False and ee21 < 1:
        enemy21.kill()
        score += 100
        ee21 += 1     
    if show_e22 == False and ee22 < 1:
        enemy22.kill()
        score += 100
        ee22 += 1     
    if show_e23 == False and ee23 < 1:
        enemy23.kill()
        score += 100
        ee23 += 1     
    if show_e24 == False and ee24 < 1:
        enemy24.kill()
        score += 100
        ee24 += 1     
    if show_e25 == False and ee25 < 1:
        enemy25.kill()
        score += 100
        ee25 += 1     
    if show_e26 == False and ee26 < 1:
        enemy26.kill()
        score += 100
        ee26 += 1   
    if show_e27 == False and ee27 < 1:
        enemy27.kill()
        score += 100
        ee27 += 1         
    if show_e28 == False and ee28 < 1:
        enemy28.kill()
        score += 100
        ee28 += 1         
    if show_e29 == False and ee29 < 1:
        enemy29.kill()
        score += 100
        ee29 += 1         
    if show_e30 == False and ee30 < 1:
        enemy30.kill()
        score += 100
        ee30 += 1         
    if show_e31 == False and ee31 < 1:
        enemy31.kill()
        score += 100
        ee31 += 1         
    if show_e32 == False and ee32 < 1:
        enemy32.kill()
        score += 100
        ee32 += 1         
    if show_e33 == False and ee33 < 1:
        enemy33.kill()
        score += 100
        ee33 += 1         
    if show_e34 == False and ee34 < 1:
        enemy34.kill()
        score += 100
        ee34 += 1         
    if show_e35 == False and ee35 < 1:
        enemy35.kill()
        score += 100
        ee35 += 1         
    if show_e36 == False and ee36 < 1:
        enemy36.kill()
        score += 100
        ee36 += 1         
    if show_e37 == False and ee37 < 1:
        enemy37.kill()
        score += 100
        ee37 += 1         
    if show_e38 == False and ee38 < 1:
        enemy38.kill()
        score += 100
        ee38 += 1         
    if show_e39 == False and ee39 < 1:
        enemy39.kill()
        score += 100
        ee39 += 1         
    if show_e40 == False and ee40 < 1:
        enemy40.kill()
        score += 100
        ee40 += 1         
    if show_e41 == False and ee41 < 1:
        enemy41.kill()
        score += 100
        ee41 += 1         
    if show_e42 == False and ee42 < 1:
        enemy42.kill()
        score += 100
        ee42 += 1         
    if show_e43 == False and ee43 < 1:
        enemy43.kill()
        score += 100
        ee43 += 1         
    if show_e44 == False and ee44 < 1:
        enemy44.kill()
        score += 100
        ee44 += 1         
    if show_e45 == False and ee45 < 1:
        enemy45.kill()
        score += 100
        ee45 += 1         
    if show_e46 == False and ee46 < 1:
        enemy46.kill()
        score += 100
        ee46 += 1         
    if show_e47 == False and ee47 < 1:
        tank2.kill()
        score += 10000
        ee47 += 1
        explosion = pygame.mixer.Sound("Flashbang.wav")
        explosion.play() 
    if show_e48 == False and ee48 < 1:
        tank3.kill()
        score += 10000
        ee48 += 1
        explosion = pygame.mixer.Sound("Flashbang.wav")
        explosion.play() 
    if show_e49 == False and ee49 < 1:
        tank4.kill()
        score += 10000
        ee49 += 1
        explosion = pygame.mixer.Sound("Flashbang.wav")
        explosion.play() 
        
          
    #if collide == True and cc1 < 1:
    #    player.kill()    
    if score >= 0:
        s_g = myfont.render(str(score), 1, (35, 255, 75))
    if score <= 0:    
        s_g = myfont.render(str(score), 1, (255, 5, 15))
    screen.blit(s_g, (633, 15))    
    all_sprites_list.draw(screen)
    enemy_list.draw(screen)
    
    
    if boss.rect.y in range(650, 656):
        show_b = False
        score -= 100
        health.health -= 10
    if boss2.rect.y in range(650, 656):
        show_b2 = False
        score -= 300
        health.health -= 10
    if boss3.rect.y in range(650, 656):
        show_b3 = False
        score -= 300
        health.health -= 10   
    if boss4.rect.y in range(650, 656):
        show_b4 = False
        score -= 300
        health.health -= 10 
    if boss5.rect.y in range(650, 656):
        show_b5 = False
        score -= 300
        health.health -= 10 
    if boss6.rect.y in range(650, 656):
        show_b6 = False
        score -= 300
        health.health -= 10 
    if boss7.rect.y in range(650, 656):
        show_b7 = False
        score -= 300
        health.health -= 10 
    if boss8.rect.y in range(650, 656):
        show_b8 = False
        score -= 300
        health.health -= 10 
    if boss9.rect.y in range(650, 656):
        show_b9 = False
        score -= 300
        health.health -= 10 
    if boss10.rect.y in range(650, 656):
        show_b10 = False
        score -= 300
        health.health -= 10 
    if boss11.rect.y in range(650, 656):
        show_b11 = False
        score -= 300
        health.health -= 10 
    if boss12.rect.y in range(650, 656):
        show_b12 = False
        score -= 300
        health.health -= 10
    if boss13.rect.y in range(650, 656):
        show_b13 = False
        score -= 300
        health.health -= 10 
    if boss14.rect.y in range(650, 656):
        show_b14 = False
        score -= 300
        health.health -= 10 
    if boss15.rect.y in range(650, 656):
        show_b15 = False
        score -= 300
        health.health -= 10          
    if boss16.rect.y in range(650, 656):
        show_b16 = False
        score -= 300
        health.health -= 10     
    if boss17.rect.y in range(650, 656):
        show_b17 = False
        score -= 300
        health.health -= 10 
    if boss18.rect.y in range(650, 656):
        show_b18 = False
        score -= 300
        health.health -= 10    
    if boss19.rect.y in range(650, 656):
        show_b19 = False
        score -= 300
        health.health -= 10     
    if boss20.rect.y in range(650, 656):
        show_b20 = False
        score -= 300
        health.health -= 10      
    if boss21.rect.y in range(650, 656):
        show_b21 = False
        score -= 300
        health.health -= 10  
    if boss22.rect.y in range(650, 656):
        show_b22 = False
        score -= 300
        health.health -= 10    
    if boss23.rect.y in range(650, 656):
        show_b23 = False
        score -= 300
        health.health -= 10    
    if boss24.rect.y in range(650, 656):
        show_b24 = False
        score -= 300
        health.health -= 10    
    if boss25.rect.y in range(650, 656):
        show_b25 = False
        score -= 300
        health.health -= 10      
        
            
    if enemy.rect.y in range (650, 651):
        show_e1 = False
        score -= 200
        health.health -= 15
    if enemy2.rect.y in range (650, 651):
        show_e2 = False
        score -= 200
        health.health -= 15
    if enemy3.rect.y in range (650, 651):
        show_e3 = False
        score -= 200
        health.health -= 15
    if enemy4.rect.y in range (650, 651):
        show_e4 = False
        score -= 200
        health.health -= 15
        ee4 += 1
    if enemy5.rect.y in range (650, 651):
        show_e5 = False
        score -= 200
        health.health -= 18
    if enemy6.rect.y in range (650, 651):
        show_e6 = False
        score -= 200
        health.health -= 18
    if enemy7.rect.y in range (650, 651):
        show_e7 = False
        score -= 200
        health.health -= 18
    if enemy8.rect.y in range (650, 651):
        show_e8 = False
        score -= 200
        health.health -= 18
    if enemy9.rect.y in range (650, 651):
        show_e9 = False
        score -= 200
        health.health -= 18
    if tank1.rect.y in range (650, 651):
        show_e10 = False
        score -= 1000
        health.health -= 20
    if enemy11.rect.y in range (650, 651):
        show_e11 = False
        score -= 200
        health.health -= 18
    if enemy12.rect.y in range (650, 651):
        show_e12 = False
        score -= 200
        health.health -= 18
    if enemy13.rect.y in range (650, 651):
        show_e13 = False
        score -= 200
        health.health -= 18
    if enemy14.rect.y in range (650, 651):
        show_e14 = False
        score -= 200
        health.health -= 18
    if enemy15.rect.y in range (650, 651):
        show_e15 = False
        score -= 200
        health.health -= 18
    if enemy16.rect.y in range (650, 651):
        show_e16 = False
        score -= 200
        health.health -= 18
    if enemy17.rect.y in range (650, 651):
        show_e17 = False
        score -= 200
        health.health -= 18
    if enemy18.rect.y in range (650, 651):
        show_e18 = False
        score -= 200
        health.health -= 18
    if enemy19.rect.y in range (650, 651):
        show_e19 = False
        score -= 200
        health.health -= 18                                  
    if enemy20.rect.y in range (650, 651):
        show_e20 = False
        score -= 200
        health.health -= 18                        
    if enemy21.rect.y in range (650, 651):
        show_e21 = False
        score -= 200
        health.health -= 18
    if enemy22.rect.y in range (650, 651):
        show_e22 = False
        score -= 200
        health.health -= 18
    if enemy23.rect.y in range (650, 651):
        show_e23 = False
        score -= 200
        health.health -= 18
    if enemy24.rect.y in range (650, 651):
        show_e24 = False
        score -= 200
        health.health -= 18
    if enemy25.rect.y in range (650, 651):
        show_e25 = False
        score -= 200
        health.health -= 18
    if enemy26.rect.y in range (650, 651):
        show_e26 = False
        score -= 200
        health.health -= 18
    if enemy27.rect.y in range (650, 651):
        show_e27 = False
        score -= 200
        health.health -= 18
    if enemy28.rect.y in range (650, 651):
        show_e28 = False
        score -= 200
        health.health -= 18
    if enemy29.rect.y in range (650, 651):
        show_e29 = False
        score -= 200
        health.health -= 18
    if enemy30.rect.y in range (650, 651):
        show_e30 = False
        score -= 200
        health.health -= 18
    if enemy31.rect.y in range (650, 651):
        show_e31 = False
        score -= 200
        health.health -= 18
    if enemy32.rect.y in range (650, 651):
        show_e32 = False
        score -= 200
        health.health -= 18
    if enemy33.rect.y in range (650, 651):
        show_e33 = False
        score -= 200
        health.health -= 18
    if enemy34.rect.y in range (650, 651):
        show_e34 = False
        score -= 200
        health.health -= 18
    if enemy35.rect.y in range (650, 651):
        show_e35 = False
        score -= 200
        health.health -= 18
    if enemy36.rect.y in range (650, 651):
        show_e36 = False
        score -= 200
        health.health -= 18
    if enemy37.rect.y in range (650, 651):
        show_e37 = False
        score -= 200
        health.health -= 18
    if enemy38.rect.y in range (650, 651):
        show_e38 = False
        score -= 200
        health.health -= 18
    if enemy39.rect.y in range (650, 651):
        show_e39 = False
        score -= 200
        health.health -= 18
    if enemy40.rect.y in range (650, 651):
        show_e40 = False
        score -= 200
        health.health -= 18
    if enemy41.rect.y in range (650, 651):
        show_e41 = False
        score -= 200
        health.health -= 18
    if enemy42.rect.y in range (650, 651):
        show_e42 = False
        score -= 200
        health.health -= 18
    if enemy43.rect.y in range (650, 651):
        show_e43 = False
        score -= 200
        health.health -= 18
    if enemy44.rect.y in range (650, 651):
        show_e44 = False
        score -= 200
        health.health -= 18
    if enemy45.rect.y in range (650, 651):
        show_e45 = False
        score -= 200
        health.health -= 18
    if enemy46.rect.y in range (650, 651):
        show_e46 = False
        score -= 200
        health.health -= 18
    if tank2.rect.y in range (650, 651):
        show_e47 = False
        score -= 2000
        health.health -= 38
    if tank3.rect.y in range (650, 651):
        show_e48 = False
        score -= 2000
        health.health -= 38
    if tank4.rect.y in range (650, 651):
        show_e49 = False
        score -= 2000
        health.health -= 38    
        
            
    if health.health >= 100:
        health.health = 100
        
    if ee4 >= 1:
        wave1 = True 
        cn1 == True 
    if ee9 >= 1:
        wave2 = True
        wave1 = False 
    if e18 >= 1:
        wave2 = False
        wave3 = True 
    if bb19 >= 1:
        wave3 = False
        wave4 = True    
    if ee46 >= 1:
        wave4 = False
    if ee49 >= 1:
        health.health = 0    
                  
              
        
           
    if j < 340:
        screen.blit(number1, (95, 4))
        if w1 < 2:
            shot = pygame.mixer.Sound("gunfire.wav")
            shot.play() 
            w1 += 1 
    
    if wave1 == True:    
        screen.blit(number2, (95, 4))

    if wave2 == True and wave1 != True:
        screen.blit(number3, (95, 4)) 
        
    if wave3 == True and wave2 != True:
        screen.blit(number4, (95, 4))    

    if wave4 == True and wave3 != True:
        screen.blit(number5, (95, 4))  


     
     
     
    screen.blit(lside, (-38, (-700 * 12) + j)) 
    screen.blit(lside2, (-38, (-700 * 11) + j)) 
    screen.blit(lside, (-38, (-700 * 10) + j)) 
    screen.blit(lside, (-38, (-700 * 9) + j))                 
    screen.blit(lside, (-38, (-700 * 8) + j))
    screen.blit(lside, (-38, (-700 * 7) + j))
    screen.blit(lside, (-38, (-700 * 6) + j))
    screen.blit(lside, (-38, (-700 * 5) + j))
    screen.blit(lside2, (-38, (-700 * 4) + j))
    screen.blit(lside, (-38, (-700 * 3) + j))
    screen.blit(lside, (-38, (-700 * 2) + j))
    screen.blit(lside2, (-38, (-700 * 1) + j))
    screen.blit(lside, (-38, j))
    screen.blit(lside2, (-38, 700 + j))
    
    
    screen.blit(wave, (5, 5))
    
    if health.health <= 0:
        black = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 700, 700))
        screen.blit(gameover, (175, 270))
        g += 1
        j -= 1
        
        #tank1  = enemy10/ 21b/46e
        
        
        enemy.rect.y = -90000000
        enemy2.rect.y = -90000000
        enemy3.rect.y = -90000000
        enemy4.rect.y = -90000000
        enemy5.rect.y = -90000000
        enemy6.rect.y = -90000000 
        enemy7.rect.y = -90000000 
        enemy8.rect.y = -90000000 
        enemy9.rect.y = -90000000 
        tank1.rect.y = -90000000 
        enemy11.rect.y = -90000000 
        enemy12.rect.y = -90000000 
        enemy13.rect.y = -90000000 
        enemy14.rect.y = -90000000 
        enemy15.rect.y = -90000000 
        enemy16.rect.y = -90000000 
        enemy17.rect.y = -90000000 
        enemy18.rect.y = -90000000 
        enemy19.rect.y = -90000000 
        enemy20.rect.y = -90000000 
        enemy21.rect.y = -90000000 
        enemy22.rect.y = -90000000 
        enemy23.rect.y = -90000000
        enemy24.rect.y = -90000000 
        enemy25.rect.y = -90000000 
        enemy26.rect.y = -90000000 
        enemy27.rect.y = -90000000 
        enemy28.rect.y = -90000000 
        enemy29.rect.y = -90000000 
        enemy30.rect.y = -90000000 
        enemy31.rect.y = -90000000 
        enemy32.rect.y = -90000000 
        enemy33.rect.y = -90000000 
        enemy34.rect.y = -90000000 
        enemy35.rect.y = -90000000  
        enemy36.rect.y = -90000000 
        enemy37.rect.y = -90000000  
        enemy38.rect.y = -90000000  
        enemy39.rect.y = -90000000  
        enemy40.rect.y = -90000000  
        enemy41.rect.y = -90000000  
        enemy42.rect.y = -90000000  
        enemy43.rect.y = -90000000
        enemy44.rect.y = -90000000  
        enemy45.rect.y = -90000000  
        enemy46.rect.y = -90000000
        tank2.rect.y = -90000000
        tank3.rect.y = -90000000
        tank4.rect.y = -99999999
        
        boss.rect.y = -90000000
        boss2.rect.y = -90000000
        boss3.rect.y = -90000000
        boss4.rect.y = -90000000
        boss5.rect.y = -90000000
        boss6.rect.y = -90000000 
        boss7.rect.y = -90000000 
        boss8.rect.y = -90000000 
        boss9.rect.y = -90000000 
        boss10.rect.y = -90000000 
        boss11.rect.y = -90000000 
        boss12.rect.y = -90000000 
        boss13.rect.y = -90000000 
        boss14.rect.y = -90000000 
        boss15.rect.y = -90000000 
        boss16.rect.y = -90000000 
        boss17.rect.y = -90000000 
        boss18.rect.y = -90000000 
        boss19.rect.y = -90000000 
        boss20.rect.y = -90000000 
        boss21.rect.y = -90000000 
        boss22.rect.y = -90000000 
        boss23.rect.y = -90000000 
        boss24.rect.y = -90000000   
        boss25.rect.y = -90000000   
          
        screen.blit("Score"+ s_g, (300, 410))
    
    pygame.display.update()
    clock.tick(30)

if g > 20:        
    pygame.quit()    
