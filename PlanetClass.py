#Import Library
import math
import random
import pygame

#from pygame.locals import * (what is this??)

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
