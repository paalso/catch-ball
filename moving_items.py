import random
import pygame

import settings
from game_group_object import GameGroupObject
from ball import Ball
from ring import Ring

SPECIES = ["Ball", "Sort"]

class MovingItems(GameGroupObject):

    def __init__(self, screen):
        super().__init__(screen)
        self.counter = 1
        self.create_items()

    def create_items(self):
        for _ in range(settings.max_moving_items):
            class_name = self.choose_items_class()
            item = Ball(self.screen) if class_name == "Ball" else Ring(self.screen)
            self.add(item)

    def choose_items_class(self):
        return random.choice(SPECIES)
##        class_name = random.choice(SPECIES)
##        return globals()[class_name]()

    def update(self):
        random.shuffle(self.items)
        super().update()

    def handle_mouse_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return
        print(event.pos)

        for item in self.items:
            if item.is_hit(event.pos):
                self.items.remove(item)
                pygame.mixer.Sound(settings.pop_sound).play()
                del(item)
