class GameStats():
    """Track statistics for Ball game"""
    
    def __init__(self, bg_settings):
        """Initialize statistics"""
        self.bg_settings = bg_settings
        self.reset_stats()
        #Start Alien invasion in an active state
        self.game_active = True
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.player_left = self.bg_settings.player_limit
