import pygame
from constants import *
from scenes.level1 import Level1

# Initialisation de pygame et de différentes variables
pygame.init()
pygame.display.set_caption("Shoot clash")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()  # Horloge du jeu (limite les fps)
current_scene = Level1(screen)
running = True

# Boucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limite à 60 fps et retourne le temps entre deux frames
    elapsed = clock.tick(MAX_FPS)

    if current_scene.is_finished == True:
        current_scene = current_scene.next_scene

    current_scene.update(elapsed)
    current_scene.draw()

    pygame.display.update()
  