import enums
import pygame

fruitImg = pygame.image.load("res/fruit.png")
bodyImg = pygame.image.load("res/body.png")
bgImg = pygame.image.load("res/background.png")

class Square:

    def __init__(self, cordX, cordY):
        self.img = bgImg
        self.type = enums.SquareType.BACKGROUND
        self.posX = cordX * (enums.squareSize + enums.gapSize)
        self.posY = cordY * (enums.squareSize + enums.gapSize)
        self.pos = self.posX, self.posY
        self.cordX = cordX
        self.cordY = cordY
        self.cords = self.cordX, self.cordY

    def changeType(self, squareType):
        if self.type == squareType: return
        self.type = squareType
        if squareType == enums.SquareType.BACKGROUND: self.img = bgImg
        if squareType == enums.SquareType.BODY: self.img = bodyImg
        if squareType == enums.SquareType.FRUIT: self.img = fruitImg