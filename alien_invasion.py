"""
Python 3.6
@Author: wrgsRay
"""
import pygame
import sys


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')
    # Set background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        # Make the most recent drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
