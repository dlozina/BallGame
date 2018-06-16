import pygame.font

class Scoreboard():
    """Class to report scoring information"""
    def __init__(self, bg_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_settings = bg_settings
        self.stats = stats
        
        #Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Call score display function
        self.prep_score()
         
    def prep_score(self):
        """Turn score to rendered image"""
        score_dis = str(self.stats.score)
        self.score_image = self.font.render(score_dis, True, 
        self.text_color, self.bg_settings.bg_color)
        
        #Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        
