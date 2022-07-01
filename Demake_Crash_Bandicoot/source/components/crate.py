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
            (),
        ]
        self.frames = []
        for frame_rect in self.frame_rects:
            self.frames.append(tools.get_image(setup.GRAPHICS['crate_all'], *frame_rect, (0, 0, 0), C.BG_MULTI))

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y