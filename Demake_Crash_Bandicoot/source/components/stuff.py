import pygame
from .. import tools,setup
from .. import constants as C
from . import info
class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name


class Checkpoint(Item):
    def __init__(self, x, y, w, h, checkpoint_type, enemy_groupid=None, name='checkpoint'):
        Item.__init__(self, x, y, w, h, name)
        self.checkpoint_type = checkpoint_type
        self.enemy_groupid = enemy_groupid

class Mask(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_image()

        # self.level = 1

    def load_image(self):
        sheet = setup.GRAPHICS['aku_aku']
        self.frame_rects = [(148, 66, 24, 52)]
        self.right_frames = []
        self.left_frames = []

        for frame_rect in self.frame_rects:
            right_image = tools.get_image(sheet, *frame_rect, C.RGB, 1.3)
            left_image = pygame.transform.flip(right_image, True, False)

            self.right_frames.append(right_image)
            self.left_frames.append(left_image)

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

class Explode(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_image()

    def load_image(self):
        sheet = setup.GRAPHICS['crate_explode']

        self.image = tools.get_image(sheet,40,80,93,62,C.RGB,1)
        self.rect = self.image.get_rect()

class TntExplode(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_image()

    def load_image(self):
        sheet = setup.GRAPHICS['crate_all']
        self.frame_rects = [(76, 159, 42, 41),(118, 159, 42, 41), (160, 159, 42, 41)]
        self.frames = []

        for frame_rect in self.frame_rects:
            self.frames.append(tools.get_image(sheet, *frame_rect, C.RGB, 1))

        self.frame_rects.append((40,80,93,62))
        self.frames.append(tools.get_image(setup.GRAPHICS['crate_explode'],40,80,93,62,C.RGB,1))

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()



