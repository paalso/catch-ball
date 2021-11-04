import pygame
import pygame_menu
from catch_ball import CatchBall
import settings

def start_the_game():
    CatchBall().run()


def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width,
                                        settings.screen_height))

    menu = pygame_menu.Menu('Cath a ball!',
                            settings.menu_width, settings.menu_height,
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add.text_input('Name : ', default='A Player')
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)


if __name__ == '__main__':
    main()
