from random import randint
from mainMenu import load_image
import pygame

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60
# 0 - начальное меню
# 1 - уже сама игра
# 2 - меню после смерти
UI_CONDITION = 0
IMAGE = randint(1, 2)  # константа конкретно на одну сессию, значение может отличаться при разных запусках программы
TITLE = "Платформер"
TILE_IMAGES = {
    'ground1': load_image('assets/map/pros.png'),  # .
    'ground2': load_image('assets/map/ground2.png'),  # #
    'stone1': load_image('assets/map/stone1.png'),  # *
    'stone2': load_image('assets/map/stone2.png'),  # -
    'stone3': load_image('assets/map/stone3.png'),  # ^
    'tree': load_image('assets/map/tree.png'),  # &
    'island': load_image('assets/map/flyingIsland.png'),  # _
    'sea': load_image('assets/map/sea.png'),  # ~
}
TILE_WIDTH = 40
TILE_HEIGHT = 34
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
mobs = pygame.sprite.Group()
