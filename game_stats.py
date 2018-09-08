"""
Python 3.6
@Author: wrgsRay
"""


class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        # Initialize statistics that can change during the game.
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0


def main():
    pass


if __name__ == '__main__':
    main()