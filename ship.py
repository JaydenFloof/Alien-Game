#Ship module

import pygame

import settings


class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        
        if self.moving_up:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down:
            self.rect.y += self.settings.ship_speed

        if self.moving_left:
            self.rect.x -= self.settings.ship_speed
        if self.moving_right:
            self.rect.x += self.settings.ship_speed

        if self.moving_up and self.rect.top <= self.screen_rect.top:
            self.moving_up = False
            self.rect.y += self.settings.ship_speed

        if self.moving_down and self.rect.bottom >= self.screen_rect.bottom:
            self.moving_down = False
            self.rect.y -= self.settings.ship_speed

        if self.moving_left and self.rect.left <= self.screen_rect.left:
            self.moving_left = False
            self.rect.x += self.settings.ship_speed

        if self.moving_right and self.rect.right >= self.screen_rect.right:
            self.moving_right = False
            self.rect.x -= self.settings.ship_speed
