import pygame
from .. import tools, setup
from .. import constants as C

def create_enemy(enemy_data):
    enemy_type = enemy_data['type']
    x, y_bottom, direction = enemy_data['x'], enemy_data['y'], enemy_data['direction']

    if enemy_type == 0:
        enemy = Turtle(x, y_bottom, direction, "turtle")
    elif enemy_type == 1:
        enemy = Flyingfish(x, y_bottom, direction, "flyingfish")
    elif enemy_type == 2:
        enemy = Slim(x, y_bottom, direction, "slim")

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
        self.x_vel = -1 * C.ENEMY_SPEED if self.direction == 0 else C.ENEMY_SPEED
        self.y_vel = 0
        self.gravity = C.GRAVITY
        self.state = 'walk'

    def load_frames(self, frame_rects):
        for frame_rect in frame_rects:
            left_frame = tools.get_image(setup.GRAPHICS[self.name], *frame_rect, C.RGB, C.ENEMY_MULTI)
            right_frame = pygame.transform.flip(left_frame, True, False)
            self.left_frames.append(left_frame)
            self.right_frames.append(right_frame)

    def update(self,level):
        self.current_time = pygame.time.get_ticks()
        self.handle_states()
        self.update_position(level)

    def handle_states(self):
        if self.state == 'walk':
            self.walk()
        elif self.state == 'jump':
            self.jump()
        elif self.state == 'die':
            self.die()
        elif self.state == 'fall':
            self.fall()

        if self.direction:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]

    def update_position(self,level):
        self.rect.x += self.x_vel
        self.check_x_collisions(level)
        self.rect.y += self.y_vel
        self.check_y_collision(level)

    def check_x_collisions(self,level):
        sprite = pygame.sprite.spritecollideany(self,level.ground_items_group)
        if sprite:
            self.direction = 1 if self.direction == 0 else 0
            self.x_vel *= -1

    def check_y_collision(self,level):
        check_group = pygame.sprite.Group.copy(level.ground_items_group)
        tools.sprite_group_add(check_group,level.crate_group)
        sprite = pygame.sprite.spritecollideany(self,check_group)
        if sprite:
            if self.rect.top < sprite.rect.top:
                self.rect.bottom = sprite.rect.top
                self.y_vel = 0
                self.state = 'walk'

        level.check_will_fall(self)

    def fall(self):
        if self.y_vel < 10:
            self.y_vel += self.gravity

    def walk(self):
        if self.current_time - self.timer > 125:
            self.frame_index = (self.frame_index + 1) % 2
            self.image = self.frames[self.frame_index]
            self.timer = self.current_time

class Turtle(Enemy):
    def __init__(self, x, y_bottom, direction, name):
        frame_rects = [(84, 111, 64, 29), (148, 111, 64, 29)]
        Enemy.__init__(self,x, y_bottom, direction, name, frame_rects)



class Flyingfish(Enemy):
    def __init__(self, x, y_bottom, direction, name):
        frame_rects = [()]
        Enemy.__init__(self,x, y_bottom, direction, name, frame_rects)



class Slim(Enemy):
    def __init__(self, x, y_bottom, direction, name):
        frame_rects = [()]
        Enemy.__init__(self,x, y_bottom, direction, name, frame_rects)

