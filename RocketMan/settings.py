import random
class Settings:
    """manages settings of RocketMan"""

    def __init__(self):
        #screen controls
        self.screen_width = 1440
        self.screen_hight = 900
        self.bgcolor = 'black' 
        
        
        # Rocket controls
        self.rocket_speed = 4
        self.rocket_drawrate = 10
        
        # Astroid controls
        #scale contoled in class
        self.astroid_speed = random.uniform(1.0, 10)
        self.spawn_rate = 50 #lower = higher spawn rate
        self.astroid_drawrate = 4 #higher = slower frame rate

        # Menu settings
        self.margin = 0
