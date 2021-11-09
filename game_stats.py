import os, csv, time
import pygame
import settings


def ellipsis_string(string, max_len=19):
    if len(string) > max_len - 1:
        return string[:max_len - 3] + ".."
    return string


class GameStats:

    # format specifiers values
    name_width = 20
    game_score_width = 4
    game_date_width = 20

    @staticmethod
    def write_new_record(file_name, data):
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                print("name,game_score,game_date",file=f)
        with open(file_name, "a", encoding="utf-8") as f:
            print(",".join(map(str, data)),file=f)

    @staticmethod
    def sort_records_decreasing(file_name, key):
        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
        header, *records = data
        id_ = header.index(key)
        records.sort(key=lambda record: -int(record[id_]))

        with open(file_name, "w", encoding="utf-8") as f:
            print(",".join(header), file=f)
            for record in records:
                print(",".join(record), file=f)

    def generate_records_textlines(file_name, textlines_qty=10):
        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
        header, *records = data
        records = records[:textlines_qty]

        textlines_header = \
            "The best results:\n" + \
            "       Name         Score         Date\n"
        textlines = []
        for record in records:
            name, *rest = record

            # format specifiers values are hardcoded, desirable TO FIX
            textlines.append(
                    "{:<20}{:>4}{:>20}".format(
                    ellipsis_string(name), *rest))
        return textlines_header + "\n".join(textlines)

    def __init__(self, player_name):
        self.player_name = player_name
        self.game_results_file = settings.game_results
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
        return int(self.score + settings.finish_early_bonus_factor * \
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

    def upd_game_results_records(self):
        GameStats.write_new_record(self.game_results_file,
                            (self.player_name, self.final_score,
                            time.strftime("%Y-%m-%d %H:%M")))
        GameStats.sort_records_decreasing(self.game_results_file, "game_score")
        print(GameStats.generate_records_textlines(self.game_results_file))
