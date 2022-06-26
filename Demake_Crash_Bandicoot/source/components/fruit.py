import pygame
from .. import tools, setup
from .. import constants as C


class Fruit(pygame.sprite.Sprite):#水果类继承精灵类
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.frame_index = 0
        frame_rects = [(540, 360, 45, 45)]
        self.load_frame(frame_rects)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 700

    def load_frame(self, frame_rects):
        sheet = setup.GRAPHICS['bandicoot_fruit']#图片来源
        for frame_rect in frame_rects:
            self.frames.append(tools.get_image(sheet, *frame_rect, (0, 0, 0), C.BG_MULTI))


    def update(self):
        pass

