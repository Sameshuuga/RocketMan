import pygame,random,os
from pathlib import Path

from settings import Settings


class Astroid:
    """Class for creating and controlling astroid objects"""

    def __init__(self, game, directory):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()
        self.scale = random.uniform(0.5, 3.0)
        self.scaled = (60 * self.scale, 60 * self.scale)

        # Drawing controls
        self.filelist = os.listdir(directory)
        self.fileindex = 0
        self.astroid = pygame.image.load(Path(f'{directory}/astroid0000.png')).convert()
        self.astroid = pygame.transform.scale(self.astroid, self.scaled).convert()
        self.astroid.set_colorkey('black')
        self.rect = self.astroid.get_rect()
        self.rect.bottom = self.screen_rect.top
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.y = self.rect.y
        
    def blitastroid (self):
        self.screen.blit (self.astroid, self.rect)

    def move (self, game): #slow down image frame rate
        if game.tick % self.settings.astroid_drawrate == 0:
            self.astroid = pygame.image.load(Path(f'images/astroid/{self.filelist[self.fileindex]}')).convert()
            self.astroid = pygame.transform.scale(self.astroid, self.scaled).convert()
            self.astroid.set_colorkey('black')
            self.fileindex += 1
            if self.fileindex == len(self.filelist):
                self.fileindex = 0
        self.y += self.settings.astroid_speed
        self.rect.y = self.y
        self.blitastroid()