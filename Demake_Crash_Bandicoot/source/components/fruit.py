import pygame
from .. import tools, setup
from .. import constants as C


class Fruit(pygame.sprite.Sprite):#水果类继承精灵类
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = tools.get_image(setup.GRAPHICS['bandicoot_fruit'], 155, 102, 34, 35, (0, 56, 222), 1)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y




    def update(self, surface):
        pass
