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
    'ground1': load_image('assets/map/ground1.png'),   #   .
    'ground2': load_image('assets/map/ground2.png'),   #   #
    'stone1': load_image('assets/map/stone1.png'),   #   *
    'stone2': load_image('assets/map/stone2.png'),   #   -
    'stone3': load_image('assets/map/stone3.png'),   #   ^
    'tree': load_image('assets/map/tree.png'),   #   &
    'island': load_image('assets/map/flyingIsland.png'),   #   _
    'sea': load_image('assets/map/sea.png'),   #   ~
    'sky': load_image('assets/map/sky.png')   #   /
}
TILE_WIDTH = TILE_HEIGHT = 50
