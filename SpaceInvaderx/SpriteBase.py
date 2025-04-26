import pygame
from Constants import CHARACTER_SIZE

class SpriteBase(pygame.sprite.Sprite):
    
    def __init__(self, image_path, speed, character_health):
        super().__init__() # Inicializa el ctor de Sprite

    # Carga y conversion de imagenes
        # Convierte la imagen de manera optima
        generic_original_img = pygame.image.load(image_path).convert_alpha()
        # Dimensionar la imagen a nuestro gusto
        self.image = pygame.transform.scale(
            generic_original_img,
            (CHARACTER_SIZE, CHARACTER_SIZE))
        
        # Establecer velocidad estandard
        self.speed = speed
        
        # Establecer vida del character
        self.character_health = character_health
            
        # Crear el rectangulo, la posicion la pone el hijo
        self.rect = self.image.get_rect()
        
    # Movimiento automatico del character
    def update(self):
        pass
        
        
        