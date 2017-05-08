import pygame.font
from pygame.sprite import Group

from player import Player

class Scoreboard():
    """Class to report scoring information"""
    def __init__(self, bg_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_settings = bg_settings
        self.stats = stats
        
        #Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)
        
        #Call score display function
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_players()
         
    def prep_score(self):
        """Turn score to rendered image"""
        score_dis = "Score: " + str(self.stats.score)
        self.score_image = self.font.render(score_dis, True, 
        self.text_color, self.bg_settings.bg_color)
        
        #Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Turn the high score into rendered image"""
        high_score_dis = "All time record: " + str(self.stats.high_score) 
        self.high_score_image = self.font.render(high_score_dis, True, 
            self.text_color, self.bg_settings.bg_color)
        
        #Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20 #self.screen_rect.top
    
    def prep_level(self):
        """Turn the level into rendered image."""
        level_display = "Level " + str(self.stats.level)
        self.level_image = self.font.render(level_display, True, 
            self.text_color, self.bg_settings.bg_color)
        
        #Position level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_players(self):
        """Show how many ships are left"""
        self.players = Group()
        for player_number in range(self.stats.player_left):
            player = Player(self.bg_settings, self.screen)
            player.rect.x = 10 + player_number * player.rect.width
            player.rect.y = 10
            self.players.add(player)
                
    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #Draw players
        self.players.draw(self.screen)
        
