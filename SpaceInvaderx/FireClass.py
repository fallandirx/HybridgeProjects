import pygame
from Constants import WINDOW_HEIGHT
from SpriteBase import SpriteBase

class FireClass(SpriteBase):
    BASE_SPEED = 10
    BASE_HEALTH = 1
    
    def __init__(self, image_path, initial_x, initial_y):
        super().__init__(image_path, self.BASE_SPEED, self.BASE_HEALTH)
        
        # En este caso si vamos a establecer una posicion en x o y, ya que dependera
        # de la posicion del jugador jiji
        self.rect.x = initial_x
        self.rect.y = initial_y
        
    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.bottom < 0:
            self.kill()