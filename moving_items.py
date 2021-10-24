import random
import pygame

import settings
from game_group_object import GameGroupObject
from ball import Ball
from ring import Ring

SPECIES = ["Ball", "Ring"]

class MovingItems(GameGroupObject):

    def __init__(self, screen):
        super().__init__(screen)
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
        if event.type != pygame.MOUSEBUTTONDOWN:
            return
        for item in self.items:
            if item.is_hit(event.pos):
                self.items.remove(item)
                pygame.mixer.Sound(settings.pop_sound).play()
                del(item)

    def __create_items_set(self):
        for _ in range(settings.start_moving_items):
            self.__add_new_item()

    def __add_new_item(self):
        if len(self.items) < settings.max_moving_items:
            class_ = self.__choose_items_class()
            self.add(class_(self.screen))

    def __choose_items_class(self):
        class_name = random.choice(SPECIES)
        return globals()[class_name]
