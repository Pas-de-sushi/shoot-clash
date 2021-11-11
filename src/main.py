import pygame

from constants import *
# Initialisation de pygame et de différentes variables
from scene_manager import SceneManager

pygame.init()
pygame.display.set_caption("Shoot clash")

pygame.mixer.init()  # Initialise le son
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()  # Horloge du jeu (limite les fps)
running = True
pygame.mixer.music.load("assets/sounds/music/music_pirate.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

scene_manager = SceneManager(screen)

# Boucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limite à 60 fps et retourne le temps entre deux frames
    elapsed = clock.tick(MAX_FPS)


    scene_manager.update(elapsed)
    scene_manager.draw()

    pygame.display.update()
