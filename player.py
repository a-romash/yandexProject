import json

from animatedSprite import *


class Player(AnimatedSprite):
    # класс игрока
    def __init__(self, screen, sprite_group, x, y):
        super().__init__(screen, sprite_group, x, y)

        with open(os.path.join("assets", "character", "data.json")) as file:
            self.data = json.load(file)

        for i in list(self.data.keys())[1:-2]:
            self.frames.update({i: self.cut_sheet(os.path.join("assets", "character", f"{i}.png"), self.data[i][0],
                                                  scale=self.data["scale"])})
            self.flipped_frames.update({i: self.cut_sheet(os.path.join("assets", "character", f"{i}.png"),
                                                          self.data[i][0], scale=self.data["scale"], symmetry=True)[::-1]})

        self.speed = self.data["speed"]
        self.image = self.frames[self.condition][self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = self.get_mask(4)
        self.damage = 65
        # self.health = 10000  # для дебага ботов

    def attack(self):
        # атака
        self.set_condition("attack")
        self.rect.x += -20 if self.flipped else 20

    def jump(self):
        # прыжок
        self.set_condition("jump")

    def update(self):
        # обновление скина персонажа
        self.draw_shield_bar()
        super().update()

    def draw_shield_bar(self):
        # шкала здоровья
        if self.health < 0:
            self.health = 50
        bar_width = 80
        bar_height = 7
        x, y = self.rect.x + self.image.get_width() // 2, self.rect.y + self.image.get_height() // 2

        outline_rect = pygame.Rect(x - bar_width // 2, y - bar_height, bar_width, bar_height)
        fill_rect = pygame.Rect(x - bar_width // 2 + 2, y - bar_height + 2,
                                (self.health / 100) * bar_width - 4, bar_height - 4)
        pygame.draw.rect(self.screen, (0, 0, 0), outline_rect, border_radius=3)
        pygame.draw.rect(self.screen, (255, 0, 0), fill_rect, border_radius=3)

