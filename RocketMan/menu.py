from pathlib import Path
import pygame

from settings import Settings

class Menu:
    """class for managing title screen
        pass the game and images for title and buttons"""

    def __init__(self, game, title, buttonlist = None):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()

        #title drawing controls
        self.title = pygame.image.load(Path(f'images/menu/{title}')).convert()
        self.title.set_colorkey('white')
        self.title_rect = self.title.get_rect()
        self.title_rect.midtop = self.screen_rect.midtop

        #menu controls
        self.menu = [Button(self, f'images/menu/{buttonlist[0]}')]
        for image in buttonlist[1:]:
            self.menu.append(Button(self, f'images/menu/{image}', self.menu[buttonlist.index(image) - 1].image_rect))
        self.option = 0 #controls key value for selecting menu item
        self.selector = pygame.image.load(Path('images/menu/selector.png')).convert()
        self.selector_rect = self.selector.get_rect(midright = self.menu[0].image_rect.midleft)


    def blitmenu (self):
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.selector, self.selector_rect)
        for button in self.menu:
            self.screen.blit(button.image, button.image_rect)

    def menu_select (self, increment = 0, game = None, key = None):
        ## moves the selector
        if self.option >= 0 and self.option <= len(self.menu) - 1: 
            self.option += increment
            if self.option < 0:
                self.option = 0
            if self.option > len(self.menu) - 1:
                self.option = len(self.menu) - 1
            self.selector_rect.midright = self.menu[self.option].image_rect.midleft
        if key == pygame.K_SPACE:
            game.state = self.option + 1
            
class Button:
    """class for creating GUI menu items
        Pass the menu and a file path the Button's image, also pass an optional reference rect"""


    def __init__(self, menu, image, referance = None):
        self.screen_rect = menu.screen_rect

        #button drawing controls
        self.image = pygame.image.load(Path(image)).convert()
        self.image.set_colorkey('white')
        self.image_rect = self.image.get_rect()
        if referance == None:
            self.image_rect.center = self.screen_rect.center
        else:
            self.image_rect.midtop = referance.midbottom
            self.image_rect.y += menu.settings.margin

            



