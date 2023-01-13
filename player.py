import json

from spriteAnimation import *


class Player(AnimatedSprite):   # класс игрока
    def __init__(self, sprite_group, x, y):
        super().__init__(sprite_group, x, y)

        with open(os.path.join("assets", "character", "data.json")) as file:
            self.data = json.load(file)

        for i in list(self.data.keys())[1:-2]:
            self.frames.update({i: self.cut_sheet(os.path.join("assets", "character", f"{i}.png"), self.data[i][0],
                                                  scale=self.data["scale"])})
            self.flipped_frames.update({i: self.cut_sheet(os.path.join("assets", "character", f"{i}.png"),
                                                          self.data[i][0], scale=self.data["scale"], symmetry=True)[::-1]})
        self.shield = 100
        self.speed = self.data["speed"]
        self.condition = "idle"
        self.image = self.frames[self.condition][self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.rect = self.image.get_rect()

    def set_condition(self, new_condition):
        if new_condition not in self.data.keys():
            return
        self.condition = new_condition
        self.k = 0
        self.cur_frame = 0

    def attack(self):
        self.set_condition("attack")
        self.rect.x += -10 if self.flipped else 10

    def jump(self):
        self.set_condition("jump")

def draw_shield_bar(surf, x, y, pct):   # отрисовка полосы здоровья
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, (0, 255, 0), fill_rect)
    pygame.draw.rect(surf, (255, 255, 255), outline_rect, 2)
