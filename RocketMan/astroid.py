import pygame,random
from pathlib import Path

from settings import Settings


class Astroid:
    """Class for creating and controlling astroid objects"""

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()

        # Drawing controls
        self.astroid = pygame.image.load(Path('images/astroid/0001.png')).convert()
        self.rect = self.astroid.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.y = self.rect.y
        
    def blitastroid (self):
        self.screen.blit (self.astroid, self.rect)

    def move (self):
        self.y += self.settings.astroid_speed
        self.rect.y = self.y
        self.blitastroid()