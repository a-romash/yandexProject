import os
import pygame
from spriteAnimation import *

from startMenu import start_menu

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 5
# 0 - Начальное меню
# 1 - уже сама игра
UI_CONDITION = 0


def load_image(name, color_key=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


if __name__ == "__main__":
    pygame.init()

    all_sprites = pygame.sprite.Group()
    character = AnimatedSprite(all_sprites,
                               load_image(os.path.join("assets", "characters", "ninja", "character", "Idle.png")), 4,
                               100, SIZE[1] - 500)
    all_sprites.add(character)

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color("white"))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
