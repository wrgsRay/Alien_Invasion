"""
Python 3.6
@Author: wrgsRay
"""
import pygame
import sys


def check_keydown_events(event, ship):
    # respond to key presses
    if event.key == pygame.K_RIGHT:
        # move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move the ship to the right.
        ship.moving_left = True


def check_keyup_events(event, ship):
    # respond to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recent drawn screen visible
    pygame.display.flip()


def main():
    print('Please import this module instead')


if __name__ == '__main__':
    main()