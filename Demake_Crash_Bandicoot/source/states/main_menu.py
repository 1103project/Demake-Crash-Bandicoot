import pygame
from .. import setup
from .. import tools
from ..components import info

class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_cursor()
        self.info = info.Info('main_menu')

    def setup_background(self):
        self.background = setup.GRAPHICS['menubackground']
        self.background_rect = self.background.get_rect()
        # 放大背景图片使之填充游戏界面
        self.background = pygame.transform.scale(self.background,(int(self.background_rect.width*3),
                                                                  int(self.background_rect.height*3.08)))  #3和3.08都是放大倍数

        self.viewport = setup.SCREEN.get_rect()
        self.caption = tools.get_image(setup.GRAPHICS['menu'],0,0,320,240,(156,44,173),3.2)


    def setup_cursor(self):
        self.cursor = tools.get_image(setup.GRAPHICS['crate_crash'],136,104,24,24,(173,93,41),3)

    def update(self,surface):
        surface.blit(self.background,self.viewport)
        surface.blit(self.caption,self.viewport)
        surface.blit(self.cursor,(90,450))  #(90,450) 表示光标初始位置

        self.info.update(surface)
        self.info.draw(surface)

