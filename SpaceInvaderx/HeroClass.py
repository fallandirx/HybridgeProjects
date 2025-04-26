import pygame

from FireClass import FireClass
from SpriteBase import SpriteBase
from Constants import *


class HeroClass(SpriteBase):

    # Atributos de clase que compartiran todos los objetos Hero
    BASE_SPEED = 7
    BASE_HEALTH = 5
    
    def __init__(self, image_path, fire_sound):
        super().__init__(image_path, self.BASE_SPEED, self.BASE_HEALTH)
        
        # Ubicacion inicial
        initial_x = (WINDOW_WIDTH * 0.475)
        initial_y = (WINDOW_HEIGHT - (CHARACTER_SIZE * 1.5))
        
        # Creacion del rectangulo
        self.rect.x = initial_x
        self.rect.y = initial_y
        
        self.fire_sound = fire_sound
        

    def update(self):
        keyPressed = pygame.key.get_pressed()
        keyDown = pygame.KEYDOWN
        
        if keyPressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keyPressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
            
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(WINDOW_WIDTH - self.rect.width, self.rect.x)
        
    def shoot(self):
        # Calculamos la posicion inicial de la bala con respecto a la posicion
        # del hero
        initial_fire_x = self.rect.centerx - CHARACTER_SIZE * 0.5
        initial_fire_y = self.rect.top - CHARACTER_SIZE * 0.5
        
        # Creacion del fire
        new_fire = FireClass(FIRE_IMAGE_PATH, initial_fire_x, initial_fire_y)
        
        # Creacion del sonido del fire
        global fire_sound
        
        if self.fire_sound:
            self.fire_sound.play()
        
        return new_fire