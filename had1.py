import pyglet
import math
window = pyglet.window.Window()

TILE_WIDTH = 64
TILE_HEIGHT = 64
FIELD_WIDTH = 10
FIELD_HEIGHT = 10
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4



window.width = TILE_WIDTH*FIELD_WIDTH
window.height = TILE_HEIGHT*FIELD_HEIGHT


square = pyglet.image.load('green.png')
snake = pyglet.sprite.Sprite(square)

position_x = 5 #position označuje buňky
position_y = 5
snake_tiles = [(1,1), (2,1), (2,2)]#last is head

def move_snake(direction):
    head = snake_tiles[-1]
    if direction == LEFT:
        head = head[0] -1 , head[1]
    elif direction == RIGHT:
        head = head[0] + 1, head[1]
    elif direction == UP:
        head = head[0], head[1] + 1
    elif direction == DOWN:
        head = head[0], head[1] - 1
    if head in snake_tiles:
        raise ValueError('srážka s hadem')
    if head[0] <= 0 or head[0] >= FIELD_WIDTH or head[1] >= FIELD_HEIGHT:
        raise ValueError('náraz do zdi')

    snake_tiles.append(head)
    del snake_tiles[0]



def drawing():
    snake.x = position_x * TILE_WIDTH
    snake.y = position_y * TILE_HEIGHT
    window.clear()
    snake.draw()

def press_button(symbol, mode):
    global position_x, position_y
    print(symbol, mode)
    if symbol == pyglet.window.key.UP:
        if position_y + 1 < FIELD_HEIGHT:
            position_y += 1

    if symbol == pyglet.window.key.DOWN:
        if position_y -1 >= 0:
            position_y += -1

    if symbol == pyglet.window.key.RIGHT:
        if position_x + 1 < FIELD_WIDTH:
            position_x += 1
    if symbol == pyglet.window.key.LEFT:
        if position_x -1 >= 0:
            position_x += -1

#def move()




window.push_handlers(on_draw = drawing, on_key_release = press_button)











pyglet.app.run()
