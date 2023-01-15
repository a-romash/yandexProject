from animatedSprite import *


class Enemy(AnimatedSprite):  # класс противиника
    def __init__(self, screen, sprite_group, x, y):
        super().__init__(screen, sprite_group, x, y)

    def move(self):
        self.set_condition('move')
        range_btw_enemy_and_player = self.rect.x - self.player_coords[0] if self.rect.x > self.player_coords[0] \
            else self.rect.x + self.image.get_width() // 2 - self.player_coords[0]
        if range_btw_enemy_and_player >= 0:
            if not self.flipped:
                self.flip()
            self.rect.x -= self.speed
        else:
            if self.flipped:
                self.flip()
            self.rect.x += self.speed

    def attack(self):
        self.mask = self.get_mask(0)
        if self.flipped:
            if abs(self.rect.x - self.player_coords[0] + 15) <= self.attack_range:
                return self.set_condition('attack')
        if abs(self.rect.x + self.frames["attack"][0].get_width() - 15 - self.player_coords[0]) <= self.attack_range:
            return self.set_condition('attack')

    def get_coords(self, obj):
        self.player_coords = (obj.rect.x + obj.image.get_width() // 2,
                              obj.rect.y + obj.image.get_height() // 2)
