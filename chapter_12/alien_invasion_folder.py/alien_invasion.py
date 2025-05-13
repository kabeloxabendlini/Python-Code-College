import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
 
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
 
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        def run_game(self):
            """Start the main loop for the game."""
            while True:
                # Watch for keyboard and mouse events.
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                # Make the most recently drawn screen visible.
                pygame.display.flip()
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

    def __init__(self):
        """Initialize the game, and create game resources."""
        
        self.clock = pygame.time.Clock()
        "--snip--"

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            "--snip--"
            pygame.display.flip()
            self.clock.tick(60)

            def __init__(self):
                "--snip--"
                pygame.display.set_caption("Alien Invasion")
                
                # Set the background color.
                self.bg_color = (230, 230, 230)
    def run_game(self):
        "--snip--"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)

         # Make the most recently drawn screen visible.
        pygame.display.flip()
        self.clock.tick(60)

class Settings:
        """A class to store all settings for Alien Invasion."""
        
        def __init__(self):
            """Initialize the game's settings."""
            # Screen settings
            self.screen_width = 1200
            self.screen_height = 800
            self.bg_color = (230, 230, 230)

"--snip--"
import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
 
        "--snip--"
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
 
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        self.clock.tick(60)
"--snip--"

import pygame

class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
 
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

"--snip--"
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        "--snip--"
        pygame.display.set_caption("Alien Invasion")
 
        self.ship = Ship(self)
 
    def run_game(self):
            "--snip--"
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
 
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

    "--snip--"
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
 
            # Redraw the screen during each pass through the loop.
    "--snip--"
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        "--snip--"

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.rect.x += 1

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        "--snip--"
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
 
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
 
    def blitme(self):
        "--snip--"

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            "--snip--"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def __init__(self, ai_game):
        "--snip--"
        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.x += 1
        if self.moving_down:
            self.rect.x -= 1

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            "--snip--"
            elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        "--snip--"
 
        # Ship settings
        self.ship_speed = 1.5

class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        "--snip--"

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
 
        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
 
        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
 
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right:
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed

        if self.moving_up:
            self.x -= self.settings.ship_speed
         
        if self.moving_down:
            self.x -= self.settings.ship_speed
 
        # Update rect object from self.x.
        self.rect.x = self.x
 
    def blitme(self):
        "--snip--"

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.x -= self.settings.ship_speed
 
        # Update rect object from self.x.
        self.rect.x = self.x

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
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
 
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _check_keydown_events(self, event):
        "--snip--"
        if event.key == pygame.K_LEFT:

            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion.")
