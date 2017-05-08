import pygame

class Player():
    def __init__(self, bg_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.bg_settings = bg_settings
        
        #Load the player image and get its rect.
        self.image = pygame.image.load('images/hajduk_game_g.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start each new player at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Not in real bg
        #self.rect.centery = self.screen_rect.centery
        #Store decimal value for the ship's speed
        #Real bg
        self.center = float(self.rect.centerx)
        #Not in real bg
        #self.centerx = float(self.rect.centerx)
        #self.centery = float(self.rect.centery)
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        #Not in real bg
        #self.moving_up = False
        #self.moving_down = False
        
    def update(self):
        """Update the player's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.center += self.bg_settings.player_speed_factor
            self.center += self.bg_settings.player_speed_factor
        if self.moving_left and self.rect.left > 0:
            #self.center -= self.bg_settings.player_speed_factor
            self.center -= self.bg_settings.player_speed_factor
        #Not in real bg
        #if self.moving_up and self.rect.top > 0:
        #    self.centery -= self.bg_settings.player_speed_factor
        #if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #    self.centery += self.bg_settings.player_speed_factor
        #Update rect object from self.center
        #Real bg
        self.rect.centerx = self.center
        #Not in real bg
        #self.rect.centerx = self.centerx
        #self.rect.centery = self.centery
        
    def center_player(self):
        """center the player on the screen"""
        self.center = self.screen_rect.centerx
        
    def blitme(self):
        """Draw the player at the current location."""
        self.screen.blit(self.image, self.rect)
