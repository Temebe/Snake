from collections import deque
import enums

UP = enums.Direction.UP
DOWN = enums.Direction.DOWN
LEFT = enums.Direction.LEFT
RIGHT = enums.Direction.RIGHT

class Snake:

    def __init__(self, head):
        self.bodyParts = deque([head])
        head.changeType(enums.SquareType.BODY)
        self.direction = UP
        self.nextDirection = UP

    def move(self, nextBody):
        if nextBody.type != enums.SquareType.FRUIT:
            self.bodyParts.popleft().changeType(enums.SquareType.BACKGROUND)
        self.bodyParts.append(nextBody)
        nextBody.changeType(enums.SquareType.BODY)

    def changeDirection(self, direction):
        if self.direction == direction: return
        if direction == UP:
            if self.direction == DOWN: return
            else: self.nextDirection = direction
        elif direction == LEFT:
            if self.direction == RIGHT: return
            else: self.nextDirection = direction  
        elif direction == RIGHT:
            if self.direction == LEFT: return
            else: self.nextDirection = direction  
        elif direction == DOWN:
            if self.direction == UP: return
            else: self.nextDirection = direction    
            