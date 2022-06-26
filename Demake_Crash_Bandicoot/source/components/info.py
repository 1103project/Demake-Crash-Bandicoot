import pygame
from .. import constants as C
pygame.font.init()

class Info:
    def __init__(self,state):
        self.state = state
        self.create_state_labels()
        self.create_info_labels()

    def create_state_labels(self):
        self.state_labels = []
        if self.state == 'main_menu':
            self.state_labels.append((self.create_label('Start Game',size=50),(190,480)))
            self.state_labels.append((self.create_label('Quit Game',size=50), (190,550)))

    def create_info_labels(self):
        pass

    def create_label(self,label,size=40):
        font = pygame.font.SysFont(C.FONT, size)
        label_image = font.render(label,True,(255,255,255)) # 将文字转化为图片，label表示目标文字，True表示抗锯齿，最后是文字颜色
        return label_image
    def update(self):
        pass

    def draw(self,surface):
        for label in self.state_labels:
            surface.blit(label[0],label[1])


