import pygame
from .. import setup
from .. import tools

class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()

    def setup_background(self):
        self.background = setup.GRAPHICS['']
        self.background_rect = self.background.get_rect()

        #放大背景图片使之填充游戏界面
        self.background = pygame.transform.scale()

        self.viewport = 
        pass

    def setup_player(self):
        pass

    def setup_cursor(self):
        pass

    def update(self,surface):
        pass

