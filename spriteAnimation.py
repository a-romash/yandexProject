import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_group, sheet, columns, x, y):
        super().__init__(sprite_group)
        self.frames = []
        sheet = pygame.transform.scale(sheet, (sheet.get_width() * 2, sheet.get_height() * 2))
        self.cut_sheet(sheet, columns)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height())
        for i in range(columns):
            frame_location = (self.rect.w * i, 0)
            self.frames.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
