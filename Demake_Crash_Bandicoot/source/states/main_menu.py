import pygame
from .. import setup
from .. import tools
from ..components import info

class MainMenu:
    def __init__(self):
        game_info = {
            'fruit': 0,
            'life': 3,
        }
        self.start(game_info)
    def start(self, game_info):
        self.game_info = game_info
        self.setup_background()
        self.setup_cursor()
        self.info = info.Info('main_menu', self.game_info)
        self.finished = False
        self.next = 'level'

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
        rect.x, rect.y = (90, 450)  #(90,450) 表示光标初始位置
        self.cursor.rect = rect
        self.cursor.state = 'Start Game'  #初始状态

    def update_cursor(self, keys):
        if keys[pygame.K_w]:
            self.cursor.state = 'Start Game'
            self.cursor.rect.y = 450
        elif keys[pygame.K_s]:
            self.cursor.state = 'Quit Game'
            self.cursor.rect.y = 520
        elif keys[pygame.K_RETURN]:
            self.reset_game_info()
            if self.cursor.state == 'Start Game':
                self.finished = True
            if self.cursor.state == 'Quit Game':
                pygame.quit()

    def update(self,surface, keys):

        self.update_cursor(keys)

        surface.blit(self.background,self.viewport)
        surface.blit(self.caption,self.viewport)
        surface.blit(self.cursor.image, self.cursor.rect)

        self.info.update(surface)
        self.info.draw(surface)

    def reset_game_info(self):
        self.info.update({
            'fruit': 0,
            'life': 3
        })

