import pygame
from source import tools
from source.states import main_menu, load_screen, level


def main():

    #bgm
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('resourses/music/main_theme_sped_up.ogg')
    pygame.mixer.music.play(-1)


    state_dict = {
        'main_menu': main_menu.MainMenu(),
        'level': level.Level(),
        'game_over': load_screen.GameOver()
    }

    game = tools.Game(state_dict, 'main_menu')
    game.run()


if __name__ == '__main__':
    main()
