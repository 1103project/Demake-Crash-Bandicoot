import pygame
from .. import tools, setup
from .. import constants as C


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
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
        self.big = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet0 = setup.GRAPHICS['bandicoot_stand']
        sheetr1 = setup.GRAPHICS['bandicoot_run_right1']
        sheetr2 = setup.GRAPHICS['bandicoot_run_right2']
        sheetr3 = setup.GRAPHICS['bandicoot_run_right3']
        sheetl1 = setup.GRAPHICS['bandicoot_run_left1']
        sheetl2 = setup.GRAPHICS['bandicoot_run_left2']
        sheetl3 = setup.GRAPHICS['bandicoot_run_left3']
        sheets = [sheet0, sheetr1,sheetr2, sheetr3, sheetl1, sheetl2, sheetl3]
        self.right_frames = []
        self.left_frames = []
        self.up_frames = []
        self.down_frames = []

        # frame_rects = [
        #     (),
        #     (),
        #     (),
        #     (),
        #     (),
        #     ()
        # ]

        # for frame_rect in frame_rects:
        for sheet in sheets:
            right_image = tools.get_image(sheet, 134, 69, 46, 61, (156, 44, 173), 1)
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
            self.frame_index %= 6
        self.image = self.frames[self.frame_index]
