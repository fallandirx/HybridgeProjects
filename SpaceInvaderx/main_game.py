import random
import pygame
import sys
from Constants import *
from pygame.time import Clock
from HeroClass import *
from EnemyClass import *
from CharacterBase import *

# Inicializar Pygame, Inicializar Window y Clock
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(WINDOW_TITLE)

# Inicializar sprites
all_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

# Inicializar Heroe
hero = HeroClass(PLAYER_IMAGE_PATH, )

# Agregamos hero a los grupos de sprites
all_sprites.add(hero)
player_sprite.add(hero)

# Spawn de Enemy
def spawnRandomEnemy():
    enemy = EnemyClass(random.choice(ENEMY_IMAGES_PATH))
    
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)
    
    
# Spawn de Hero
def spawnHero():
    hero = HeroClass(PLAYER_IMAGE_PATH)


# Configurar el temporizador para que el trigger del evento
pygame.time.set_timer(SPAWN_ENEMY_EVENT, 1000)

# Variable de control (?)
draw_enemy_this_frame = False


# --- Bucle Principal del Juego ---
ejecutarJuego = True
# clock = pygame.time.Clock() # Para controlar los FPS

while ejecutarJuego:
    # --- Manejo de Eventos (pygame.event) ---
    for event in pygame.event.get():
        # Si el evento es cerrar la ventana
        if event.type == pygame.QUIT:
            ejecutarJuego = False # Sale del bucle principal
        if event.type == SPAWN_ENEMY_EVENT:
            spawnRandomEnemy()

    # Logica del juego y actualizacion
    all_sprites.update()

    keyPressed = pygame.key.get_pressed()
    
    # if (keyPressed[pygame.K_LEFT]):
    #     playerX -= N_PIXELS_TO_MOVE
    # if (keyPressed[pygame.K_RIGHT]):
    #     playerX += N_PIXELS_TO_MOVE
    # # if (keyPressed[pygame.K_DOWN]):
    # #     playerY += N_PIXELS_TO_MOVE
    # # if (keyPressed[pygame.K_UP]):
    # #     playerY -= N_PIXELS_TO_MOVE
    #     
    # hero_image_rect = pygame.Rect(playerX, playerY, CHARACTER_HEIGHT_WIDTH, CHARACTER_HEIGHT_WIDTH)
        

    # --- Dibujado (pygame.display) ---
    window.fill(BLACK)
    
    # Dibujar los sprites
    all_sprites.draw(window)
    
    # Actualizar la pantalla
    pygame.display.update()
    
    # Controlar FPS
    clock.tick(FPS)

    # Dibujar todos los sprites en la pantalla
    # grupo_todos_los_sprites.draw(pantalla)

    # --- Actualizar la Pantalla ---
    # pygame.display.flip() o pygame.display.update()
    # flip() actualiza toda la pantalla, update() solo actualiza las partes que han cambiado (puede ser más eficiente)
    # pygame.display.flip()

    # --- Control de FPS (Frames por Segundo) ---
    # clock.tick(60) # Limita el bucle a 60 FPS (o los que necesites)

# --- Salir de Pygame ---
# Después de que el bucle principal termine
pygame.quit()
sys.exit()