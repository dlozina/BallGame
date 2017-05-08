class Settings():
    """a class to store all settings for Ball game"""
    
    def __init__(self):
        """Initialise the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_color = (230, 230, 230) #Gray 
        self.bg_color = (50, 210, 50) #Green
        #Plyer settings
        self.player_speed_factor = 1.5
        self.player_limit = 3
        #Ball settings
        self.ball_speed_factor = 0.5
