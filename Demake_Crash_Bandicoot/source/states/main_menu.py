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
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = tools.get_image(setup.GRAPHICS['crate_crash'],136,104,24,24,(173,93,41),3)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (90, 450)
        self.cursor.rect = rect
        self.cursor.state = 'Start Game'#状态机

    def update_cursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = 'Start Game'
            self.cursor.rect.y = 450
        elif keys[pygame.K_DOWN]:
            self.cursor.state = 'Quit Game'
            self.cursor.rect.y = 520
        elif keys[pygame.K_RETURN]:
            if self.state == 'Start Game':
                pass
            if self.state == 'Suit Game':
                pass

    def update(self,surface, keys):
        self.update_cursor(keys)
        surface.blit(self.background,self.viewport)
        surface.blit(self.caption,self.viewport)
        surface.blit(self.cursor.image, self.cursor.rect)  #(90,450) 表示光标初始位置

        self.info.update(surface)
        self.info.draw(surface)

