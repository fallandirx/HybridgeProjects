# Configuración de la ventana 
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Evil Invaders"
FPS = 60

# Tamaño de los personajes 
CHARACTER_SIZE = 50 # Tamaño fijo para CharacterBase y sus hijos

# Daño de los personajes
CHARACTER_DAMAGE = 1

# Rutas de Imágenes 
PLAYER_IMAGE_PATH = 'images/hero.gif'
ENEMY_IMAGES_PATH = ['images/evil1.gif', 'images/evil2.gif', 'images/evil3.gif'] # Lista de imágenes de enemigos

# Colores 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Eventos
SPAWN_ENEMY_EVENT = pygame.USEREVENT + 1