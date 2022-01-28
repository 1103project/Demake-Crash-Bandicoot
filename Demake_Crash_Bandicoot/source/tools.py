import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((800, 450))
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                if event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            pygame.display.update()
            self.clock.tick(30)
