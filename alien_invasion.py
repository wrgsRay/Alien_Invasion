"""
Python 3.6
@Author: wrgsRay
"""
import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship.
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
