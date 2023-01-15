from random import randint
from main import load_image

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60
# 0 - начальное меню
# 1 - уже сама игра
# 2 - меню после смерти
UI_CONDITION = 0
IMAGE = randint(1, 2)  # константа конкретно на одну сессию, значение может отличаться при разных запусках программы
TITLE = "Платформер"
TILE_IMAGES = {
    'far-grounds': load_image('assets/map/far-grounds.png'),   #   .
    'clouds': load_image('assets/map/clouds.png'),   #   #
    'tileset': load_image('assets/map/tileset.png'),   #   *
    'sea': load_image('assets/map/sea.png'),   #   ~
    'sky': load_image('assets/map/sky.png')   #   /
}
TILE_WIDTH = TILE_HEIGHT = 50
