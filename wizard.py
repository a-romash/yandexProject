import json

from enemy import *


class Wizard(Enemy):
    def __init__(self, screen, sprite_group, x, y):
        super().__init__(screen, sprite_group, x, y)

        with open(os.path.join("assets", "enemies", "wizard", "data.json")) as file:
            self.data = json.load(file)

        for i in list(self.data.keys())[1:-3]:
            self.frames.update({i: self.cut_sheet(os.path.join("assets", "enemies", "wizard", f"{i}.png"),
                                                  self.data[i][0], scale=self.data["scale"])})
            self.flipped_frames.update({i: self.cut_sheet(os.path.join("assets", "enemies", "wizard", f"{i}.png"),
                                                          self.data[i][0], scale=self.data["scale"],
                                                          symmetry=True)[::-1]})
        self.speed = self.data["speed"]
        self.image = self.frames[self.condition][self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = self.get_mask(0)
        self.attack_range = self.data["attack_range"]
        self.damage = 0.5
