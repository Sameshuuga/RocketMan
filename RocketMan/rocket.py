from pathlib import Path
import pygame

from settings import Settings

class Rocket:
    """creates and manages the Rocket object"""

    def __init__(self, game):
        ## get screen rect
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()

        # drawing contol
        self.rocket = pygame.image.load(Path('images/Rocket.bmp')).convert()
        self.rocket.set_colorkey('white')
        self.rect = self.rocket.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movment flags
        self.movingup = False
        self.movingdown = False
        self.movingleft = False
        self.movingright = False
        self.collide = False
   

    def blitrocket (self):
        self.screen.blit(self.rocket, self.rect)
    
    def update (self):
        if self.movingup and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.movingdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.movingleft and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.movingright and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.collide:
            self.rocket = pygame.image.load(Path('images/Explosion/explosion_3.png')).convert() ## explosion on collision
            self.rect = self.rocket.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y 
        self.blitrocket()

    def getsize (self):
        # use to scale rocket size with the scale setting
        self.size = ((self.rocket.get_width() * self.settings.scale), (self.rocket.get_height() * self.settings.scale))
        self.rocket = pygame.transform.smoothscale(self.rocket, (self.size))
        self.rect = self.rocket.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)