"""
Python 3.6
@Author: wrgsRay
"""


class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        # Initialize statistics that can change during the game.
        self.ships_left = self.ai_settings.ship_limit


def main():
    pass


if __name__ == '__main__':
    main()