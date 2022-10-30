class boxer:
    """A class to manage the ship."""

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen =screen
        self.screen_rect = screen.get_rect()

        # Load the boxer image and get its rect.
        self.image = pygame.image.load('images/boxer.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom