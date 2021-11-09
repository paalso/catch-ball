import random
import pygame

import settings
from basic_classes.game_group_object import GameGroupObject
from ball import Ball
from ring import Ring

SPECIES = ["Ball", "Ring"]

class MovingItems(GameGroupObject):

    def __init__(self, screen, game_stats):
        super().__init__(screen)
        self.stats = game_stats
        self.frames_counter = 0
        self.__create_items_set()

    def update(self):
        self.frames_counter += 1
##        random.shuffle(self.items)
        super().update()

        if self.frames_counter == settings.creation_new_item_frames:
            self.frames_counter = 0
            self.__add_new_item()

    def handle_mouse_event(self, event):
        self.stats.inc_clicks()
        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        # fine for extra clicks
        self.stats.inc_score(-settings.extra_click_cost)

        for item in self.items:
            if item.is_hit(event.pos):
                self.items.remove(item)
                self.stats.upd_items_left(-1)
                self.stats.inc_score(settings.extra_click_cost)
                self.stats.inc_score(item.points)
                self.stats.inc_cought()
                print("Caught {}".format(item))
                pygame.mixer.Sound(settings.pop_sound).play()
                del(item)       # ?

    def __create_items_set(self):
        for _ in range(settings.start_moving_items):
            self.__add_new_item()

    def __add_new_item(self):
        if len(self.items) < settings.max_moving_items:
            class_ = self.__choose_items_class()
            self.add(class_(self.screen))
        self.stats.upd_items_left(1)

    def __choose_items_class(self):
        class_name = random.choice(SPECIES)
        return globals()[class_name]
