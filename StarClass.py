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

    def draw(self, screen):
        size = self.size
        color = self.color
        x = int(self.positionx() + 320)
        y = int(self.positiony() + 240)
        pygame.draw.circle(screen, color, (x,y), size, 0)
