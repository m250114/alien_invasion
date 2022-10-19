import pygame
import sys

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resorces."""
        pygame.init()

        self.screen=pygame.display.set_
    def run_game(self):
        --snip--
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

    #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__== '__main__':
    #Make a game instance, and run the game.
ai=AlienInvasion()

