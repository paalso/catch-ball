import pygame

import settings
import basic_classes.colors as colors
from basic_classes.game_rect_object import GameRectObject
from basic_classes.text_object import TextObject

EMPTY_COLOR = (0, 0, 0)
text_sector_start = 0.40
text_sector_len = 1 - text_sector_start

class InfoPanel(GameRectObject):   # GameObject ?
    def __init__(self, screen, game_stats):
        super().__init__(screen, 0, 0,
                        settings.screen_width, settings.info_text_size * 3)
        self.stats = game_stats
        self.clicks = -1
        self.cought = -1
        self.score = -1
        self.items_left = -1
        self.seconds_left = settings.game_duration

    def update(self):
        # для экономии ресурсов: чтобы не переформировывать изображение
        # Info Panel, если ее текстовое содержание не изменилось
        if self.clicks == self.stats.clicks and \
            self.seconds_left == self.stats.seconds_left and \
            self.items_left == self.stats.items_left and \
            self.cought == self.stats.cought and \
            self.score == self.stats.score:
            return

        self.clicks = self.stats.clicks
        self.seconds_left = self.stats.seconds_left
        self.cought = self.stats.cought
        self.score = self.stats.score
        self.items_left = self.stats.items_left

        self.__clear()
        self.__set_clicks_info()
        self.__set_cought_info()
        self.__set_left_info()
        self.__set_score_info()
        self.__set_timer_info()

    def __clear(self):
        self.surface.fill(EMPTY_COLOR)
        self.surface.set_colorkey(EMPTY_COLOR)

    def __set_clicks_info(self):
        self.__set_text_info(
                "Clicks  {}".format(self.clicks),
                text_sector_start * self.width,
                settings.padding, settings.info_text_size)

    def __set_cought_info(self):
        self.__set_text_info(
                "Cought  {}".format(self.cought),
                (text_sector_start + 0.30 * text_sector_len) * self.width,
                settings.padding, settings.info_text_size)

    def __set_left_info(self):
        self.__set_text_info(
                "Targets left  {}".format(self.items_left),
                (text_sector_start + 0.60 * text_sector_len) * self.width,
                settings.padding, settings.info_text_size)

    def __set_score_info(self):
        self.__set_text_info(
                "Score  {}".format(self.score),
                (text_sector_start + 0.60 * text_sector_len) * self.width,
                settings.padding + settings.info_text_size,
                int(1.25 * settings.info_text_size), colors.ORANGE)

    def __set_timer_info(self):
        self.__set_text_info(
                "Timer  {}".format(self.seconds_left),
                text_sector_start * self.width,
                settings.padding + settings.info_text_size,
                int(1.25 * settings.info_text_size), colors.ORANGE)

    def __set_text_info(self, text_content, x, y, font_size,
                        color=settings.info_text_color):
        text = TextObject(x, y, text_content, color, font_size)
        text.draw(self.surface)