import pygame
import random

import basic_classes.colors as colors
import settings
from ball import Ball


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def non_zeroize(x):
    return 1 if x == 0 else x


def stochasticize_speed(x, dx, min_x, max_x):
    x += dx + random.random()
    x = max(x, min_x)
    x = min(x, max_x)
    return x


class Ring(Ball):
    def __init__(self, screen):
        super().__init__(screen)
        self.radius = random.randint(settings.min_radius, settings.max_radius)
        self.inner_radius = round(self.radius * settings.inner_radius_quotient)
        self.frames_counter = 0
        # self.point = self._calculate_point()

    def __str__(self):
        return "Ring: {}, {}".format(self.radius, self.points)

    def update(self):
        self.frames_counter += 1
        self.__process_wall_collisions()

        self.x += self.speed_x
        self.y += self.speed_y

        self.speed_x += random.randint(-settings.frame_speed_stochastic_change,
                                        settings.frame_speed_stochastic_change)
        self.speed_y += random.randint(-settings.frame_speed_stochastic_change,
                                        settings.frame_speed_stochastic_change)

        if self.frames_counter == settings.speed_change_frames:
            self.frames_counter = 0
            self.__randomize_speed()

        self._update_points()

    def draw(self):
        pygame.draw.circle(self.screen, self.color,
                            (self.x, self.y), self.radius)
        pygame.draw.circle(self.screen, settings.bg_color,
                            (self.x, self.y), self.inner_radius)

    def is_hit(self, hit_pos):
        return self.inner_radius <= self._dist(hit_pos) <= self.radius

    def __process_wall_collisions(self):
        if self.x <= self.radius:
            self.__inverse_speed_x()
            self.x = self.radius
        elif self.x >= settings.screen_width - self.radius:
            self.__inverse_speed_x()
            self.x = settings.screen_width - self.radius
        if self.y <= self.radius:
            self.__inverse_speed_y()
            self.y = self.radius
        elif self.y >= settings.screen_height - self.radius :
            self.__inverse_speed_y()
            self.y = settings.screen_height - self.radius

        self._update_points()

    def _update_points(self):
        self._recalculate_speed()
        self.points = round((settings.max_radius / self.radius) ** 2 + \
                    (self.speed / settings.min_speed) ** 0.5)

    def __randomize_speed(self):
        self.speed_x = self._generate_random_speed()
        self.speed_y = self._generate_random_speed()

    def __inverse_speed_x(self):
        self.speed_x = -abs(self._generate_random_speed()) * \
                        non_zeroize(sgn(self.speed_x))
        self.speed_y = self.speed_x = self._generate_random_speed()

    def __inverse_speed_y(self):
        self.speed_x = self._generate_random_speed()
        self.speed_y = -abs(self._generate_random_speed()) * \
                        non_zeroize(sgn(self.speed_y))

