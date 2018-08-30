"""
Python 3.6
@Author: wrgsRay
"""


class Settings:
    # Settings for the game Alien Invasion

    def __init__(self):
        # Initial settings for the game
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship Settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60


def main():
    print('This file is for import only.')


if __name__ == '__main__':
    main()
