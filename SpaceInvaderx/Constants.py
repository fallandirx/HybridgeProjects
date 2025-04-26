# Configuración de la ventana 
import pygame

# Variables del juego
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Evil Invaders"
FPS = 60

# Tamaño de los personajes 
CHARACTER_SIZE = 50 # Tamaño fijo para CharacterBase y sus hijos
FIRE_SIZE = 50

# Rutas de Imágenes 
PLAYER_IMAGE_PATH = 'images/hero.gif'
ENEMY_IMAGES_PATH = ['images/evil1.gif', 'images/evil2.gif', 'images/evil3.gif'] # Lista de imágenes de enemigos
FIRE_IMAGE_PATH = 'images/fire1.jpg'
POWER_IMAGE_PATH = 'images/power1.jpg'
BACKGROUND_PATH = 'images/background.jpg'

# Rutas de sonidos
POWER_SOUND_PATH = 'sounds/powerup.wav'
DAMAGE_SOUND_PATH = 'sounds/hurt.wav'
FIRE_SOUND_PATH = 'sounds/fire.wav'

# Colores 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Eventos
SPAWN_ENEMY_EVENT = pygame.USEREVENT + 1
SPAWN_POWER_EVENT = pygame.USEREVENT + 2

HIT_ENEMY_EVENT = pygame.USEREVENT + 3