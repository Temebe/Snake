import pygame, sys
import snake, square, map as mapClass, enums

screenSize = 1200, 800
black = 0, 0, 0

def clickedPos():
    posX, posY = pygame.mouse.get_pos()
    x = int(posX/25)
    y = int(posY/25)
    if x >= enums.mapSize or y >= enums.mapSize: return None
    else: return (x, y)


pygame.init()
screen = pygame.display.set_mode(screenSize)
map = mapClass.Map()
snake = snake.Snake(map.squares[(10, 10)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #Edit this later
            if clickedPos() != None: (x, y) = clickedPos()
            else: break
            #map.squares[(i, j)].changeType(SquareType.BODY)
            snake.move(map.squares[(x, y)])
            print("Clicked ({0}, {1}) ".format(x, y))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if clickedPos() != None: (x, y) = clickedPos()
            else: break
            map.squares[(x, y)].changeType(enums.SquareType.FRUIT)
            print("Fruited ({0}, {1}) ".format(x, y))
    
    screen.fill(black)
    for square in map.squares.values():
        screen.blit(square.img, square.pos)
    pygame.display.flip()

#x = Map()
#print(x.squares)

