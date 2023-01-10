import os
import pygame
import sys

from pygame.locals import *


def start_menu(screen):
    click = False
    font = pygame.font.SysFont(None, 30)
    main_clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))
        draw_text('START MENU', 'tiger', (100, 22, 0), screen, 430, 250, 45)

        mx, my = pygame.mouse.get_pos()

        btn_play = pygame.Rect(500, 340, 300, 50)
        btn_rules = pygame.Rect(500, 440, 300, 50)
        btn_choice_character = pygame.Rect(500, 540, 300, 50)

        if btn_play.collidepoint((mx, my)):
            if click:
                game(screen)
        if btn_rules.collidepoint((mx, my)):
            if click:
                rules(screen)
        if btn_choice_character.collidepoint((mx, my)):
            if click:
                choice(screen)
        pygame.draw.rect(screen, (255, 0, 0), btn_play)
        pygame.draw.rect(screen, (255, 0, 0), btn_rules)
        pygame.draw.rect(screen, (255, 0, 0), btn_choice_character)

        draw_text('ИГРАТЬ', 'tiger', (255, 255, 255), screen, 575, 350, 30)
        draw_text('ПРАВИЛА', 'tiger', (255, 255, 255), screen, 575, 450, 30)
        draw_text('ВЫБОР ИГРОКА', 'tiger', (255, 255, 255), screen, 530, 550, 30)

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


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def draw_text(text, fon, color, surface, x, y, size):
    font_name = pygame.font.match_font(fon)
    font = pygame.font.Font(font_name, size)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def game(screen):
    running = True
    main_clock = pygame.time.Clock()

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


def choice(screen):
    running = True

    click = False
    font = pygame.font.SysFont(None, 30)
    main_clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        btn_archer = pygame.Rect(230, 200, 300, 400)
        btn_ninja = pygame.Rect(750, 200, 300, 400)

        pygame.draw.rect(screen, (0, 0, 255), btn_archer)
        pygame.draw.rect(screen, (0, 0, 255), btn_ninja)
        pygame.draw.rect(screen, (0, 0, 0), (250, 220, 260, 300))
        pygame.draw.rect(screen, (0, 0, 0), (770, 220, 260, 300))

        if btn_ninja.collidepoint((mx, my)):
            if click:
                pygame.draw.rect(screen, (255, 255, 0), btn_ninja)
                pygame.draw.rect(screen, (0, 0, 0), (770, 220, 260, 300))
        if btn_archer.collidepoint((mx, my)):
            if click:
                pygame.draw.rect(screen, (255, 255, 0), btn_archer)
                pygame.draw.rect(screen, (0, 0, 0), (250, 220, 260, 300))

        draw_text('Выберете игрока:', 'tiger', (255, 255, 255), screen, 150, 30, 50)
        draw_text('ARCHER', 'tiger', (255, 255, 255), screen, 300, 540, 30)
        draw_text('NINJIA', 'tiger', (255, 255, 255), screen, 830, 540, 30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        main_clock.tick(30)


def rules(screen):
    main_clock = pygame.time.Clock()
    running = True

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.fill((0, 0, 0))
        draw_text('ПРАВИЛА:', 'tiger', (100, 22, 0), screen, 100, 20, 45)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        main_clock.tick(30)
