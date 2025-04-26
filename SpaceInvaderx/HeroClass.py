from CharacterBase import CharacterBase
from Constants import *


class HeroClass(CharacterBase):

    # Atributos de clase que compartiran todos los objetos Hero
    BASE_SPEED = 7
    BASE_HEALTH = 5
    
    def __init__(self, image_path):
        super().__init__(image_path, self.BASE_SPEED, self.BASE_HEALTH)
        
        initial_x = (WINDOW_WIDTH * 0.475)
        initial_y = (WINDOW_HEIGHT - (CHARACTER_SIZE * 1.5))
        
        self.rect.x = initial_x
        self.rect.y = initial_y

    def update(self):
        pass