import pygame
import random

import settings
import colors
from ball import Ball


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


class Ring(Ball):
    def __init__(self, screen):
        super().__init__(screen)
        self.radius = random.randint(settings.min_radius, settings.max_radius)
        self.inner_radius = round(self.radius * settings.inner_radius_quotient)
        # self.point = self._calculate_point()

    def __str__(self):
        return "Ring: {}, {}".format(self.radius, self.point)

    def update(self):
        self.__process_wall_collisions()
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color,
                            (self.x, self.y), self.radius)
        pygame.draw.circle(self.screen, settings.bg_color,
                            (self.x, self.y), self.inner_radius)

    def hit(self):
        pass

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

        self._update_point()
        print(self.speed_x, self.speed_y, self.point)

    def _update_point(self):
        self._update_speed()
        self.point = round((settings.max_radius / self.radius) ** 2 + \
                    (self.speed / settings.min_speed) ** 0.5)

    def __inverse_speed_x(self):
        self.speed_x = -abs(self._generate_random_speed()) * sgn(self.speed_x)
        self.speed_y = self.speed_x = self._generate_random_speed()

    def __inverse_speed_y(self):
        self.speed_x = self._generate_random_speed()
        self.speed_y = -abs(self._generate_random_speed()) * sgn(self.speed_y)


    # НУЖЕН ЛИ?
##    def __calculate_speed(self):
##        return (self.speed_x ** 2 + self.speed_y ** 2) ** 0.5

##    def __inverse_speed_x(self):
##        self.speed_x = -self.speed_x + self.__random_speed_biase()
##        self.speed_y = self.speed_y + self.__random_speed_biase()
##
##    def __inverse_speed_y(self):
##        self.speed_x = self.speed_x + self.__random_speed_biase()
##        self.speed_y = -self.speed_y + self.__random_speed_biase()

##    def __random_sign(self):
##        return random.choice((-1, 0, 1))
##
##    def __random_speed_biase(self):
##        return self.__random_sign() * random.randint(
##                settings.wall_reflection_speed_min_biase,
##                settings.wall_reflection_speed_max_biase)