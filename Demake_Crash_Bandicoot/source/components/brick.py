import  pygame
from .. import tools, setup
from .. import constants as C

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, brick_type, color=None):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.brick_type = brick_type
        bright_frame_rect = []
        dark_frame_rect = []

        if not color:
            self.frame_rects = bright_frame_rect
        else:
            self.frame_rects = dark_frame_rect

        self.frames = []
        for frame_rect in self.frame_rects:
            self.frames.append(tools.get_image(setup.GRAPHICS['tile_set'], *frame_rect, (0, 0, 0), C.BG_MULTI))

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y