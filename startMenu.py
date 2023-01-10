import pygame
import sys

from pygame.locals import *


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def start_menu(screen):
    click = False
    font = pygame.font.SysFont(None, 30)
    main_clock = pygame.time.Clock()

    while True:

        screen.fill((0, 0, 0))
        draw_text('START MENU', font, (0, 0, 0), screen, 250, 40)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(100, 480, 270, 50)
        button_2 = pygame.Rect(100, 580, 270, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game(screen)
        if button_2.collidepoint((mx, my)):
            if click:
                rules(screen)
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        draw_text('ИГРАТЬ', font, (255, 255, 255), screen, 160, 500)
        draw_text('ПРАВИЛА', font, (255, 255, 255), screen, 160, 600)

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
        main_clock.tick(60)


def game(screen):
    main_clock = pygame.time.Clock()
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
        main_clock.tick(60)


def rules(screen):
    main_clock = pygame.time.Clock()
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
        main_clock.tick(60)
