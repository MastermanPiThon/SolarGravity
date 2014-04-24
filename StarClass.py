#Import Library
import math
import random
import pygame

#import pygame.locals import * (what is this??)


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

    def positionX(self, xplayer, scale):
        """ Relative Abscissa Position """
        return int(-xplayer * scale + 320)

    def positionY(self, yplayer, scale):
        """ Relative Ordinate Position """
        return int(-yplayer * scale + 240)
    
    def draw(self, screen, xplayer, yplayer, scale):
        size = self.size
        color = self.color
        x = self.positionX(xplayer, scale)
        y = self.positionY(yplayer, scale)
        pygame.draw.circle(screen, color, (x,y), size, 0)
