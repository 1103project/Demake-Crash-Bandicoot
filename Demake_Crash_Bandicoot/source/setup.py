import pygame
from . import constants as C
from . import tools

pygame.init()
SCREEN = pygame.display.set_mode((C.SCREEN_W,C.SCREEN_H))

GRAPHICS = tools.load_graphics('resourses/img/Crash_bandicoot')
