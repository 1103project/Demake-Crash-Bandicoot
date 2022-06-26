import pygame


class Fruit(pygame.sprite.Sprite):
    #定义构造函数
    def __init__(self, fruit_filename, fruit_location):
        #调用父类来初始化子类
        pygame.sprite.Sprite.__init__(self)
        #加载水果图片
        self.image = pygame.image.load(fruit_filename)
        #获取图片rect区域
        self.rect = self.image.get_rect()
        #设置图片位置
        self.rect.topleft = fruit_location
    #屏幕画出水果
    def fruit_draw(self):
        screen.blit(self.image, self.rect)
    #定义碰撞
    def fandb_crash(self, other, fruit_filename):
        crash_result = pygame.sprite.collide_rect(self, other)
        if crash_result:
            #原来水果图变透明
            transparent = (0, 0, 0, 0)
            self.image.fill(transparent)
            #左上角画出水果buff
            fruit_image = pygame.image.load(fruit_filename)
            fruit_image = pygame.transform.scale(fruit_image, (10, 10))
            screen.blit(fruit_image, (0, 0))
            #定义时间
            time_begin = 0
            time_now = pygame.time.get_ticks()
            time_begin = time_now
            #buff维持10秒，10秒后左上角水果图片变透明
            if time_now - time_begin >= 1000:
                fruit_image.fill(transparent)
            else:
                pass
        else:
            pass

