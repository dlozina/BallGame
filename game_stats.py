class GameStats():
    """Track statistics for Ball game"""
    
    def __init__(self, bg_settings):
        """Initialize statistics"""
        self.bg_settings = bg_settings
        self.reset_stats()
        #Start Alien invasion in an active state
        self.game_active = False
        #High score should never be reset
        #Load high score from file
        filename = 'highscore.txt'
        with open(filename) as file_object:
            self.high_score = int(file_object.read())
            
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.player_left = self.bg_settings.player_limit
        self.score = 0
        self.level_up = 0
        self.level = 1
