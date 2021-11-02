import pygame

import basic_classes.colors as colors
import settings
from ball import Ball
from ring import Ring
from moving_items import MovingItems


class CatchBall():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Catch balls!")
        self.frame_rate = settings.FPS
        self.screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        self.clock = pygame.time.Clock()

        self.moving_items = MovingItems(self.screen)

    def run(self):
##        pygame.display.update()
        finished = False

        while not finished:
            self.clock.tick(self.frame_rate)
            finished = self.__check_events()
            self.__update_screen(self.screen)

        pygame.quit()
        print("Good bye!")

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.moving_items.handle_mouse_event(event)
                print('Click!')
        return False

    def __update_screen(self, items):
        pygame.display.update()

        self.screen.fill(settings.bg_color)
        self.moving_items.update()
        self.moving_items.draw()
