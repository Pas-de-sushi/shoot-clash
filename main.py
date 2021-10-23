import pygame

from block import Block
from constants import *
from sprites import Player
from world import World

pygame.init()

screen = pygame.display.set_mode((1080, 720))

# Initialisation de l'horloge du jeu (limite les fps)
clock = pygame.time.Clock()
running = True
world = World(screen)
while running:
    # Limite à 60 fps et retourne le temps entre deux frames
    elapsed = (clock.tick(MAX_FPS))
    events_queue = pygame.event.get()
    for event in events_queue:
        if event.type == pygame.QUIT:
            running = False



    world.draw()

    pygame.display.flip()
