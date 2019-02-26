import square, enums
import random as rand

class Map:

    def __init__(self):
        self.squares = dict()
        for x, y in list([(x, y) for x in range(enums.mapSize) for y in range(enums.mapSize)]):
            self.squares[(x, y)] = square.Square(x, y)

    def randomFruit(self):
        rand.seed()
        memory = list()
        for i in range(enums.mapSize * enums.mapSize):
            (x, y) = (rand.randrange(0, enums.mapSize - 1), rand.randrange(0, enums.mapSize - 1))
            if (x, y) in memory: continue
            square = self.squares[(x, y)]
            if square.type == enums.SquareType.BACKGROUND:
                square.changeType(enums.SquareType.FRUIT)
                break
            else:
                memory.append((x, y))

