import os
import pygame


def load_image(name, color_key=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, screen, sprite_group, x, y):
        super().__init__(sprite_group)
        self.cur_frame = 0
        self.screen = screen
        self.frames = dict()
        self.flipped_frames = dict()
        self.condition = "idle"
        self.health = 100
        self.flipped = False
        self.k = 0

    def cut_sheet(self, sheet_path, columns, scale=1, symmetry=False):
        sheet = load_image(sheet_path)
        sheet = pygame.transform.scale(sheet, (sheet.get_width() * scale, sheet.get_height() * scale))
        if symmetry:
            sheet = pygame.transform.flip(sheet, True, False)
        frames = list()
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height())

        for i in range(columns):
            frame_location = (self.rect.w * i, 0)
            frames.append(sheet.subsurface(pygame.Rect(
                frame_location, self.rect.size)))

        return frames

    def update(self):
        if not self.flipped:
            if self.k % self.data[self.condition][1] == 0:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames[self.condition])
                self.image = self.frames[self.condition][self.cur_frame]
            if self.k // self.data[self.condition][1] == len(self.frames[self.condition]) - 1\
                    and self.condition == "attack":
                self.set_condition("idle")
            elif self.k // self.data[self.condition][1] == len(self.frames[self.condition]) \
                    and self.condition == "jump":
                self.set_condition("fall")
        else:
            if self.k % self.data[self.condition][1] == 0:
                self.cur_frame = (self.cur_frame + 1) % len(self.flipped_frames[self.condition])
                self.image = self.flipped_frames[self.condition][self.cur_frame]
            if self.k // self.data[self.condition][1] == len(self.frames[self.condition]) - 1 \
                    and self.condition == "attack":
                self.set_condition("idle")
            elif self.k // self.data[self.condition][1] == len(self.frames[self.condition]) \
                    and self.condition == "jump":
                self.set_condition("fall")
        self.k += 1

    def flip(self):
        self.flipped = True if not self.flipped else False
        self.cur_frame = 0
