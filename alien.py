"""
Python 3.6
@Author: wrgsRay
"""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # A class to represent a single alien in the fleet.

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        # Draw the alien at its current location
        self.screen.blit(self.image, self.rect)


def main():
    pass


if __name__ == '__main__':
    main()