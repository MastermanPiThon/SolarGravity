#Import Library
import math
import random
import pygame
from PlanetClass import *
from PlayerClass import *
from StarClass import *

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
