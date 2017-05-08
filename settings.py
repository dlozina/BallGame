class Settings():
    """a class to store all settings for Ball game"""
    
    def __init__(self):
        """Initialise the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 210, 50) #Green
        #Player limit
        self.player_limit = 3
        
        #Link to self variables from method in class
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Init settings that change troughout the game."""
        #Plyer settings
        self.player_speed_factor = 1.2
        #Ball settings
        self.ball_speed_factor = 0.7
        #Scoring
        #Add scoring increment
        
        #New level and new speed
        self.speedup_scale_player = 1.1
        self.speedup_scale_ball = 1.1
    
    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.player_speed_factor *= self.speedup_scale_player
        self.ball_speed_factor *= self.speedup_scale_ball
        
