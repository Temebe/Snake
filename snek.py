import pygame, sys
from enum import Enum

fruitImg = pygame.image.load("res/fruit.png")
bodyImg = pygame.image.load("res/body.png")
bgImg = pygame.image.load("res/background.png")
mapSize = 20
squareSize = 20
gapSize = 5

screenSize = 1200, 800
black = 0, 0, 0

class SquareType(Enum):
    BODY = 0
    FRUIT = 1
    BACKGROUND = 2
    
class Snake:
    pass

class Square:

    def __init__(self, cordX, cordY):
        self.img = bgImg
        self.type = SquareType.BACKGROUND
        self.posX = cordX * (squareSize + gapSize)
        self.posY = cordY * (squareSize + gapSize)
        self.pos = self.posX, self.posY
        self.cordX = cordX
        self.cordY = cordY
        self.cords = self.cordX, self.cordY
        pass

    def changeType(self, squareType):
        if self.type == squareType: return
        self.type = squareType
        if squareType == SquareType.BACKGROUND: self.img = bgImgx
        if squareType == SquareType.BODY: self.img = bodyImg
        if squareType == SquareType.FRUIT: self.img = fruitImg

class Map:

    def __init__(self):
        self.squares = dict()
        for i, j in list([(i, j) for i in range(mapSize) for j in range(mapSize)]):
            self.squares[(i, j)] = Square(i, j)


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
            if i >= mapSize or j >= mapSize: break
            map.squares[(i, j)].changeType(SquareType.BODY)
            print("Clicked ({0}, {1}) ".format(i, j))
    
    screen.fill(black)
    for square in map.squares.values():
        screen.blit(square.img, square.pos)
    pygame.display.flip()

#x = Map()
#print(x.squares)

