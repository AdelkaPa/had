import pyglet
from pyglet.window.key import LEFT, RIGHT, UP, DOWN
window = pyglet.window.Window()

TILE_WIDTH = 64
TILE_HEIGHT = 64
FIELD_WIDTH = 10
FIELD_HEIGHT = 10



window.width = TILE_WIDTH*FIELD_WIDTH
window.height = TILE_HEIGHT*FIELD_HEIGHT


square = pyglet.image.load('green.png')
snake = pyglet.sprite.Sprite(square)

position_x = 5 #position označuje buňky
position_y = 5
snake_tiles = [(1,1), (2,1), (2,2)]#last is head

food = pyglet.image.load('apple.png')
apple = pyglet.sprite.Sprite(food)
apple.scale = 0.25 #zmenšení obrázku

food_position = (7,7)

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
    window.clear()
    for tile in snake_tiles:
        snake.x = tile[0] * TILE_WIDTH
        snake.y = tile[-1] * TILE_HEIGHT
        snake.draw()
    apple.x = food_position[0] * TILE_WIDTH
    apple.y = food_position[1] * TILE_HEIGHT
    apple.draw()

def press_button(symbol, mode):
    move_snake(symbol)


#def move()




window.push_handlers(on_draw = drawing, on_key_release = press_button)











pyglet.app.run()
