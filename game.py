import pygame
import sys

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """"""
    def run_game(self):
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

    #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__== '__main__':
    #Make a game instance, and run the game.
ai=AlienInvasion()

