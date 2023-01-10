import pygame
import sys

from pygame.locals import *


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def start_menu(screen):
    click = False
    font = pygame.font.SysFont(None, 30)
    main_clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))
        draw_text('START MENU', font, (0, 0, 0), screen, 250, 40)

        mx, my = pygame.mouse.get_pos()

        btn_start = pygame.Rect(100, 480, 270, 50)
        btn_rules = pygame.Rect(100, 580, 270, 50)

        if btn_start.collidepoint((mx, my)):
            if click:
                game(screen)
        if btn_rules.collidepoint((mx, my)):
            if click:
                rules(screen)
        pygame.draw.rect(screen, (255, 0, 0), btn_start)
        pygame.draw.rect(screen, (255, 0, 0), btn_rules)

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
