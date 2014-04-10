#Import Library
import math
import random
import pygame

#import pygame.locals import * (what is this??)

class player:
    def __init__(self, size, color, Sx, Sy, Vx, Vy):
        self.size = size
        self.color = color
        self.distx = Sx
        self.disty = Sy
        self.velx = Vx
        self.vely = Vy
        self.accex = 0.0
        self.accey = 0.0
        #self.xarray = [x,x]
        #self.yarray = [y,y]
        #self.varray = [vx,vy]
        #self.aarray = [0,0]
        

    def position(self, objects, t, Deltat):
        """ Absolute Position """
        #xarray[0] = xarray[1]
        #yarray[0] = yarray[1]
        Sx = self.distx
        Sy = self.disty
        Vx = self.velx
        Vy = self.vely
        Ax = self.accex
        Ay = self.accey

        
        #S i+1 redefinition
        Sx += Vx * Deltat
        Sy += Vy * Deltat
        
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
        Vx += Ax * Deltat
        Vy += Ay * Deltat
        
        
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
        x = 320
        y = 240
        pygame.draw.polygon(screen, color, [[x, y + size ], [x - size, y + size], [x + size, y + size]], 0)
        
        
