import pygame


def create_enemy(enemy_date):
    pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass


class Turtle(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = 1
        pass


class Flyingfish(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = 2
        pass


class Slim(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.type = 3
        pass
