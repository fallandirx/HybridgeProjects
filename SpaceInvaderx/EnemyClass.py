import pygame
import random

from SpriteBase import SpriteBase
from Constants import *

class EnemyClass(SpriteBase):
    
    # Atributos de clase que compartiran todos los objetos Enemy
    BASE_SPEED = 1.0
    BASE_HEALTH = 1
    
    def __init__(self, image_path):
        speed = random.uniform((EnemyClass.BASE_SPEED*0.5),EnemyClass.BASE_SPEED)

        super().__init__(image_path, speed, self.BASE_HEALTH)

        initial_x = random.randrange(CHARACTER_SIZE,(WINDOW_WIDTH-CHARACTER_SIZE))
        initial_y = 0

        self.rect.x = initial_x
        self.rect.y = initial_y
        
        
    def update(self):
        self.rect.y += self.speed
        

        if self.rect.top > WINDOW_HEIGHT:
            hit_event = pygame.event.Event(HIT_ENEMY_EVENT)
            
            pygame.event.post(hit_event) # Notificacion de que se cumplio el evento
            
            self.kill()
        
        