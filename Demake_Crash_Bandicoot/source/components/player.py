import pygame
from .. import tools, setup
from .. import constants as C
import json
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name    # name = bandicoot
        self.load_data()
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

    def load_data(self):
        file_name = self.name + '.json'
        file_path = os.path.join('source/data',file_name)
        with open(file_path) as f:
            self.player_data = json.load(f)

    def setup_states(self):
        self.state = 'stand'
        self.face_right = True
        self.dead = False
        self.can_jump = True
        self.span = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0
        self.jump_vel = -15
        self.gravity = C.GRAVITY
        self.anti_gravity = C.ANTI_GRAVITY
        self.max_y_vel = 15
        self.max_x_vel = 10
        self.x_accel = 2

    def setup_timers(self):
        self.span_timer = 0  # 旋转攻击时长
        self.walking_timer = 0
        self.death_timer = 0

    def load_images(self):
        sheet = setup.GRAPHICS['bandicoot']
        frame_rects = self.player_data['image_frames']

        self.right_frames = []
        self.left_frames = []

        self.normal_frames = [self.right_frames, self.left_frames]

        self.all_frames = [
            self.right_frames,
            self.left_frames,
        ]

        self.right_frames = self.right_frames
        self.left_frames = self.left_frames

        for frame_rect in frame_rects:
            right_image = tools.get_image(sheet, frame_rect['x'], frame_rect['y'], frame_rect['width'],
                                          frame_rect['height'], (156,44,173), C.PLAYER_MULTI)
            left_image = pygame.transform.flip(right_image, True, False)
            self.right_frames.append(right_image)
            self.left_frames.append(left_image)

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self, keys):
        self.current_time = pygame.time.get_ticks()
        self.handle_states(keys)
        if self.span :
            self.span_attack_check()

    def handle_states(self, keys):
        self.can_jump_or_not(keys)
        if self.state == 'stand':
            self.stand(keys)
        elif self.state == 'walk':
            self.walk(keys)
        elif self.state == 'jump':
            self.jump(keys)
        elif self.state == 'die':
            self.die()
        elif self.state == 'fall':
            self.fall(keys)
        elif self.state == 'tp':
            self.tp()


        if self.face_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]

    def can_jump_or_not(self, keys):
        if not keys[pygame.K_SPACE]:
            self.can_jump = True

    def stand(self, keys):
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0
        if keys[pygame.K_d]:
            self.face_right = True
            self.state = 'walk'

        elif keys[pygame.K_a]:
            self.face_right = False
            self.state = 'walk'

        if keys[pygame.K_SPACE] and self.can_jump:
            if self.span != True:
                self.state = 'jump'
                self.y_vel = self.jump_vel

        elif keys[pygame.K_j]:
            self.span_attack()
            self.span_attack_check()


    def walk(self, keys):
        if keys[pygame.K_SPACE] and self.can_jump:
            self.state = 'jump'
            self.y_vel = self.jump_vel
        if self.current_time - self.walking_timer > 100:
            if self.span != True:
                if self.frame_index < 6:
                    self.frame_index += 1
                else:
                    self.frame_index = 1
            self.walking_timer = self.current_time
        if keys[pygame.K_d]:
            if self.span != True:
                self.face_right = True
                self.x_vel = 10
        elif keys[pygame.K_a]:
            if self.span != True:
                self.face_right = False
                self.x_vel = -10
        elif keys[pygame.K_j]:
            self.span_attack()
            self.span_attack_check()
        else:
            self.x_vel = 0
            self.state = 'stand'

    def jump(self, keys):
        self.frame_index = 4
        self.y_vel += self.anti_gravity
        self.can_jump = False
        if self.y_vel != 0:
            self.state = 'fall'

        if keys[pygame.K_d]:
            # self.x_vel = 10
            self.face_right = True
            self.x_vel = self.calc_vel(self.x_vel, self.x_accel, self.max_x_vel, True)
        elif keys[pygame.K_a]:
            # self.x_vel = -10
            self.face_right = False
            self.x_vel = self.calc_vel(self.x_vel, self.x_accel, self.max_x_vel, False)
        elif keys[pygame.K_j]:
            self.span_attack()
            self.span_attack_check()

        if not keys[pygame.K_SPACE]:
            self.state = 'fall'

    def fall(self, keys):
        self.y_vel = self.calc_vel(self.y_vel, self.gravity, self.max_y_vel)

        if keys[pygame.K_d]:
            self.face_right = True
            self.x_vel = self.calc_vel(self.x_vel, self.x_accel, self.max_x_vel, True)
        elif keys[pygame.K_a]:
            self.face_right = False
            self.x_vel = self.calc_vel(self.x_vel, self.x_accel, self.max_x_vel, False)
        elif keys[pygame.K_j]:
            self.span_attack()
            self.span_attack_check()

    def die(self):
        self.rect.y += self.y_vel
        self.y_vel += self.anti_gravity

    def go_die(self):
        self.dead = True
        self.y_vel = self.jump_vel
        self.frames_index = 8
        self.state = 'die'
        self.death_timer = self.current_time

    def tp(self):
        pass

    def calc_vel(self, vel, accel, max_vel, is_positive=True):
        if is_positive:
            return min(vel + accel, max_vel)
        else:
            return max(vel - accel, -max_vel)

    def span_attack(self):
        self.span = True
        self.span_timer = pygame.time.get_ticks()

    def span_attack_check(self):
        if pygame.time.get_ticks() - self.span_timer < 100:
            self.frame_index = 12
        elif pygame.time.get_ticks() - self.span_timer < 200:
            self.frame_index = 13
        elif pygame.time.get_ticks() - self.span_timer < 300:
            self.frame_index = 14
        elif pygame.time.get_ticks() - self.span_timer < 400:
            self.frame_index = 15
        elif pygame.time.get_ticks() - self.span_timer >= 500:
            self.span = False
        if self.span != True:
            self.frame_index = 1
