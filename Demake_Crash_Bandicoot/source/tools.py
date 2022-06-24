import pygame
import os


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((800, 450))
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            GRAPHICS = load_graphics('resourses/img/Crash_bandicoot')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                if event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            image = get_image(GRAPHICS['bandicoot_stand'], 136, 73, 38, 42, (173,44,148), 1.5)
            self.screen.blit(image, (300, 300))
            pygame.display.update()
            self.clock.tick(30)


def load_graphics(path, accept=('.jpg', '.png', '.psd')):
    '''
    将path路径下的所有.jpg.png.psd文件导入到一个字典里，key为文件名，value为文件。
    返回值为一个字典，建议使用时，字典名以文件名命名。
    '''
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics


def get_image(sheet,x,y,width,height,colorkey,scale): #scale 表示放大的倍数
    image = pygame.Surface((width,height))
    image.blit(sheet,(0,0),(x,y,width,height)) #0,0表示画到surface的位置，x，y，width，height表示从sheet里哪个区域取出来
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    return image