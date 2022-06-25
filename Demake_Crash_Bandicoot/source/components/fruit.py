import pygame
from source import tools, setup
from source import contants as C


class Fruit(pygame.sprite.Sprite):#水果类继承精灵类
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.frame_index = 0
        frame_rects = [()]#水果位置xy宽高
        self.load_frame(frame_rects)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 10
        self.timer = 0

    def load_frame(self, frame_rects):
        sheet = setup.GRAPHICS['']#图片来源
        for frame_rect in frame_rects:
            self.frames.append(tools.get_image(sheet, *frame_rect, (0, 0, 0), C.BG_MULTI))
            self.current_time = pygame.time.get_ticks()
            frame_duraction = []#buff停留时间

        if self.timer == 0
            self.timer = self.current_time
        elif self.current_time - self.timer > frame_duraction[self.frame_index]:
            self.frame_index = 1
            self.timer = self.current_time

        self.image = self.frames[self.frame_index]


