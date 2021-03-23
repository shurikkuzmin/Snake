# -*- coding: utf-8 -*-
"""
Created on 

"""

import pygame
from pygame.locals import *
import random
import numpy

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()


FIELDWIDTH = 10
FIELDHEIGHT = 10

field = numpy.zeros((FIELDHEIGHT, FIELDWIDTH), dtype=numpy.int16)

anaconda = [[7,4], [6,4], [5,4], [4,4], [3,4]]


SURFACE = pygame.display.set_mode((32 * FIELDWIDTH, 32 * FIELDHEIGHT))



snake = pygame.image.load("snake.png")

head = snake.subsurface(3 * 64, 0, 64, 64)
head = pygame.transform.scale(head, (32, 32))
body = snake.subsurface(2 * 64, 64, 64, 64)
body = pygame.transform.scale(body, (32, 32))
tail = snake.subsurface(3 * 64, 2 * 64, 64, 64)
tail = pygame.transform.scale(tail, (32, 32))

def drawField():
    field[:,:] = 0
    
    for segment in anaconda:
        field[segment[0]][segment[1]] = 2
    field[anaconda[0][0]][anaconda[0][1]] = 1
    field[anaconda[-1][0]][anaconda[-1][1]] = 3
    
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i][j] == 1:
                SURFACE.blit(tail, (j * 32, i * 32))
            elif field[i][j] == 2:
                SURFACE.blit(body, (j * 32, i * 32))
            elif field[i][j] == 3:
                SURFACE.blit(head, (j * 32, i * 32))
                
def moveSnake():
    pass


SPEEDSNAKE = 3
SPEED = 60

gameCounter = 0
isRunning = True
while isRunning:
    SURFACE.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
    
    if gameCounter % (SPEED / SPEEDSNAKE) == 0:
        moveSnake()
    
    drawField()
    
    clock.tick(SPEED)
    
    pygame.display.update()
    
    gameCounter = gameCounter + 1
    
pygame.quit()