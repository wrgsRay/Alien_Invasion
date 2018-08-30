"""
Python 3.6
@Author: wrgsRay
"""
from bullet import Bullet
import pygame
import sys


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # respond to key presses
    if event.key == pygame.K_RIGHT:
        # move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move the ship to the right.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    # respond to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, alien, bullets):
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

    # Make the most recent drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    # Update position of bullets and get rid of old bullets.
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def main():
    print('Please import this module instead')


if __name__ == '__main__':
    main()