from ..components import info
from ..components import player
import pygame


class Level:
    def __init__(self):
        self.finished = False
        self.next =None
        self.setup_player()

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
        surface.blit(self.player.image,self.player.rect)
        surface.fill((0,125,125))


