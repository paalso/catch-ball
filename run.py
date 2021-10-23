import game_functions as gf
import pygame

import settings
import colors
from ball import Ball
from ring import Ring
from moving_items import MovingItems


def main():
    pygame.init()

    FPS = settings.FPS
    screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Catch balls!")

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
##    game_objects = []

    moving_items = MovingItems(screen)

    while not finished:
        clock.tick(FPS)
        finished = gf.check_events(moving_items)
        gf.update_screen(screen, moving_items)

    pygame.quit()
    print("Good bye!")


if __name__ == '__main__':
    main()
