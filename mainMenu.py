import pygame
import sys
import os

from pygame.locals import *
from constants import *


def load_image(name):   # функция загрузки изображения
    fullname = os.path.join(name)
    image = pygame.image.load(fullname)
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


class Menu_image(pygame.sprite.Sprite):     # отрисовка главного фона
    def __init__(self, group, image_path):
        super().__init__(group)
        self.image = load_image(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.buttons_color = 0


def draw_text(text, font, color, surface, x, y, size):  # функция для отрисовки текста
    font_name = pygame.font.match_font(font)
    font = pygame.font.Font(font_name, size)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def start_menu(screen):     # основное окно меню
    click = False
    font = pygame.font.SysFont(None, 30)
    main_clock = pygame.time.Clock()

    pygame.mixer.music.load("assets/music/magic cliffs.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

    all_sprites = pygame.sprite.Group()
    menu = Menu_image(all_sprites, os.path.join("assets", "background", f"background_{IMAGE}.jpg"))

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
                print('123')
                UI_CONDITION = 1
                return UI_CONDITION
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


def rules(screen):      # окно с правила игры
    main_clock = pygame.time.Clock()
    running = True
    click = False

    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
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


def credits(screen):    # окно с благодарностями
    main_clock = pygame.time.Clock()
    running = True
    click = False

    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
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
