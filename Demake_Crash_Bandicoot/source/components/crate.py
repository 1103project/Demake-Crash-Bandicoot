import  pygame
from .. import tools, setup
from .. import constants as C

class Crate(pygame.sprite.Sprite):
    def __init__(self, x, y, crate_type):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.crate_type = crate_type
        self.frames_rects = [
            (74, 74, 43, 42),
            (117, 74, 42, 42),
            (159, 74, 42, 42),
            (201, 74, 45, 42),
            (74, 116, 43, 44),
            (117, 116, 42, 44),
            (159, 116, 42, 44),
            (201, 116, 45, 44)
        ]
        self.frames = []
        for frame_rect in self.frames_rects:
            self.frames.append(tools.get_image(setup.GRAPHICS['crate_all'], *frame_rect, C.RGB, C.BG_MULTI))

        # self.frame_index = 0
        self.image = self.frames[self.crate_type]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

