class Settings:
    """manages settings of RocketMan"""

    def __init__(self):
        self.screen_width = 1440
        self.screen_hight = 900
        self.bgcolor = 'black' 
        
        # Speed controls
        self.rocket_speed = 4
        self.astroid_speed = 1.5
        self.spawn_rate = 100
        
        # Controls surface size
        self.scale = 1.0

        # Menu settings
        self.margin = 0
