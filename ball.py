import pygame
import random

class Ball():
    """A class to represent a single ball"""
    
    def __init__(self, bg_settings, screen):
        """Initialize the ball and set its random starting position."""
        self.screen = screen
        self.bg_settings = bg_settings
        
        #Load the ball image and set its rect attribute.
        self.image = pygame.image.load('images/ball_g.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new ball at random x-position.
        self.rect.x = random.randint(self.rect.width, 
            (bg_settings.screen_width - self.rect.width))
        self.rect.y = self.rect.height
        
        #Store the ball's exact position.
        self.x = float (self.rect.x)
        self.y = float(self.rect.y)
    
    def end_of_screen(self):
        """
        Detect end of screen (y - corinate) and
        return Ball to new random position.
        """
        screen_rect = self.screen.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.bottom >= screen_rect.bottom:
           self.x = random.randint(self.rect.width, 
            (self.bg_settings.screen_width - self.rect.width))
           self.y = self.rect.height
           return True
            
    def update(self):
        """Move ball down."""
        self.y += self.bg_settings.ball_speed_factor
           
                        
    def blitme(self):
        """Draw the ball at its currect location."""
        self.screen.blit(self.image, self.rect)
