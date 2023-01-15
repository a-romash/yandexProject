from animatedSprite import *


class Enemy(AnimatedSprite):  # класс противиника
    def __init__(self, screen, sprite_group, x, y):
        super().__init__(screen, sprite_group, x, y)

    def move(self):
        self.set_condition('move')
        range_btw_enemy_and_player = self.rect.x - self.player_coords[0] if self.rect.x > self.player_coords[0] \
            else self.rect.x + self.image.get_width() // 2 - self.player_coords[0]
        if range_btw_enemy_and_player <= 0:
            self.flipped = self.flipped if self.flipped else not self.flipped
            self.rect.x += self.speed
        else:
            self.flipped = not self.flipped if not self.flipped else self.flipped
            self.rect.x -= self.speed

    def attack(self):
        self.mask = self.get_mask(0)
        if abs(self.rect.x - self.player_coords[0]) <= self.attack_range:
            self.set_condition('attack')

    def get_coords(self, obj):
        self.player_coords = (obj.rect.x + obj.image.get_width() // 2,
                              obj.rect.y + obj.image.get_height() // 2)
