import random
import pygame
import sys

from Constants import *
from pygame.time import Clock
from HeroClass import *
from EnemyClass import *
from PowerClass import PowerClass
from SpriteBase import *

# Inicializar Pygame, Inicializar Window y Clock
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(WINDOW_TITLE)

# Variables constantes
GLOBAL_HEALTH = 3
GLOBAL_SCORE = 0

# Cargar background
background_image_raw = pygame.image.load(BACKGROUND_PATH)
background_image = pygame.transform.scale(background_image_raw, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Cargar sonidos
fire_sound = pygame.mixer.Sound(FIRE_SOUND_PATH)
hit_sound = pygame.mixer.Sound(DAMAGE_SOUND_PATH)

# Inicializar sprites
all_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
fire_sprite = pygame.sprite.Group()
power_sprite = pygame.sprite.Group()


# Spawneamos Heroe desde el inicio del juego
# (El enemy, el fire y el powerup se inicializan en sus respectivos metodos)
hero = HeroClass(PLAYER_IMAGE_PATH, fire_sound)

# Agregamos inicialmente a hero a los grupos de sprites
all_sprites.add(hero)
player_sprite.add(hero)

# Spawn de Enemy
def spawnRandomEnemy():
    enemy = EnemyClass(random.choice(ENEMY_IMAGES_PATH))
    
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)
    
# Spawn de Powerup
def spawnPower():
    power = PowerClass(POWER_IMAGE_PATH)
    
    all_sprites.add(power)
    power_sprite.add(power)
    
# Disparo de hero
def heroShoot():
    new_fire = hero.shoot()
    if new_fire:
        all_sprites.add(new_fire)
        fire_sprite.add(new_fire)

def enemyHurtPlayer():
    global GLOBAL_HEALTH
    GLOBAL_HEALTH -= 1
    hit_sound.play()
    
        
# Configurar el temporizador para que el trigger del evento
pygame.time.set_timer(SPAWN_ENEMY_EVENT, 500)
pygame.time.set_timer(SPAWN_POWER_EVENT, 2000)

# --- Bucle Principal del Juego ---
playGame = True
# clock = pygame.time.Clock() # Para controlar los FPS

while playGame:
    # --- Manejo de Eventos (pygame.event) ---
    for event in pygame.event.get():
        # Evento: Cerrar juego
        if event.type == pygame.QUIT:
            playGame = False # Sale del bucle principal
        
        # Evento: Spawn de enemigo
        if event.type == SPAWN_ENEMY_EVENT:
            spawnRandomEnemy()
            
        # Evento: Spawn de powerup
        if event.type == SPAWN_POWER_EVENT:
            spawnPower()
            
        # Evento: Interacciones de jugador
        if event.type == pygame.KEYDOWN:
            
            # Disparo de jugador
            if event.key == pygame.K_SPACE:
                heroShoot()
                
        # Evento: Enemigo golpea a jugador
        if event.type == HIT_ENEMY_EVENT:
            enemyHurtPlayer()
            
    
                    

    # Logica de juego y actualizacion
    
    # Carga el update al mismo tiempo de todos los sprites del grupo all_sprites 
    all_sprites.update()

    # --- Dibujado (pygame.display) ---
    window.blit(background_image, (0, 0))
    
    # Dibujar los sprites
    all_sprites.draw(window)
    
    # Actualizar la pantalla
    pygame.display.update()
    
    # Controlar FPS
    clock.tick(FPS)

    if GLOBAL_HEALTH <= 0:
        print("GAME OVER")
        playGame = False

# Salir
pygame.quit()
sys.exit()