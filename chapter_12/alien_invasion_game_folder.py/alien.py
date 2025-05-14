import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
 
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
 
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
 
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
 
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
       
        def _create_alien(self, x_position, y_position):
            """Create an alien and place it in the fleet."""
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

        def __init__(self, ai_game):
            """Initialize the alien and set its starting position."""
            super().__init__()
            self.screen = ai_game.screen
            self.settings = ai_game.settings
            "--snip--"
        
        def update(self):
            """Move the alien to the right."""
            self.x += self.settings.alien_speed
            self.rect.x = self.x

            while True:
                self._check_events()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()
                self.clock.tick(60)

        def check_edges(self):
            """Return True if alien is at edge of screen."""
            screen_rect = self.screen.get_rect()
            return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
 
        def update(self):
            """Move the alien right or left."""
            self.x += self.settings.alien_speed * self.settings.fleet_direction
            self.rect.x = self.x

class GameStats:
    """Track statistics for Alien Invasion."""
 
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
 
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.set
