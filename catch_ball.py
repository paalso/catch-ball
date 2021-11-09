import pygame
import sys

import basic_classes.colors as colors
from basic_classes.text_object import TextObject
from basic_classes.text import Text
import settings
from ball import Ball
from ring import Ring
from info_panel import InfoPanel
from moving_items import MovingItems
from game_stats import GameStats


class CatchBall():
    def __init__(self, player_name):
        if not player_name:
            player_name = None
        self.player_name = player_name
        print(f"Hello, {self.player_name}")
        pygame.init()
        pygame.display.set_caption("Catch balls!")
        self.frame_rate = settings.FPS
        self.screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        self.clock = pygame.time.Clock()

        self.stats = GameStats(self.player_name)
        self.moving_items = MovingItems(self.screen, self.stats)
        self.info_panel = InfoPanel(self.screen, self.stats)

        self.depicted_objects = [self.moving_items, self.info_panel]

    def run(self):

        while True:
            self.clock.tick(self.frame_rate)
            finished = self.__check_events()
            self.__update_screen(self.screen)

        pygame.quit()
        print("Good bye!")

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.__exit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.moving_items.handle_mouse_event(event)
        return False

    def __update_screen(self, items):
        pygame.display.update()

        self.screen.fill(settings.bg_color)

        self.stats.upd_ticks()

        # Рефакторить!
        if self.stats.items_left == 0:
            self.__endgame("win")

        if self.stats.seconds_left < 0:
            self.__endgame("fail")

        for o in self.depicted_objects:
            o.update()

        for o in self.depicted_objects:
            o.draw()

    def __endgame(self, game_result):
        pygame.time.delay(500)
        final_img = pygame.transform.scale(
            pygame.image.load(settings.endgame_imgs[game_result]),
            (settings.screen_width, settings.screen_height))
        self.screen.blit(final_img, (0, 0))
        pygame.mixer.Sound(settings.endgame_sounds[game_result]).play()
        goodbye_msg = settings.endgame_msgs[game_result].format(
                                                        self.stats.final_score)
        print(goodbye_msg)
        Text(self.screen, goodbye_msg, *settings.endgame_msg_position,
                settings.endgame_msg_color, settings.endgame_msg_size).draw()
        self.stats.upd_game_results_records()
        pygame.display.update()
        pygame.time.wait(settings.endgame_delay)
        self.__exit_game()

    def __exit_game(self):
        pygame.quit()
        sys.exit()
