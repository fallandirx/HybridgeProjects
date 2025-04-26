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

    @property
    def speed(self):
        return self._speed # Cambiamos a un getter, ya que estamos utilizando un guion bajo

    @speed.setter
    def speed(self, value): # PErsonalizamos el setter
        if value < 0:
            print("No se puede utilizar una velocidad negativa. Estableciendo en 0")
            value = 0
        else:
            self._speed = float(value)
        
    @property
    def character_health(self):
        return self._character_health

    @character_health.setter
    def character_health(self, value): # PErsonalizamos el setter
        if value < 0:
            print("No se puede utilizar una vida negativa. Estableciendo en 0")
            value = 0
        else:
            self._character_health = int(value)
        