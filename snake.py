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


FIELDWIDTH = 20
FIELDHEIGHT = 20

field = numpy.zeros((FIELDHEIGHT, FIELDWIDTH), dtype=numpy.int16)

anaconda = [[7,4], [6,4], [5,4], [4,4], [3,4]]


SURFACE = pygame.display.set_mode((32 * FIELDWIDTH, 32 * FIELDHEIGHT))



snake = pygame.image.load("snake.png")

headNorth = snake.subsurface(3 * 64, 0, 64, 64) #1
headNorth = pygame.transform.scale(headNorth, (32, 32))
headSouth = snake.subsurface(4 * 64, 64, 64, 64) #2
headSouth = pygame.transform.scale(headSouth, (32, 32))
headWest = snake.subsurface(3 * 64, 64, 64, 64) #3
headWest = pygame.transform.scale(headWest, (32, 32))
headEast = snake.subsurface(4 * 64, 0, 64, 64) #4
headEast = pygame.transform.scale(headEast, (32, 32))

bodyVertical = snake.subsurface(2 * 64, 64, 64, 64) #5
bodyVertical = pygame.transform.scale(bodyVertical, (32, 32))
bodyHorizontal = snake.subsurface(64, 0, 64, 64) #6
bodyHorizontal = pygame.transform.scale(bodyHorizontal, (32, 32))

tailNorth = snake.subsurface(3 * 64, 2 * 64, 64, 64) #7
tailNorth = pygame.transform.scale(tailNorth, (32, 32))
tailSouth = snake.subsurface(4 * 64, 3 * 64, 64, 64) #8
tailSouth = pygame.transform.scale(tailSouth, (32, 32))
tailWest = snake.subsurface(3 * 64, 3 * 64, 64, 64) #9
tailWest = pygame.transform.scale(tailWest, (32, 32))
tailEast = snake.subsurface(4 * 64, 2 * 64, 64, 64) #10
tailEast = pygame.transform.scale(tailEast, (32, 32))

joint1 = snake.subsurface(0, 0, 64, 64) #11
joint1 = pygame.transform.scale(joint1, (32, 32))
joint2 = snake.subsurface(0, 64, 64, 64) #12
joint2 = pygame.transform.scale(joint2, (32, 32))
joint3 = snake.subsurface(2 * 64, 0, 64, 64) #13
joint3 = pygame.transform.scale(joint3, (32, 32))
joint4 = snake.subsurface(2 * 64, 2 * 64, 64, 64) #14
joint4 = pygame.transform.scale(joint4, (32, 32))

def drawField():
    field[:,:] = 0
    
    for segment in anaconda:
        field[segment[0]][segment[1]] = 5
    field[anaconda[0][0]][anaconda[0][1]] = 7
    field[anaconda[-1][0]][anaconda[-1][1]] = 1
    
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i][j] == 1:
                SURFACE.blit(headNorth, (j * 32, i * 32))
            elif field[i][j] == 2:
                SURFACE.blit(headSouth, (j * 32, i * 32))
            elif field[i][j] == 3:
                SURFACE.blit(headWest, (j * 32, i * 32))
            elif field[i][j] == 4:
                SURFACE.blit(headEast, (j * 32, i * 32))
            elif field[i][j] == 5:
                SURFACE.blit(bodyVertical, (j * 32, i * 32))
            elif field[i][j] == 6:
                SURFACE.blit(bodyHorizontal, (j * 32, i* 32))
            elif field[i][j] == 7:
                SURFACE.blit(tailNorth, (j * 32, i * 32))
                
def moveSnake(direction):
    headSegment = anaconda[-1]
    
    if direction == "Up":
        newRow = headSegment[0] - 1
        newColumn = headSegment[1]
    if direction == "Down":
        newRow = headSegment[0] + 1
        newColumn = headSegment[1]
    if direction == "Left":
        newRow = headSegment[0]
        newColumn = headSegment[1] - 1
    if direction == "Right":
        newRow = headSegment[0]
        newColumn = headSegment[1] + 1
    
    if newRow == -1:
        newRow = FIELDHEIGHT-1
    if newRow == FIELDHEIGHT:
        newRow = 0
    if newColumn == -1:
        newColumn = FIELDWIDTH - 1
    if newColumn == FIELDWIDTH:
        newColumn = 0
    anaconda.append([newRow, newColumn])
    anaconda.pop(0)


SPEEDSNAKE = 3
SPEED = 60

gameCounter = 0
isRunning = True
direction = "Up"
oldDirection = "Up"
while isRunning:
    SURFACE.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
            if event.key == K_UP and oldDirection != "Down":
                direction = "Up"
            if event.key == K_DOWN and oldDirection != "Up":
                direction = "Down"
            if event.key == K_LEFT and oldDirection != "Right":
                direction = "Left"
            if event.key == K_RIGHT and oldDirection != "Left":
                direction = "Right"
    
    if gameCounter % (SPEED / SPEEDSNAKE) == 0:
        oldDirection = direction
        moveSnake(direction)
    
    drawField()
    
    clock.tick(SPEED)
    
    pygame.display.update()
    
    gameCounter = gameCounter + 1
    
pygame.quit()