import pygame
from .. import constants as C
from .import fruit
from .. import tools, setup
pygame.font.init()

class Info:
    def __init__(self,state, game_info):
        self.state = state
        self.game_info = game_info
        self.create_state_labels()
        self.create_info_labels()


    def create_state_labels(self):
        self.state_labels = []
        if self.state == 'main_menu':
            self.state_labels.append((self.create_label('Start Game',size=50),(190,480)))
            self.state_labels.append((self.create_label('Quit Game',size=50), (190,550)))



        if self.state == 'game_over':
            self.state_labels.append((self.create_label('Game Over', size=50), (390, 320)))







    def create_info_labels(self):
        pass

    def create_label(self,label,size=40):
        font = pygame.font.SysFont(C.FONT, size)
        label_image = font.render(label,True,(255,255,255)) # 将文字转化为图片，label表示目标文字，True表示抗锯齿，最后是文字颜色
        return label_image

    def update(self, surface):
        pass

    def draw(self,surface):
        for label in self.state_labels:
            surface.blit(label[0], label[1])
        surface.blit(self.create_label('*', size=50), (875, 35))
        surface.blit(self.create_label(str(self.game_info['fruit']), size=50), (900, 30))
        surface.blit(self.create_label('life:', size=50), (20, 35))
        surface.blit(self.create_label(str(self.game_info['life']), size=50), (90, 35))
        surface.blit(self.create_label(str(self.game_info['arrow']), size=100), (200, 30))


        surface.blit(tools.get_image(setup.GRAPHICS['bandicoot_fruit'], 155, 102, 34, 35, (0, 56, 222), 1.5), (800, 20))


