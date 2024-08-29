#Jayden Vuong
#Aliens Assignment 10

import pygame, sys, time
from random import randint
from pygame.sprite import Sprite
from settings import Settings
from ship import Ship
from rain import Rain
from alien import Alien
from bullet import Bullet
        
class Aliens_game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Aliens Game')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
        self.fleet = pygame.sprite.Group()
        self.create_fleet()

        
    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_fleet()
            self.update_screen()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_q:
                    sys.exit()
                    pygame.exit()
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_fleet(self):
        self.fleet.update()

    def create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        for e in range(8):
            alien_number = randint(7, 9)
            row_number = randint(0, 6)
            self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width * alien_number * 1.5
        alien.y = alien_width * alien_number
        alien.rect.x = alien.x 
        alien.rect.y = alien_height * row_number
        self.fleet.add(alien)

    def update_bullets(self):
        length = len(self.fleet)
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= 1050:
                self.bullets.remove(bullet)
                
        collisions = pygame.sprite.groupcollide(self.bullets, self.fleet, True, True)


        for alien in self.fleet.copy():
            if alien.rect.right <= 0:
                self.fleet.remove(alien)
            if len(self.fleet) < length:
                alien_number = randint(7, 9)
                row_number = randint(0, 6)
                self.create_alien(alien_number, row_number)
            if alien.rect.x == self.ship.rect.x:
                for x in range(0, 75):
                    if(alien.rect.y == self.ship.rect.y - x) or (alien.rect.y == self.ship.rect.y + x):
                        sys.exit()
                        pygame.exit()

    def update_screen(self):
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.fleet.draw(self.screen)
            
        pygame.display.flip()


        
game = Aliens_game()
game.run_game()
