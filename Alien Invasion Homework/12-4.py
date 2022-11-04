import pygame
import sys


class Game:
    def __init__(self):
        pygame.self()

class Picture():
    def __init__(self, screen, image_address):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image_address)
        self.rect = self.image.get_rect()

    def draw(self):
        self.rect.center = self.screen_rect.center
        self.screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((230, 230, 230))

class Ship:
    """ Ship."""

    def __init__(self, slivin):
        self.screen = slivin.screen
        self.settings = slivin.settings
        self.screen_rect = slivin.screen.get_rect()

        self.image = pygame.image.load('/Alien Invasion Homework/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def update(self):

        #right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        #left
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #up
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        #down
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from position attributes.
        self.rect.x = self.x
        self.rect.y = self.y

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((230, 230, 230))

ship = Picture(screen, "ship.bmp")
ship.draw()

pygame.display.flip()
