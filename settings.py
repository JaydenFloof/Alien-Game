#Settings module

import pygame


class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 750
        self.background_colour = (65, 165, 200)

        self.ship_speed = 0.55

        self.alien_speed = 0.3
        self.fleet_drop_speed = 1
        self.fleet_direction = 1

        self.bullet_speed = 0.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (60, 60, 60)

        
        
