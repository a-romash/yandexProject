import pygame
import spriteAnimation

from startMenu import start_menu

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 30
# 0 - Начальное меню
# 1 - Правила
# 2 - Что то после "Играть"
UI_CONDITION = 0


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if UI_CONDITION == 0:
            start_menu(screen)

        screen.fill((0, 0, 0))
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
