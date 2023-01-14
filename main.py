import pygame

from player import *
from enemy import *
from camera import *
from mainMenu import start_menu
from constants import *


def load_image(name, color_key=None):
    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    pygame.display.set_mode((1, 1), pygame.NOFRAME)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def load_level(filename):
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = TILE_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)

def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('ground1', x, y)
            elif level[y][x] == '#':
                Tile('ground2', x, y)
            elif level[y][x] == '*':
                Tile('stone1', x, y)
            elif level[y][x] == '-':
                Tile('stone2', x, y)
            elif level[y][x] == '^':
                Tile('stone3', x, y)
            elif level[y][x] == '&':
                Tile('tree', x, y)
            elif level[y][x] == '_':
                Tile('island', x, y)
            elif level[y][x] == '~':
                Tile('sea', x, y)
            elif level[y][x] == '/':
                Tile('sky', x, y)
    # вернем размер поля в клетках
    return x, y

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(SIZE)

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    player = Player(screen, all_sprites, 100, SIZE[1] - 500)
    all_sprites.add(player)

    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    running = True
    camera = Camera()

    pygame.mixer.music.load("assets/music/magic cliffs.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    #level_map = load_level("assets/levels/level1.txt")
    #WIDTH, HEIGHT = generate_level(level_map)

    while running:
        if UI_CONDITION == 0:
            UI_CONDITION = start_menu(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                UI_CONDITION = 0
                continue
            elif event.type == pygame.KEYDOWN and player.condition not in ["attack", "jump", "fall"]:
                if event.key == pygame.K_d:     # при нажатии D игрок бежит вправо
                    player.set_condition("run")
                    if player.flipped:
                        player.flip()
                    player.speed = -player.speed if player.speed < 0 else player.speed
                elif event.key == pygame.K_a:   # при нажатии A игрок бежит влево
                    player.set_condition("run")
                    if not player.flipped:
                        player.flip()
                    player.speed = -player.speed if player.speed > 0 else player.speed
                elif event.key == pygame.K_w:   # при нажатии W игрок прыгает
                    player.jump()
                elif event.key == pygame.K_SPACE and player.condition not in ["attack", "jump", "fall"]:  # при нажатии пробела игрок атакует
                    player.attack()
            elif event.type == pygame.KEYUP and player.condition not in ["attack", "jump", "fall"]:
                player.set_condition("idle")

        if player.condition == "run":   # изменение скорости игрока в зависимости от положения
            player.rect.x += player.speed
        elif player.condition == "jump":
            player.rect.x += player.speed // 2
            player.rect.y -= 5
        elif player.condition == "fall":
            player.rect.x += player.speed // 2
            player.rect.y += 5
            if player.rect.y == SIZE[1] - 500:
                player.set_condition("idle")

        screen.fill(pygame.Color("white"))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(FPS)

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)

        pygame.display.flip()
    pygame.quit()
