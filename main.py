from player import *

from startMenu import start_menu
from constants import *

if __name__ == "__main__":
    pygame.init()

    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites, 100, SIZE[1] - 500)
    all_sprites.add(player)

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    running = True

    if UI_CONDITION == 0:
        start_menu(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and player.condition not in ["attack", "jump", "fall"]:
                if event.key == pygame.K_d:
                    player.set_condition("run")
                    if player.flipped:
                        player.flip()
                    player.speed = -player.speed if player.speed < 0 else player.speed
                elif event.key == pygame.K_a:
                    player.set_condition("run")
                    if not player.flipped:
                        player.flip()
                    player.speed = -player.speed if player.speed > 0 else player.speed
                if event.key == pygame.K_w:
                    player.jump()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
                    and player.condition not in ["attack", "jump", "fall"]:  # Клик левой кнопкой мыши
                player.attack()

            if event.type == pygame.KEYUP and player.condition not in ["attack", "jump", "fall"]:
                player.set_condition("idle")

        if player.condition == "run":
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
        pygame.display.flip()
    pygame.quit()
