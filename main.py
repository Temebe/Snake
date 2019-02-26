import pygame, sys
import snake, square, map as mapClass, enums

screenSize = 1200, 800
black = 0, 0, 0
white = 255, 255, 255
SNAKEMOVE = pygame.USEREVENT + 1


def clickedPos():
    posX, posY = pygame.mouse.get_pos()
    x = int(posX/25)
    y = int(posY/25)
    if x >= enums.mapSize or y >= enums.mapSize: return (None, None)
    else: return (x, y)

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
mousePos = font.render("Mouse pos: 0,0", 1, white)
pygame.time.set_timer(SNAKEMOVE, 500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (x, y) = clickedPos()
            if (x, y) == (None, None): break
            snake.move(map.squares[(x, y)])
            print("Clicked ({0}, {1}) ".format(x, y))
            print("Snake's head: ({0}, {1})".format(snake.bodyParts[-1].cordX, snake.bodyParts[-1].cordY))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            (x, y) = clickedPos()
            if (x, y) == (None, None): break
            map.squares[(x, y)].changeType(enums.SquareType.FRUIT)
            print("Fruited ({0}, {1}) ".format(x, y))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: snake.changeDirection(enums.Direction.UP)
            elif event.key == pygame.K_a: snake.changeDirection(enums.Direction.LEFT)
            elif event.key == pygame.K_s: snake.changeDirection(enums.Direction.DOWN)
            elif event.key == pygame.K_d: snake.changeDirection(enums.Direction.RIGHT)
        if event.type == SNAKEMOVE:
            nextSquare = findNextSquare()
            if nextSquare == None:
                print("LOST")
                break
            if nextSquare.type == enums.SquareType.FRUIT:
                map.randomFruit()
            snake.move(nextSquare)

    if clickedPos() != None:
        x, y = clickedPos()
        mousePos = font.render("Mouse pos: " + str(x) + "," + str(y), 1, white)

    
    screen.fill(black)
    for square in map.squares.values():
        screen.blit(square.img, square.pos)
    screen.blit(mousePos, (500, 500))
    pygame.display.flip()

#x = Map()
#print(x.squares)

