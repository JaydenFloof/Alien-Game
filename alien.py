#Alien module

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = 600
        self.rect.y = 25

        self.x = float(self.rect.x)
        
    def update(self):
        self.x -= (self.settings.alien_speed)
        self.rect.x = self.x

    
