from .. import setup
from ..components import info
from ..components import player
import pygame


class Level:
    def __init__(self):
        self.finished = False
        self.next =None
        self.info = info.Info('level')
        self.setup_background()
        self.setup_player()

    def setup_background(self):
        self.background = setup.GRAPHICS['menubackground']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,(int(rect.width*3),
                                                                  int(rect.height*3.08)))  #放大，同mainMenu
        self.background_rect = self.background.get_rect()

    def setup_player(self):
        self.player = player.Player('bandicoot')
        self.player.rect.x = 300
        self.player.rect.y = 300

    def update(self,surface,keys):
        self.player.update(keys)
        self.update_player_position()
        self.draw(surface)

    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def draw(self,surface):

        surface.fill((0,125,125))
        surface.blit(self.player.image, self.player.rect)
        self.info.draw(surface)


