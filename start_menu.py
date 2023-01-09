import pygame
import sys

from pygame.locals import *

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 30


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def start_menu():
    click = False

    while True:

        screen.fill((0, 0, 0))
        draw_text('START MENU', font, (0, 0, 0), screen, 250, 40)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(500, 330, 300, 50)
        button_2 = pygame.Rect(500, 480, 300, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                rules()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        draw_text('ИГРАТЬ', font, (255, 255, 255), screen, 600, 350)
        draw_text('ПРАВИЛА', font, (255, 255, 255), screen, 600, 500)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def rules():
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


if __name__ == "__main__":

    mainClock = pygame.time.Clock()
    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    font = pygame.font.SysFont(None, 30)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        start_menu()

        screen.fill((0, 0, 0))
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()

click = False
