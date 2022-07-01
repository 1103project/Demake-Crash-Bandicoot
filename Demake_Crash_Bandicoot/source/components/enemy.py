import pygame
from .. import tools, setup
from .. import constants as C

def create_enemy(enemy_data):
    enemy_type = enemy_data['type']
    x, y_bottom, direction = enemy_data['x'], enemy_data['y'], enemy_data['direction']

    if enemy_type == 0:
        enemy = Turtle(x, y_bottom, direction, "Turtle")
    # elif enemy_type == 1:
    #     enemy = Flyingfish(x, y_bottom, direction, "Flyingfish")
    # elif enemy_type == 2:
    #     enemy = Slim(x, y_bottom, direction, "Slim")

    return enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y_bottom, direction, name, frame_rects):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.name = name
        self.frame_index = 0
        self.left_frames = []
        self.right_frames = []

        self.load_frames(frame_rects)
        self.frames = self.left_frames if self.direction == 0 else self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y_bottom

        self.timer = 0

    def load_frames(self, frame_rects):
        for frame_rect in frame_rects:
            left_frame = tools.get_image(setup.GRAPHICS['turtle'], *frame_rect, C.rgb, C.ENEMY_MULTI)
            right_frame = pygame.transform.flip(left_frame, True, False)
            self.left_frames.append(left_frame)
            self.right_frames.append(right_frame)

    def update(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.timer > 125:
            self.frame_index = (self.frame_index + 1) % 2
            self.image = self.frames[self.frame_index]
            self.timer = self.current_time
class Turtle(Enemy):
    def __init__(self, x, y_bottom, direction, name):
        frame_rects = [(84, 111, 64, 29), (148, 111, 64, 29)]
        Enemy.__init__(x, y_bottom, direction, name, frame_rects)



# class Flyingfish(Enemy):
#     def __init__(self, x, y_bottom, direction, name):
#         frame_rects = [()]
#         Enemy.__init__(x, y_bottom, direction, name, frame_rects)



# class Slim(Enemy):
#     def __init__(self, x, y_bottom, direction, name):
#         frame_rects = [()]
#         Enemy.__init__(x, y_bottom, direction, name, frame_rects)

