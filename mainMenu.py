import pygame
import sys
import os
import random

from pygame.locals import *
from constants import *

IMAGE = random.randint(1, 2)


def load_image(name, color_key=None):
    # загрузка и обработка изображения
    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    return image


def change_number(all_sprites):
    with open('window.txt', encoding='utf8') as w:
        window = int(w.read().strip()) + 1

    with open('window.txt', mode='wt') as w:
        w.write(f'{window % 2}')

    with open('window.txt', encoding='utf8') as w:
        if '0' in w.read():
            b = 0
        else:
            b = 1
        all_sprites.update(b)


class BackgroundImage(pygame.sprite.Sprite):
    # отрисовка главного фона

    def __init__(self, group, image_path):
        super().__init__(group)
        image = load_image(image_path)
        image = pygame.transform.scale(image, (1280, 720))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.buttons_color = 0


def draw_text(text, font, color, surface, x, y, size):
    # функция для отрисовки текста

    font_name = pygame.font.match_font(font)
    font = pygame.font.Font(font_name, size)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def start_menu(screen):
    # основное окно меню

    FPS = 60
    click = False
    font = pygame.font.SysFont(None, 30)
    main_clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    background_image = BackgroundImage(all_sprites, os.path.join("assets", "background", f"background_{IMAGE}.jpg"))

    while True:
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        rect_text = pygame.Rect(370, 160, 510, 80)

        mx, my = pygame.mouse.get_pos()

        btn_start = pygame.Rect(100, 380, 270, 50)
        btn_rules = pygame.Rect(100, 480, 270, 50)
        btn_credits = pygame.Rect(100, 580, 270, 50)

        pygame.draw.rect(screen, (147, 112, 250), rect_text, border_radius=10)

        pygame.draw.rect(screen, (147, 112, 250), btn_start, border_radius=10)
        pygame.draw.rect(screen, (147, 112, 250), btn_rules, border_radius=10)
        pygame.draw.rect(screen, (147, 112, 250), btn_credits, border_radius=10)

        draw_text('ПЛАТФОРМЕР', 'arrial', (245, 245, 245), screen, 380, 170, 100)

        draw_text('ИГРАТЬ', 'arrial', (245, 245, 245), screen, 190, 397, 30)
        draw_text('ПРАВИЛА', 'arrial', (245, 245, 245), screen, 180, 497, 30)
        draw_text('CREDITS', 'arrial', (245, 245, 245), screen, 180, 597, 30)

        if click:
            if btn_start.collidepoint((mx, my)):
                return 1
            if btn_rules.collidepoint((mx, my)):
                rules(screen)
            if btn_credits.collidepoint((mx, my)):
                credits(screen)

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

        main_clock.tick(FPS)
        pygame.display.update()


def rules(screen):
    # окно с правила игры

    main_clock = pygame.time.Clock()
    running = True
    click = False
    all_sprites = pygame.sprite.Group()
    FPS = 60

    background_image = BackgroundImage(all_sprites, os.path.join("assets", "background", f"background_{IMAGE}.jpg"))

    while running:
        mx, my = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        # отрисовка всех надписей и кнопок
        btn_esc = pygame.Rect(50, 580, 170, 50)
        pygame.draw.rect(screen, (174, 24, 255), btn_esc, 5, 10)
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

        main_clock.tick(FPS)
        pygame.display.update()


def credits(screen):
    # окно с благодарностями

    main_clock = pygame.time.Clock()
    running = True
    click = False
    all_sprites = pygame.sprite.Group()
    FPS = 60

    background_image = BackgroundImage(all_sprites, os.path.join("assets", "background", f"background_{IMAGE}.jpg"))

    while running:
        mx, my = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        btn_esc = pygame.Rect(50, 580, 170, 50)
        pygame.draw.rect(screen, (174, 24, 255), btn_esc, 5, 10)
        draw_text('НАЗАД', 'arrial', (255, 255, 255), screen, 95, 595, 30)
        draw_text('Отдельноe спасибо:', 'arrial', (255, 255, 255), screen, 400, 50, 100)
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

        main_clock.tick(FPS)
        pygame.display.update()
