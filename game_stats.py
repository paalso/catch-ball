import pygame
import settings


class GameStats:

    def __init__(self):
        self.clicks = 0
        self.cought = 0
        self.score = 0
        self.items_left = 0
        self.start_ticks = pygame.time.get_ticks()
        self.current_ticks = self.start_ticks

    @property
    def seconds_left(self):
        self.seconds_passed = (self.current_ticks - self.start_ticks) // 1000
        return settings.game_duration - self.seconds_passed

    @property
    def final_score(self):
        score_per_second = self.score / self.seconds_passed
        return int(self.score + settings.finish_early_bonus_quotient * \
                            score_per_second * self.seconds_left)

    def inc_clicks(self):
        self.clicks += 1

    def inc_cought(self):
        self.cought += 1

    def inc_score(self, score):
        self.score += score

    def upd_items_left(self, change):
        self.items_left += change

    def upd_ticks(self):
        self.current_ticks = pygame.time.get_ticks()
