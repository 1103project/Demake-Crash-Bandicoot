import pygame
from source import tools, setup
from source.states import main_menu,load_screen,level


def main():
    game = tools.Game()
    state = level.Level()
    game.run(state)


if __name__ == '__main__':
    main()
