import pygame
import random
import pathlib

import settings
import basic_classes.colors as colors


class Ball():

    maximum_area = settings.max_radius ** 2

    def __init__(self, screen):
        self.screen = screen
        self.radius = random.randint(settings.min_radius, settings.max_radius)

        # this property is not really necessary for the class Ball
        # otherwise, the Ring class throws an AttributeError:
        # 'Ring' object has no attribute 'inner_radius'
        self.inner_radius = 0   # workaround

        self.x = random.randint(
                self.radius, settings.screen_width - self.radius)
        self.y = random.randint(
                self.radius, settings.screen_height - self.radius)
        self.speed_x = self._generate_random_speed()
        self.speed_y = self._generate_random_speed()
        self.speed = (self.speed_x ** 2 + self.speed_y ** 2) ** 0.5
        self.color = random.choice(colors.COLORS)
        self.area_points = round(
                Ball.maximum_area / self._area() + \
                (self.speed / settings.min_speed))
        self.points = self.area_points

    def __str__(self):
        return "Ball: radius: {}, speed: {:.1f}, points: {}" \
                .format(self.radius, self.speed, self.points)

    def update(self):
        self.__process_wall_collisions()
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color,
                            (self.x, self.y), self.radius)

    def is_hit(self, hit_pos):
        return  self._dist(hit_pos) <= self.radius

    def _generate_random_speed(self):
        return random.randint(-settings.max_speed, settings.max_speed)

    def _recalculate_speed(self):
        self.speed = (self.speed_x ** 2 + self.speed_y ** 2) ** 0.5

    def _area(self):
        return self.radius ** 2

    def _dist(self, other):
        x, y = other
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

    def __process_wall_collisions(self):
        if self.x <= self.radius or \
            self.x + self.radius >= settings.screen_width:
            self.speed_x = -self.speed_x

        if self.y <= self.radius or \
            self.y + self.radius >= settings.screen_height:
            self.speed_y = -self.speed_y
