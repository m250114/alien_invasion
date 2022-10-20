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
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    sys.exit()
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__== '__main__':
    #make a game instance, and run the game.
    ai= AlienInvasion()
    ai.run_game()

    #Set Background Music
    self.bg_color=(230,230,230)

    #redraw the screen during each pass through the loop.
    self.screen.fill(self.bg_color)

from settings import Settings
    self.settings=Settings()

    self.screen.fill(self.settings.bg_color)

from ship import Ship

self.ship= Ship(self)
self.ship.blitme()




