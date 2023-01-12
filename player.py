import json

from spriteAnimation import *


class Player(AnimatedSprite):
    def __init__(self, sprite_group, x, y):
        super().__init__(sprite_group, x, y)

        with open(os.path.join("assets", "character", "data.json")) as file:
            self.data = json.load(file)

        for i in list(self.data.keys())[1:-2]:
            self.frames.update({i: self.cut_sheet(os.path.join("assets", "character", f"{i}.png"), self.data[i][0],
                                                  scale=self.data["scale"])})
            self.flipped_frames.update({i: self.cut_sheet(os.path.join("assets", "character", f"{i}.png"),
                                                          self.data[i][0], scale=self.data["scale"], symmetry=True)[::-1]})
        self.speed = self.data["speed"]
        self.condition = "idle"
        self.image = self.frames[self.condition][self.cur_frame]
        self.rect = self.rect.move(x, y)

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
