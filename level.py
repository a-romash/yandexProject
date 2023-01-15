from constants import *
from constants import tiles_group, all_sprites, mobs
import pygame


def load_level(filename):
    # читаем уровень, убирая символы перевода строки

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, tiles_group):
        super().__init__(tiles_group, all_sprites)
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)


def generate_level(level):
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
            elif level[y][x] == '/':
                Tile('sky', x, y, tiles_group)
    # вернем размер поля в клетках
    return x, y
