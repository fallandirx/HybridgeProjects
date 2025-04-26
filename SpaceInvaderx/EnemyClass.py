import pygame
import random

from CharacterBase import CharacterBase
from Constants import *

class EnemyClass(CharacterBase):
    
    # Atributos de clase que compartiran todos los objetos Enemy
    BASE_SPEED = 5
    BASE_HEALTH = 1
    
    def __init__(self, image_path):
        super().__init__(image_path, self.BASE_SPEED, self.BASE_HEALTH)

        initial_x = random.randrange(CHARACTER_SIZE,(WINDOW_WIDTH-CHARACTER_SIZE))
        initial_y = 0
        
        self.rect.x = initial_x
        self.rect.y = initial_y
        
        
    def update(self):
        self.rect.y += self.speed
        
        if self.rect.top > WINDOW_HEIGHT:
            print("Enemigo muerto")
            self.kill()
        
        