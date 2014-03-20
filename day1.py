#Import Library
import math
import random
import pygame

#import pygame.locals import * (what is this??)

#initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#define the class planet
class planet:
    """ a planet """
    def __init__(self, size, distance, color, ipos):
        self.size = size
        self.distance = distance
        self.color = color
        self.ipos = ipos

    def positionx(self, t):
        """ Absolute Abscissa Position """
        R = self.distance
        i = self.ipos
        x = R * math.cos((t+i) / (R ** 1.5))
        return x

    def positiony(self, t):
        """ Absolute Ordinate Position """
        R = self.distance
        i = self.ipos
        y = R * math.sin((t+i) / (R ** 1.5))
        return y

    #def positionX(self,t):
        
        
    #def positionY(self,t):
        
    
    def draw(self, screen, t):
        size = self.size
        color = self.color
        x = int(self.positionx(t) + 320)
        y = int(self.positiony(t) + 240)
        pygame.draw.circle(screen, color, (x,y), size, 0)

#define the star class
class star:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def positionx(self):
        """ Absolute Abscissa Position """
        return 0

    def positiony(self):
        """ Absolute Ordinate Position """
        return 0

    def draw(self, screen):
        size = self.size
        color = self.color
        x = int(self.positionx() + 320)
        y = int(self.positiony() + 240)
        pygame.draw.circle(screen, color, (x,y), size, 0)

            
class player:
    fuel = 0
    def __init__(self, size, color, x0, y0):
        self.size = size
        self.color = color
        self.x0 = x0
        self.y0 = y0

    def positionx(self, t):
        """ Absolute Abscissa Position """
        R = self.distance
        i = self.ipos
        x = R * math.cos((t+i) / (R ** 1.5))
        return x

    def positiony(self, t):
        """ Absolute Ordinate Position """
        R = self.distance
        i = self.ipos
        y = R * math.sin((t+i) / (R ** 1.5))
        return y

    #def positionX(self,t):
        
        
    #def positionY(self,t):
        
    
    def draw(self, screen, t):
        size = self.size
        color = self.color
        x = int(self.positionx(t) + 320)
        y = int(self.positiony(t) + 240)
        pygame.draw.circle(screen, color, (x,y), size, 0)

t=0
tick0 = pygame.time.get_ticks()
tick1 = pygame.time.get_ticks()
while 1:
    screen.fill(0)
    sun = star(15, 0xeee8aa)
    mercury = planet(5, 50, 0x3366FF, 0)
    venus = planet(10, 100, 0x4B0082, 0)
    #x = int(math.floor(50*math.cos(t)))
    #y = int(math.floor(30*math.sin(t)))
    #pygame.draw.circle(screen, 0x3366FF, (250+ x,250 + y), 10, 0)
    #pygame.draw.circle(screen, 0x3366FF, (250+ 2*x,250 + 2*y), 10, 0)
    sun.draw(screen)
    mercury.draw(screen, t)
    venus.draw(screen, t)

    # Time Handling
    tick1 = pygame.time.get_ticks()
    t+=(tick1-tick0)*1.0
    tick0 = tick1

    # The Flip
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
