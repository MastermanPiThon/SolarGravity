#Import Library
import math
import random
import pygame
from PlanetClass.py import *
from PlayerClass.py import *
from StarClass.py import *

#import pygame.locals import * (what is this??)

#initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
 
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
    objects = [sun, mercury, venus]

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
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            

#define the class planet
class planet:
    """ a planet """
    def __init__(self, size, distance, color, ipos, mass):
        self.size = size
        self.distance = distance
        self.color = color
        self.ipos = ipos
        self.mass = mass

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

    def positionX(self, t, player, objects, timeinterval, scale):
        ''' Relative Abscissa Position '''
        xme = self.positionx(t)
        xit = player.position(objects, t, timeinterval)
        X = (xme - xit)/scale + 320
        return X
        
    #def positionY(self,t):
        
    
    def draw(self, screen, t):
        size = self.size
        color = self.color
        x = int(self.positionx(t) + 320)
        y = int(self.positiony(t) + 240)
        pygame.draw.circle(screen, color, (x,y), size, 0)

#define the star class
class star:
    def __init__(self, size, color, mass):
        self.size = size
        self.color = color
        self.mass = mass

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
    def __init__(self, size, color, Sx, Sy, Vx, Vy):
        self.size = size
        self.color = color
        self.Sx = Sx
        self.Sy = Sy
        self.Vx = Vx
        self.Vy = Vy
        self.Ax = 0.0
        self.Ay = 0.0
        #self.xarray = [x,x]
        #self.yarray = [y,y]
        #self.varray = [vx,vy]
        #self.aarray = [0,0]
        

    def position(self, objects, t, ∆t):
        """ Absolute Position """
        #xarray[0] = xarray[1]
        #yarray[0] = yarray[1]
        Sx = self.Sx
        Sy = self.Sy
        Vx = self.Vx
        Vy = self.Vy
        Ax = self.Ax
        Ay = self.Ay
        
        #S i+1 redefinition
        Sx += Vx * ∆t
        Sy += Vy * ∆t
        
        #A i+1 redefinition
        Ax = 0.0
        Ay = 0.0
        
        for planet in objects:
            xdistance = planet.positionx(t) - Sx
            ydistance = planet.positiony(t) - Sy
            r = (xdistance ** 2 + ydistance ** 2) ** 0.5
            Ax += planet.mass / r ** 3 * xdistance
            Ay += planet.mass / r ** 3 * ydistance
        #INSERT Player input
        
        #V i+3/2 redefinition
        Vx += Ax * ∆t
        Vy += Ay * ∆t
        
        
        return {'x' : Sx, 'y' : Sy}
        
        '''
        for planet in objects:
            xdistance = planet.positionx(t) - xarray[0]
            ydistance = planet.positiony(t) - yarray[0]
            r = (xdistance ** 2 + ydistance ** 2) ** 0.5
            aarray[0] += planet.mass / r ** 3 * xdistance
            aarray[1] += planet.mass / r ** 3 * ydistance

        #player input here
        
        
        varray[0] += aarray[0]*timeinterval
        varray[1] += aarray[1]*timeinterval

        xarray[1] = varray[0]*timeinterval
        yarray[1] = varray[1]*timeinterval

        aarray = [0,0]
        
        return [xarray[1], yarray[1]]
        '''

    #def positionX(self,t):
        
        
    #def positionY(self,t):
        
    
    def draw(self, screen, t):
        size = self.size
        color = self.color
        x = int(self.positionx(t) + 320)
        y = int(self.positiony(t) + 240)
        pygame.draw.circle(screen, color, (x,y), size, 0)
