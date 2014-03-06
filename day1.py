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
        """ some mathy function """
        R = self.distance
        i = self.ipos
        x = R * math.cos((t+i) / (R ** 1.5))
        return x

    def positiony(self, t):
        """ some other mathy function """
        R = self.distance
        i = self.ipos
        y = R * math.sin((t+i) / (R ** 1.5))
        return y

    def positionX(self,t):
        
    
    def drawme(self, screen, t):
        size = self.size
        color = self.color
        x = self.positionx(self, t) + 250
        y = self.positiony(self, t) + 250
        pygame.draw.circle(screen, color, (x,y), size, 0)
            
#class player:
    

t=0
tick0 = pygame.time.get_ticks()
tick1 = pygame.time.get_ticks()
while 1:
    screen.fill(0)
    x = int(math.floor(50*math.cos(t)))
    y = int(math.floor(30*math.sin(t)))
    pygame.draw.circle(screen, 0x3366FF, (250+ x,250 + y), 10, 0)
    pygame.draw.circle(screen, 0x3366FF, (250+ 2*x,250 + 2*y), 10, 0)
    tick1 = pygame.time.get_ticks()
    t+=(tick1-tick0)/200.0
    tick0 = tick1
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
