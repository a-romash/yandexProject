import pygame
import spriteAnimation

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 30

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
