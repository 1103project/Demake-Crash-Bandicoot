import pygame
from .. import tools, setup
from .. import constants as C


class Player(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name    # name = bandicoot
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def setup_states(self):
        self.face_right = True
        self.dead = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0

    def load_images(self):
        sheet = setup.GRAPHICS['bandicoot_stand']
        self.frames = []
        self.frames.append(tools.get_image(sheet,136,73,38,42,(156,44,173),1))

    def update(self,keys):
        if keys[pygame.K_d]:
            self.x_vel = 5
        if keys[pygame.K_a]:
            self.x_vel = -5

