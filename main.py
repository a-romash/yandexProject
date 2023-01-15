import pygame

from player import *
from enemy import *
from camera import *
from mainMenu import *
from constants import *
from wizard import Wizard
from level import *

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(SIZE)

    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    running = True
    camera = Camera()

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()

    fon = load_fon(all_sprites)

    player = Player(screen, all_sprites, 100, SIZE[1] - 320)

    for i in range(8):
        wizard = Wizard(screen, all_sprites, randint(150, SIZE[0]), SIZE[1] - 320)
        enemies.add(wizard)

    play_tick = 0

    pygame.mixer.music.load("assets/music/magic cliffs.mp3")  # загрузка музыки
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    level_map = load_level("assets/levels/level1.txt")  # загрузка уровня

    while running:
        start_ticks = pygame.time.get_ticks()

        if UI_CONDITION == 0:
            UI_CONDITION = start_menu(screen)
            play_tick = pygame.time.get_ticks()
            UI_CONDITION = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                UI_CONDITION = 0
                continue
            elif event.type == pygame.KEYDOWN and player.condition not in ["attack", "jump", "fall"]:
                if event.key == pygame.K_d:  # при нажатии D игрок бежит вправо
                    player.set_condition("run")
                    if player.flipped:
                        player.flip()
                    player.speed = -player.speed if player.speed < 0 else player.speed
                elif event.key == pygame.K_a:  # при нажатии A игрок бежит влево
                    player.set_condition("run")
                    if not player.flipped:
                        player.flip()
                    player.speed = -player.speed if player.speed > 0 else player.speed
                elif event.key == pygame.K_w:  # при нажатии W игрок прыгает
                    player.jump()
                elif event.key == pygame.K_SPACE and player.condition not in ["attack", "jump",
                                                                              "fall"]:  # при нажатии пробела игрок атакует
                    player.attack()
                    for enemy in enemies:
                        if pygame.sprite.collide_mask(player, enemy):
                            enemy.health -= player.damage
                            if enemy.health <= 0:
                                enemies.remove(enemy)
                                enemy.die()
            elif event.type == pygame.KEYUP and player.condition not in ["attack", "jump", "fall"]:
                player.set_condition("idle")

        if player.condition == "run":  # изменение положения игрока в зависимости от действия
            player.rect.x += player.speed
            fon.rect.x += player.speed
        elif player.condition == "attack":
            fon.rect.x += -10 if player.flipped else 10
            player.rect.x += -10 if player.flipped else 10
        elif player.condition == "jump":
            player.rect.x += player.speed // 2
            fon.rect.x += player.speed // 2
            player.rect.y -= 5
        elif player.condition == "fall":
            player.rect.x += player.speed // 2
            fon.rect.x += player.speed // 2
            player.rect.y += 5
            if player.rect.y == SIZE[1] - 320:
                player.set_condition("idle")

        # изменяем ракурс камеры
        camera.update(player)

        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)

        screen.fill(pygame.Color("white"))

        for enemy in enemies:
            enemy.get_coords(player)
            enemy.attack()
            if pygame.sprite.collide_mask(player, enemy) and enemy.condition == "attack":
                player.health -= enemy.damage
                if player.health <= 0:
                    all_sprites.remove(player)
                    player.die()
            elif enemy.condition != "attack":
                enemy.set_condition('run')
                enemy.move()

        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(FPS)

        camera.update(player)   # обновление камеры
        for sprite in all_sprites:
            camera.apply(sprite)
        camera.update(fon)

        if UI_CONDITION == 1:
            draw(screen, start_ticks - play_tick)

        pygame.display.flip()
    pygame.quit()
