# За основу этого класса (недоработанного Popup) взят класс из игры Alien Invasion
# Его задача состояла в том, чтобы формировать (всплывающее) текстовое окно,
# к-е можно впоследствии закрыть каким-л. действием мыши или клавиатуры
# Для этой игры, впрочем хватало только функциональности информационного
# текстового окна
# В pygame очень неудобно организована работа с текстом -
# в частности, он не переносится
# В Popup из Alien Invasion для переносов текста в ограниченной по ширине области
# использовалась ф-я word_wrap, но, все равно это было не очень неудобно:
# например, при попытке сформировать нечто вроде таблицы, очень сложно
# было подобрать отступы (с помощью пробелов) между элементами строк, при этом
# начинались проблемы с переносом строк и т.п.

# В этой игре я попытался реализовать класс иначе:
# - разбиваем текст на строки (для этого он изначально должен содержать символы
# переносов строк)
# - методом render() экземпляра Font формируем "полоски"-поверхности с изображением
# этих строк, сохраняем
# - рассчитываем размеры общей поверхности, к-я их будет содержать (высота = 
# сумме высот, ширина = максимуму ширин)
# - формируем поверхность необходимых размеров
# - накладываем на него полученные "полоски"
# Profit!
# Но что-то недополучилось, и я реализовал гораздо более простой вариант отображения 
# многострочного текста - класс Text
# Он принимает текст, разбивет на строки и просто печатает их одну под другой
# Очень примитивно, но работает
# Кстати, нужно таки добавить возможность использования разных шрифтов (пока он работает
# на дефолтном pygame.font.Font(None, ...)) - например могут понадобиться
# моноширинные шрифтв для печаити таблиц.


import pygame
import pygame.freetype
from basic_classes.game_rect_object import GameRectObject


EMPTY_COLOR = (0, 0, 0)

class Popup(GameRectObject):   # GameObject ?

    def __init__(self, screen, x, y, text,
                color, back_color, font_name, font_size,
                transparent=False, centralized=False):
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = (0, 0)

        self.back_color = back_color if back_color else EMPTY_COLOR
        self.transparent = transparent
        self.text = text
        self.color = color
        self.font = pygame.freetype.SysFont(None, font_size)

        self.surface = self.__get_suface()
        self.rect = self.surface.get_rect()

        # if centralized center = x, y else topleft = x, y
        if centralized:
            self.rect.center = (self.x, self.y)
        else:
            self.rect.topleft = (self.x, self.y)

        print(self.surface, self.rect)

    def __get_suface(self):
        lines = self.text.split("\n")
        heights = []
        widths = []
        text_surfs = []
##        print(lines)
        for line in lines:
##            print(line)
            text = self.font.render(line, True, self.color)
            text_surf, text_rect = text
            text_surfs.append(text_surf)
            heights.append(text_rect.height)
            widths.append(text_rect.width)

        width = max(widths)
        height = sum(heights)
        surface = pygame.Surface((width, height))

        from_top = 0
        for i in range(len(text_surfs)):
            surface.blit(text_surfs[i], (0, from_top))
            from_top += heights[i]

##        if self.transparent:
##            surface.fill(EMPTY_COLOR)
##            surface.set_colorkey(EMPTY_COLOR)
##        else:
##            surface.fill(self.back_color)

        return surface
