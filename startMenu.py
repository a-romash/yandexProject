import pygame
import sys

from pygame.locals import *


def draw_text(text, fon, color, surface, x, y, size):
    font_name = pygame.font.match_font(fon)
    font = pygame.font.Font(font_name, size)
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
        draw_text('START MENU', 'arrial', (100, 22, 0), screen, 430, 250, 100)

        mx, my = pygame.mouse.get_pos()

        btn_start = pygame.Rect(100, 380, 270, 50)
        btn_rules = pygame.Rect(100, 480, 270, 50)
        btn_credits = pygame.Rect(100, 580, 270, 50)

        if btn_start.collidepoint((mx, my)):
            if click:
                game(screen)
        if btn_rules.collidepoint((mx, my)):
            if click:
                rules(screen)
        if btn_credits.collidepoint((mx, my)):
            if click:
                credits(screen)
        pygame.draw.rect(screen, (255, 0, 0), btn_start)
        pygame.draw.rect(screen, (255, 0, 0), btn_rules)
        pygame.draw.rect(screen, (255, 0, 0), btn_credits)

        draw_text('ИГРАТЬ', 'arrial', (255, 255, 255), screen, 190, 397, 30)
        draw_text('ПРАВИЛА', 'arrial', (255, 255, 255), screen, 180, 497, 30)
        draw_text('CREDITS', 'arrial', (255, 255, 255), screen, 180, 597, 30)

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
        choise(screen, main_clock)
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
    click = False

    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        btn_esc = pygame.Rect(50, 580, 170, 50)
        pygame.draw.rect(screen, (174, 24, 255), btn_esc)
        draw_text('НАЗАД', 'arrial', (255, 255, 255), screen, 95, 595, 30)
        draw_text('Правила:', 'arrial', (255, 255, 255), screen, 400, 50, 100)
        if btn_esc.collidepoint((mx, my)):
            if click:
                running = False
        click = False
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
        main_clock.tick(60)

def credits(screen):
    main_clock = pygame.time.Clock()
    running = True
    click = False

    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        btn_esc = pygame.Rect(50, 580, 170, 50)
        pygame.draw.rect(screen, (174, 24, 255), btn_esc)
        draw_text('НАЗАД', 'arrial', (255, 255, 255), screen, 95, 595, 30)
        draw_text('Кредиты:', 'arrial', (255, 255, 255), screen, 400, 50, 100)
        if btn_esc.collidepoint((mx, my)):
            if click:
                running = False
        click = False
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
        main_clock.tick(60)

def choise(screen, mainClock):
    running = True
    click = False
    while running:
        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        btn_archer = pygame.Rect(230, 200, 300, 400)
        btn_ninjia = pygame.Rect(750, 200, 300, 400)

        pygame.draw.rect(screen, (0, 0, 255), btn_archer)
        pygame.draw.rect(screen, (0, 0, 255), btn_ninjia)
        pygame.draw.rect(screen, (0, 0, 0), (250, 220, 260, 300))
        pygame.draw.rect(screen, (0, 0, 0), (770, 220, 260, 300))

        btn_esc = pygame.Rect(50, 630, 170, 50)
        pygame.draw.rect(screen, (174, 24, 255), btn_esc)
        draw_text('НАЗАД', 'arrial', (255, 255, 255), screen, 95, 645, 30)

        if btn_esc.collidepoint((mx, my)):
            if click:
                running = False
        if btn_ninjia.collidepoint((mx, my)):
            if click:
                pygame.draw.rect(screen, (255, 255, 0), btn_ninjia)
                pygame.draw.rect(screen, (0, 0, 0), (770, 220, 260, 300))
        if btn_archer.collidepoint((mx, my)):
            if click:
                pygame.draw.rect(screen, (255, 255, 0), btn_archer)
                pygame.draw.rect(screen, (0, 0, 0), (250, 220, 260, 300))

        draw_text('Выберете игрока:', 'arrial', (255, 255, 255), screen, 150, 80, 80)
        draw_text('ARCHER', 'tiger', (255, 255, 255), screen, 287, 540, 30)
        draw_text('NINJIA', 'tiger', (255, 255, 255), screen, 817, 540, 30)

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
        mainClock.tick(60)
