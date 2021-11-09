import pygame


class Text():   # GameObject ?

    def __init__(self, screen, text, x, y, color, font_size, font_family=None):
        self.x = x
        self.y = y
        self.screen = screen
        self.text = text
        self.color = color
        try:
            self.font = pygame.font.SysFont(font_family, font_size)
        except:
            self.font = pygame.font.SysFont(None, font_size)

    def draw(self):
        text_lines = self.text.split("\n")
        y = self.y
        for line in text_lines:
            text_surf = self.font.render(line, True, self.color)
            self.screen.blit(text_surf, (self.x, y))
            y += text_surf.get_rect().height
