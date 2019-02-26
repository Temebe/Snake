"""Snake in python
By Sebastian Aksamit
Simple snake just to get along with pygame and python itself
"""
import pygame, sys
import snake, square, map as mapClass, enums

screenSize = 25*20 + 200, 25*20
black = 0, 0, 0
white = 255, 255, 255
SNAKEMOVE = pygame.USEREVENT + 1

def findNextSquare():
    x, y = snake.bodyParts[-1].cords
    if snake.nextDirection == enums.Direction.UP: x, y = x, y - 1
    elif snake.nextDirection == enums.Direction.DOWN: x, y = x, y + 1
    elif snake.nextDirection == enums.Direction.LEFT: x, y = x - 1, y
    elif snake.nextDirection == enums.Direction.RIGHT: x, y = x + 1, y
    snake.direction = snake.nextDirection    
    if x >= enums.mapSize or x < 0 or y >= enums.mapSize or y < 0:
        return None
    nextSquare = map.squares[(x, y)]
    if nextSquare.type == enums.SquareType.BODY:
        print("LOST")
        return None
    return nextSquare


pygame.init()
screen = pygame.display.set_mode(screenSize)
font = pygame.font.Font("res/Arial.ttf", 15)
map = mapClass.Map()
snake = snake.Snake(map.squares[(10, 10)])
map.randomFruit()
scoreText = font.render("Score: 0", 1, white)
speedText = font.render("Speed: 300", 1, white)
pygame.time.set_timer(SNAKEMOVE, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: snake.changeDirection(enums.Direction.UP)
            elif event.key == pygame.K_a: snake.changeDirection(enums.Direction.LEFT)
            elif event.key == pygame.K_s: snake.changeDirection(enums.Direction.DOWN)
            elif event.key == pygame.K_d: snake.changeDirection(enums.Direction.RIGHT)
            elif event.key == pygame.K_ESCAPE: sys.exit()
        if event.type == SNAKEMOVE:
            nextSquare = findNextSquare()
            if nextSquare == None:
                print("LOST")
                break
            if nextSquare.type == enums.SquareType.FRUIT:
                map.randomFruit()
                scoreText = font.render("Score: " + str(snake.score), 1, white)
                if(snake.score%5 == 0):
                    newSpeed = int(300 - snake.score/5 * 2)
                    pygame.time.set_timer(SNAKEMOVE, newSpeed)
                    speedText = font.render("Speed: " + str(newSpeed), 1, white)
            snake.move(nextSquare)
    
    screen.fill(black)
    for square in map.squares.values():
        screen.blit(square.img, square.pos)
    screen.blit(scoreText, (25*20+20, 0))
    screen.blit(speedText, (25*20+20, 30))
    pygame.display.flip()

#x = Map()
#print(x.squares)

