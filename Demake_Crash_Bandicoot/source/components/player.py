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
        self.face_right = True
        self.dead = False
        self.big = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

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

    def update(self,keys):
        self.current_time = pygame.time.get_ticks()
        if keys[pygame.K_d]:
            self.x_vel = 5
            self.y_vel = 0
            self.frames = self.right_frames
        if keys[pygame.K_a]:
            self.x_vel = -5
            self.y_vel = 0
            self.frames = self.left_frames
        if self.current_time - self.walking_timer > 100:
            self.walking_timer = self.current_time
            self.frame_index += 1
            self.frame_index %= 7
        self.image = self.frames[self.frame_index]
