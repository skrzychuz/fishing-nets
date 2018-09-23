class Settings():
    """A class to store all settings for the game."""

    def __init__(self):
    
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (231, 231, 231)

        # Nets settings
        self.net_speed = 1.5
        self.net_width = 200
        self.net_height = 5
        self.net_color = 60, 60, 60
        self.net_limit = 100


        # Fish
        self.rows_drop = 25
        # 1 for right, -1 left
        self.rows_direction = 1
