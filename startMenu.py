import pygame
import sys
import os

from pygame.locals import *


def load_image(name):
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


class Menu_img(pygame.sprite.Sprite):
    sprite = pygame.sprite.Sprite()
    sprite.img_menu1 = load_image("assets/background/background_1.jpg")
    image1 = pygame.transform.scale(sprite.img_menu1, (1280, 720))

    sprite.img_menu2 = load_image("assets/background/background_2.jpg")
    image2 = pygame.transform.scale(sprite.img_menu2, (1280, 720))

    def __init__(self, group):
        super().__init__(group)
        self.image = Menu_img.image1
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.buttons_color = 0

    def update(self, b):
        if b == 1:
            self.image = self.image2
            self.buttons_color = 1
        else:
            self.image = self.image1
            self.buttons_color = 0


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

    all_sprites = pygame.sprite.Group()
    menu = Menu_img(all_sprites)

    with open('window.txt', encoding='utf8') as w:
        b = None
        if '0' in w.read():
            b = 0
        else:
            b = 1
        all_sprites.update(b)

    while True:

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        rect_text = pygame.Rect(380, 160, 490, 80)

        mx, my = pygame.mouse.get_pos()

        btn_start = pygame.Rect(100, 380, 270, 50)
        btn_rules = pygame.Rect(100, 480, 270, 50)
        btn_credits = pygame.Rect(100, 580, 270, 50)

        if menu.buttons_color == 0:
            pygame.draw.rect(screen, (147, 112, 250), rect_text)

            pygame.draw.rect(screen, (147, 112, 250), btn_start)
            pygame.draw.rect(screen, (147, 112, 250), btn_rules)
            pygame.draw.rect(screen, (147, 112, 250), btn_credits)

        else:
            pygame.draw.rect(screen, (102,205,170), rect_text)

            pygame.draw.rect(screen, (102,205,170), btn_start)
            pygame.draw.rect(screen, (102,205,170), btn_rules)
            pygame.draw.rect(screen, (102,205,170), btn_credits)

        draw_text('START MENU', 'arrial', (245, 245, 245), screen, 400, 170, 100)

        draw_text('ИГРАТЬ', 'arrial', (245, 245, 245), screen, 190, 397, 30)
        draw_text('ПРАВИЛА', 'arrial', (245, 245, 245), screen, 180, 497, 30)
        draw_text('CREDITS', 'arrial', (245, 245, 245), screen, 180, 597, 30)

        if btn_start.collidepoint((mx, my)):
            if click:
                game(screen)
                change_number(all_sprites)
        if btn_rules.collidepoint((mx, my)):
            if click:
                rules(screen)
                change_number(all_sprites)
        if btn_credits.collidepoint((mx, my)):
            if click:
                credits(screen)
                change_number(all_sprites)

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
