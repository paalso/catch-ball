import pygame
import settings
from ball import Ball


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
    return False


def update_screen(screen, items):
    pygame.display.update()
    screen.fill(settings.bg_color)
    items.update()
    items.draw()
