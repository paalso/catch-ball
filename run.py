import game_functions as gf
import pygame

import settings
import colors
from ball import Ball
from ring import Ring
##from moving_items import MovingItems


def main():
    pygame.init()

    FPS = settings.FPS
    screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Catch balls!")

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    game_objects = []

    ball = Ball(screen)
    ball = Ring(screen)
##    moving_items = MovingItems(screen)

    while not finished:
        clock.tick(FPS)
        finished = gf.check_events()
        gf.update_screen(screen, ball)

    pygame.quit()
    print("Good bye!")


if __name__ == '__main__':
    main()
