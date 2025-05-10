import sys, pygame, random

from rocket import Rocket
from settings import Settings
from astroid import Astroid
from menu import Menu

class RocketMan:
    """Main class for RocketMan. Creats and manages the game."""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption('RocketMan')

        self.state = 0
       

    def run (self):
        while True:
            #title loop
            while self.state == 0:
                self.title = Menu(self)
                self.title_length = len(self.title.menu)
                while self.state == 0:
                    self._events()
                    self.title.blitmenu()
                    self._tick()
                del self.title
            #game loop
            while self.state == 1:
                self.rocket = Rocket(self)
                self.astroidlist = [Astroid(self)]
                while self.state == 1:
                    self._events()
                    self._update()
                    self._tick()
                del self.rocket, self.astroidlist
            if self.state == self.title_length:
                sys.exit()
           

    def _events (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._KEYDOWN(event)
            elif event.type == pygame.KEYUP:
                self._KEYUP(event)

    def _KEYDOWN(self, event):
        if self.state == 0:
            if event.key == pygame.K_s:
                self.title.menu_select(1)
            if event.key == pygame.K_w:
                self.title.menu_select(-1)
            if event.key == pygame.K_SPACE:
                self.title.menu_select(game = self,key = event.key)

        if self.state == 1:
            if event.key == pygame.K_a:
                self.rocket.movingleft = True
            if event.key == pygame.K_s:
                self.rocket.movingdown = True
            if event.key == pygame.K_d:
                self.rocket.movingright = True
            if event.key == pygame.K_w:
                self.rocket.movingup = True
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    def _KEYUP(self, event):
        if self.state == 1:
            if event.key == pygame.K_a:
                self.rocket.movingleft = False
            if event.key == pygame.K_s:
                self.rocket.movingdown = False
            if event.key == pygame.K_d:
                self.rocket.movingright = False
            if event.key == pygame.K_w:
                self.rocket.movingup = False

    def _update(self):
        if self.state == 1:
            self.rocket.update()
        if random.randint(0, self.settings.spawn_rate) == 1:
            self.astroidlist.append(Astroid(self))
        for astroid in self.astroidlist:
            astroid.move()
            if pygame.Rect.colliderect(self.rocket.rect, astroid.rect): ## astroid collision flag 
                self.rocket.collide = True
            if astroid.rect.y > astroid.screen_rect.bottom:
                del astroid
        

    def _tick (self):
        pygame.display.flip()
        self.clock.tick(60)
        self.screen.fill(self.settings.bgcolor)



################################################################################################
if __name__ == '__main__':
    game = RocketMan()
    game.run()
