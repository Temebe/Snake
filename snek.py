import pygame, sys
from enum import Enum

fruitImg = pygame.image.load("res/fruit.png")
bodyImg = pygame.image.load("res/body.png")
bgImg = pygame.image.load("res/background.png")
mapSize = 20
screenSize = 1200, 800
black = 0, 0, 0

class SquareType(Enum):
    BODY = 0
    FRUIT = 1
    BACKGROUND = 2
class Snake:
    pass

class Square:

    def __init__(self, posX, posY):
        self.img = bgImg
        self.type = SquareType.BACKGROUND
        self.posX = posX
        self.posY = posY
        self.pos = posX, posY
        pass

    def changeType(self, squareType):
        if self.type == squareType: return
        self.type = squareType
        if squareType == SquareType.BACKGROUND: self.img = bgImg
        if squareType == SquareType.BODY: self.img = bodyImg
        if squareType == SquareType.FRUIT: self.img = fruitImg

class Map:

    def __init__(self):
        self.squares = dict()
        for i, j in list([(i, j) for i in range(mapSize) for j in range(mapSize)]):
            self.squares[(i, j)] = Square(i * 25, j * 25)


pygame.init()
screen = pygame.display.set_mode(screenSize)
map = Map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Edit this later
            posX, posY = pygame.mouse.get_pos()
            i = int(posX/25)
            j = int(posY/25)
            map.squares[(i, j)].changeType(SquareType.BODY)
    
    screen.fill(black)
    for square in map.squares.values():
        screen.blit(square.img, square.pos)
    pygame.display.flip()

#x = Map()
#print(x.squares)

