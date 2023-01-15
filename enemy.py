from animatedSprite import *


class Enemy(AnimatedSprite):   # класс противиника
    def __init__(self, screen, player, sprite_group, x, y):
        super().__init__(screen, sprite_group, x, y)
        self.player_coords = (player.rect.x + player.image.get_width() // 2,
                              player.rect.y + player.image.get_height() // 2)
        self.rect = self.rect.move(x, y)
        self.speed = 10

    def move(self):
        if self.rect.x < self.player_coords[0]:
            self.flipped = not self.flipped if not self.flipped else self.flipped
            self.rect.x += self.speed
            return
        self.flipped = not self.flipped if self.flipped else self.flipped
        self.rect.x += -self.speed
