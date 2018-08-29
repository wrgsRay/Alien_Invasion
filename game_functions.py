"""
Python 3.6
@Author: wrgsRay
"""
import pygame
import sys


def check_events():
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recent drawn screen visible
    pygame.display.flip()


def main():
    print('Please import this module instead')


if __name__ == '__main__':
    main()