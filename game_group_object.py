import pygame


class GameGroupObject:

    counter = 0

    def __init__(self, screen):
        self.screen = screen
        self.items = []

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def empty(self):
        self.items.empty()

    def update(self):
        for e in self.items:
            e.update()

    def draw(self):
        for e in self.items:
            e.draw()


