class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed = 1.5

    def __init__(self):
        "--snip--"
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = float('inf')

    def __init__(self):
        "--snip--"
        # Alien settings
        self.alien_speed = 1.0

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
"--snip--"

    self __init__(self):
        "--snip--"
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
 
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        self.ship = Ship(self)

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships_left.
        self.stats.ships_left -= 1
 
        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()
 
        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Pause.
        sleep(0.5)

        def _update_aliens(self):
            "--snip--"
            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                self._ship_hit()

        def center_ship(self):
            """Center the ship on the screen."""
            self.rect.midbottom = self.screen_rect.midbottom
            self.x = float(self.rect.x)

        def _check_aliens_bottom(self):
            """Check if any aliens have reached the bottom of the screen."""
            for alien in self.aliens.sprites():

                if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                    self._ship_hit()
                break

        def _update_aliens(self):
            "--snip--"
            # Look for alien-ship collisions.
            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                self._ship_hit()
 
            # Look for aliens hitting the bottom of the screen.
            self._check_aliens_bottom()

        def __init__(self):
            "--snip--"
            # Start Alien Invasion in an active state.
            self.game_active = True

        def _ship_hit(self):
            """Respond to ship being hit by alien."""
            if self.stats.ships_left > 0:
                # Decrement ships_left.
                self.stats.ships_left -= 1
                "--snip--"
                # Pause.
                sleep(0.5)
            else:
                self.game_active = False

        def run_game(self):
            """Start the main loop for the game."""
            while True:
                self._check_events()
 
                if self.game_active:
                    self.ship.update()
                    self._update_bullets()
                    self._update_aliens()
                    
                self._update_screen()
                self.clock.tick(60)
    
        def __init__(self):
            "--snip--"
            # Bullet settings
            self.bullet_speed = 2.0
            self.bullet_width = 3
            self.bullet_height = 15
            self.bullet_color = (60, 60, 60)

            # Alien settings
            self.alien_speed = 1.0
            self.fleet_drop_speed = 10
            # fleet_direction of 1 represents right; -1 represents left.
            self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        "--snip--"

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

class Settings:
    """A class to store all settings for Alien Invasion."""
 
    def __init__(self):
        "--snip--"
        # Ship settings
        self.ship_speed = 1.5