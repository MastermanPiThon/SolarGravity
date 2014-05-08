#Import Library
import math
import random
import pygame

#import pygame.locals import * (what is this??)

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
        

    def position(self, planets, star, t, Deltat):
        """ Absolute Position """

        #S i+1 redefinition
        self.Sx += self.Vx * Deltat
        self.Sy += self.Vy * Deltat
        
        #A i+1 redefinition
        self.Ax = 0.0
        self.Ay = 0.0
        for planet in planets:
            xdistance = planet.positionx(t) - self.Sx
            ydistance = planet.positiony(t) - self.Sy
            r = (xdistance ** 2 + ydistance ** 2) ** 0.5 + 10
            print r
            self.Ax += planet.mass / r ** 3 * xdistance
            self.Ay += planet.mass / r ** 3 * ydistance
        xdistance = star.positionx() - self.Sx
        ydistance = star.positiony() - self.Sy
        r = (xdistance ** 2 + ydistance ** 2) ** 0.5 + 10
        print r
        self.Ax += planet.mass / r ** 3 * xdistance
        self.Ay += planet.mass / r ** 3 * ydistance
        #INSERT Player input
        
        #V i+3/2 redefinition
        self.Vx += self.Ax * Deltat
        self.Vy += self.Ay * Deltat
        
        
        return {'x' : self.Sx, 'y' : self.Sy}
        
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
        
   
    def positionX(self,t):
        """ Relative Abscissa Position """
        return 320
        
    def positionY(self,t):
        """ Relative Ordinate Position """
        return 2
    '''
    def draw(self, screen):
        size = self.size
        color = self.color
        x = 320
        y = 240
        pygame.draw.circle(screen, color, (x,y), size, 0)
        #pygame.draw.polygon(screen, color, [[x, y + size ], [x - size, y + size], [x + size, y + size]], 0)
        
        
