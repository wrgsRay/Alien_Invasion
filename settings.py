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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1


def main():
    print('This file is for import only.')


if __name__ == '__main__':
    main()
