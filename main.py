import pygame

from player import *
from enemy import *
from camera import *
from mainMenu import *
from constants import *
from level import *

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(SIZE)

    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    running = True
    camera = Camera()

    pygame.mixer.music.load("assets/music/magic cliffs.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    level_map = load_level("assets/levels/level1.txt")
    WIDTH, HEIGHT = generate_level(level_map)

    player = Player(screen, all_sprites, 100, SIZE[1] - 500)
    all_sprites.add(player)

    while running:
        if UI_CONDITION == 0:
            start_menu(screen)
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
            elif event.type == pygame.KEYUP and player.condition not in ["attack", "jump", "fall"]:
                player.set_condition("idle")

        if player.condition == "run":  # изменение скорости игрока в зависимости от положения
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
