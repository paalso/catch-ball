import pygame
import settings


def check_events(game_objects):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_objects.handle_mouse_event(event)
            print('Click!')
    return False


def update_screen(screen, items):
    pygame.display.update()
    screen.fill(settings.bg_color)
    items.update()
    items.draw()
