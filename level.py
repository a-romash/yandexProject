from constants import *
import pygame
import datetime as dt

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


def load_level(filename):
    # читаем уровень, убирая символы перевода строки

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку прозрачными клетками
    return list(map(lambda x: x.ljust(max_width, ' '), level_map))


class Fon(pygame.sprite.Sprite):
    # класс для фонового изображения
    def __init__(self, all_sprites, name):
        super().__init__(all_sprites)
        image = load_image(name)
        image = pygame.transform.scale(image, (1400, 720))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = -450
        self.rect.y = 0


def load_fon(sprite_group):
    # смена фона в зависимости от времени на компьютере
    time_now = dt.datetime.now().time()
    if dt.time(hour=4, minute=0) <= time_now <= dt.time(hour=11, minute=59):
        a = 1
    elif dt.time(hour=12, minute=0) <= time_now <= dt.time(hour=16, minute=59):
        a = 2
    elif dt.time(hour=17, minute=0) <= time_now <= dt.time(hour=22, minute=59):
        a = 3
    elif dt.time(hour=23, minute=0) <= time_now <= dt.time(hour=3, minute=59):
        a = 4
    else:
        a = 4

    fon = Fon(sprite_group, f'assets/map/fon{a}.jpg')
    return fon


class Tile(pygame.sprite.Sprite):
    # класс неподвижных элементов
    def __init__(self, tile_type, pos_x, pos_y, tiles_group):
        super().__init__(tiles_group, all_sprites)
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x - TILE_WIDTH * 3, TILE_HEIGHT * pos_y - 15)


def generate_level(level):
    # генератор объектов для уровня
    for y in range(len(level)):
        for x in range(len(level[0])):
            if level[y][x] == '.':
                Tile('ground1', x, y, tiles_group)
            elif level[y][x] == '#':
                Tile('ground2', x, y, tiles_group)
            elif level[y][x] == '*':
                Tile('stone1', x, y, tiles_group)
            elif level[y][x] == '-':
                Tile('stone2', x, y, tiles_group)
            elif level[y][x] == '^':
                Tile('stone3', x, y, tiles_group)
            elif level[y][x] == '&':
                Tile('tree', x, y, tiles_group)
            elif level[y][x] == '_':
                Tile('island', x, y, tiles_group)
            elif level[y][x] == '~':
                Tile('sea', x, y, tiles_group)
    # вернем размер поля в клетках
    return x, y


def draw(screen, ticks):
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 24)
    font = pygame.font.Font(None, 70)
    text = font.render(f"{minutes}:{seconds}", True, (255, 0, 0))
    screen.blit(text, (80, 60))
