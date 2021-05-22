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

def generateApple(mcintosh): 
    notGenerated = True  
    while notGenerated:
        newRow = random.randint(0,FIELDHEIGHT - 1)
        newColumn = random.randint(0,FIELDWIDTH - 1)
        
        notGenerated = False
        for segment in anaconda:
            if segment[0] == newRow and segment[1] == newColumn:
                notGenerated = True
                break
    
    mcintosh[0] = newRow 
    mcintosh[1] = newColumn

mcintosh = [0,0]
generateApple(mcintosh)
counterApple = 0

SURFACE = pygame.display.set_mode((32 * FIELDWIDTH, 32 * FIELDHEIGHT))

font = pygame.font.SysFont("Comic Sans MS", 50, bold=5)
fontCounter = pygame.font.SysFont("Comic Sans MS", 25, bold=2)

gameOverText = font.render("Game Over", False, BLUE)
gameOverRect = gameOverText.get_rect()
gameOverRect.centerx = 16 * FIELDWIDTH
gameOverRect.centery = 16 * FIELDHEIGHT

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

apple = snake.subsurface(0, 3 * 64, 64, 64) #15
apple = pygame.transform.scale(apple, (32, 32))

sprites = []
for i in range(0, 4):
    for j in range(0, 5):
        tempSprite = snake.subsurface(j * 64, i * 64, 64, 64) 
        tempSprite = pygame.transform.scale(tempSprite, (32, 32))
        sprites.append(tempSprite)

def drawField(oldDirection):
    field[:,:] = 0
    
    field[mcintosh[0]][mcintosh[1]] = 15
    
    
    tailCoors = anaconda[0]
    nextTailCoors = anaconda[1]
    
    if tailCoors[0] == nextTailCoors[0]:
        if (nextTailCoors[1] == tailCoors[1] + 1) or ((tailCoors[1] == FIELDWIDTH - 1) and (nextTailCoors[1] == 0)):
            field[tailCoors[0]][tailCoors[1]] = 10
        if (nextTailCoors[1] == tailCoors[1] - 1) or (tailCoors[1] == 0 and (nextTailCoors[1] == FIELDWIDTH - 1)):
            field[tailCoors[0]][tailCoors[1]] = 9
    else:
        if (nextTailCoors[0] == tailCoors[0] + 1) or ((tailCoors[0] == FIELDHEIGHT - 1) and (nextTailCoors[0] == 0)):
            field[tailCoors[0]][tailCoors[1]] = 8
        if (nextTailCoors[0] == tailCoors[0] - 1) or (tailCoors[0] == 0 and (nextTailCoors[0] == FIELDHEIGHT - 1)):
            field[tailCoors[0]][tailCoors[1]] = 7
            
    headCoors = anaconda[-1]
    if oldDirection == "Up":
        field[headCoors[0]][headCoors[1]] = 1
    if oldDirection == "Down":
        field[headCoors[0]][headCoors[1]] = 2
    if oldDirection == "Left":
        field[headCoors[0]][headCoors[1]] = 3
    if oldDirection == "Right":
        field[headCoors[0]][headCoors[1]] = 4
    
    for i in range(1, len(anaconda)-1):
        prevCoors = anaconda[i-1]
        nextCoors = anaconda[i+1]
        coors = anaconda[i]
        if coors[0] == prevCoors[0] and coors[0] == nextCoors[0]:
            field[coors[0]][coors[1]] = 6
        if coors[1] == prevCoors[1] and coors[1] == nextCoors[1]:
            field[coors[0]][coors[1]] = 5
        if nextCoors[0] < prevCoors[0]:
            if coors[0] == prevCoors[0]:
                if nextCoors[1] > prevCoors[1]:
                    field[coors[0]][coors[1]] = 14
                else:
                    field[coors[0]][coors[1]] = 12
            if coors[0] == nextCoors[0]:
                if nextCoors[1] > prevCoors[1]:
                    field[coors[0]][coors[1]] = 11
                else:
                    field[coors[0]][coors[1]] = 13
        if nextCoors[0] > prevCoors[0]: 
            if coors[0] == prevCoors[0]:
                if nextCoors[1] < prevCoors[1]:
                    field[coors[0]][coors[1]] = 11
                else:
                    field[coors[0]][coors[1]] = 13
            if coors[0] == nextCoors[0]:
                if nextCoors[1] < prevCoors[1]:
                    field[coors[0]][coors[1]] = 14
                else:
                    field[coors[0]][coors[1]] = 12
            
    
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            #SURFACE.blit(sprites[field[i][j]], j*32, i*32)
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
            elif field[i][j] == 8:
                SURFACE.blit(tailSouth, (j * 32, i * 32))
            elif field[i][j] == 9:
                SURFACE.blit(tailWest, (j * 32, i * 32))
            elif field[i][j] == 10:
                SURFACE.blit(tailEast, (j * 32, i * 32))
            elif field[i][j] == 11:
                SURFACE.blit(joint1, (j * 32, i * 32))
            elif field[i][j] == 12:
                SURFACE.blit(joint2, (j * 32, i * 32))
            elif field[i][j] == 13:
                SURFACE.blit(joint3, (j * 32, i * 32))
            elif field[i][j] == 14:
                SURFACE.blit(joint4, (j * 32, i * 32))
            elif field[i][j] == 15:
                SURFACE.blit(apple, (j * 32, i * 32))
                
    counterText = fontCounter.render(str(counterApple), False, RED)
    counterRect = counterText.get_rect()
    counterRect.top = 0
    counterRect.right = 32 * FIELDWIDTH
    SURFACE.blit(counterText, counterRect)
    
def moveSnake(direction):
    global counterApple
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
        
    for segment in anaconda:
        if segment[0] == newRow and segment[1] == newColumn:
            return False
    anaconda.append([newRow, newColumn])
    
    if newRow == mcintosh[0] and newColumn == mcintosh[1]:
        counterApple = counterApple + 1
        generateApple(mcintosh)
    else:
        anaconda.pop(0)
    
    return True

SPEEDSNAKE = 4
SPEED = 60

gameCounter = 0
isRunning = True
direction = "Up"
oldDirection = "Up"

gameState = "Idle"
#gameStarted = False
while isRunning:
    if gameState != "GameOver":
        SURFACE.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
            if event.key == K_RETURN:
                gameState = "Started"

            if gameState != "GameOver":
                if event.key == K_UP and oldDirection != "Down":
                    direction = "Up"
                if event.key == K_DOWN and oldDirection != "Up":
                    direction = "Down"
                if event.key == K_LEFT and oldDirection != "Right":
                    direction = "Left"
                if event.key == K_RIGHT and oldDirection != "Left":
                    direction = "Right"
    
    if gameState == "Started" and gameCounter % (SPEED / SPEEDSNAKE) == 0:
        oldDirection = direction
        if not moveSnake(direction):
            gameState = "GameOver"

            #isRunning = False
    
    drawField(oldDirection)
 
    if gameState == "GameOver":
         SURFACE.blit(gameOverText, gameOverRect)
    
    clock.tick(SPEED)
    
    pygame.display.update()
    
    if gameState == "Started":
        gameCounter = gameCounter + 1
    
pygame.quit()