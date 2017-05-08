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
        self.player_speed_factor = 1.5
        #Ball settings
        self.ball_speed_factor = 0.5
        #Scoring
        #Add scoring increment
