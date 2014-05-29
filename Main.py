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

#Create Objects
sun = star(15, 0xeee8aa, 70)
mercury = planet(5, 50, 0x3366FF, 0, .1)
venus = planet(10, 100, 0xFFCC66, 0, .1)
me = player(10, 0xFFFFFF, 75, -30, 0, 0)
planets = [mercury, venus]

#initialize time
t=0
deltat = 10
tick0 = pygame.time.get_ticks()
tick1 = pygame.time.get_ticks()

#initialize input
keys = [False, False, False, False]

while 1:
    screen.fill(0)

    #register Player Input
    for event in pygame.event.get():
        # check if the event is the X button 
        #if event.type==pygame.QUIT:
            # if it is quit the game
            #pygame.quit() 
            #exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False 
    
    # Find Player Position
    splayer = me.position(planets, sun, t, deltat, keys)
    xplayer = splayer['x']
    yplayer = splayer['y']

    # Drawing
    sun.draw(screen, xplayer, yplayer, 1)
    mercury.draw(screen, xplayer, yplayer, 1, t)
    venus.draw(screen, xplayer, yplayer, 1, t)
    me.draw(screen, keys)

    # Time Handling
    tick1 = pygame.time.get_ticks()
    deltat = (tick1-tick0)*1.0
    t+=deltat
    tick0 = tick1

    # The Flip
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
            

    
    
