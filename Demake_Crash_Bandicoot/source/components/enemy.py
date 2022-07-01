import pygame
from .. import tools, setup
from .. import constants as C

def create_enemy(enemy_date):
    # enemy_type = enemy_data['type']
    # x, y_bottom, direction, color = enemy_data['x'], enemy_data['y'], enemy_data['direction'], enemy_data['color']
    #
    # if enemy_type == 0:
    #     enemy = Turtle(x, y, direction, "Turtle", color)
    # elif enemy_type == 1:
    #     enemy = Flyingfish(x, y, direction, "Flyingfish", color)
    # elif enemy_type == 2:
    #     enemy = Slim(x, y, direction, "Slim", color)
    #
    # return enemy
    pass

class Enemy(pygame.sprite.Sprite):
    # def __init__(self, x, y_bottom, direction, name, frame_rects):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.direction = direction
    #     self.name = name
    #     self.frame_index = 0
    #     self.left_frames = []
    #     self.right_frames = []
    #
    #     self.load_frames(frame_rects)
    #     self.frames = self.left_frames if self.direction == 0 else self.right_frames
    #     self.image = self.frames[self.frame_index]
    #     self.rect = self.image.get_rect()
    #     self.rect.x = x
    #     self.rect.y = y
    #
    # def load_frames(self, frame_rects):
    #     for frame_rect in frame_rects:
    #         left_frame = tools.get_image(setup.GRAPHICS['enemies'], *frame_rect, (0, 0, 0), C.ENEMY_MULTI)
    #         right_frame = pygame.transform.flip(left_frame, True, False)
    #         self.left_frames.append(left_frame)
    #         self.right_frames.append(right_frame)
    pass

class Turtle(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = 1
        pass


class Flyingfish(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = 2
        pass


class Slim(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = 3
        pass
