import pygame

from constants import *
from world import World

# Initialisation de pygame et de différentes variables
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()  # Horloge du jeu (limite les fps)
world = World(screen)  # Initialisation du "monde" du jeu

# Boucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Limite à 60 fps et retourne le temps entre deux frames
    elapsed = clock.tick(MAX_FPS)
    
    world.update(elapsed)
    world.draw()

    pygame.display.update()
