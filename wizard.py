from enemy import *


class Wizard(Enemy):
    def __init__(self, screen, player, sprite_group, x, y):
        super().__init__(screen, player, sprite_group, x, y)

