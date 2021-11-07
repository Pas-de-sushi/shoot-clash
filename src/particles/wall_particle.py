import pygame

from model.particle import Particle
from utils.vector import Vector


class Wall(Particle):
    """
    Représente un particule de sang.

    Paramètres:
        world: le monde dans lequel se déroule la simulation
        x: la position en x de la particule
        y: la position en y de la particule
        velocity: la vitesse de la particule
        lifetime: le temps de vie de la particule
        groups: les groupes dans lesquels la particule doit apparaître

    Modifie la vitesse de la particule de manière aléatoire.
    """

    def __init__(self, world, x, y, velocity: Vector, lifetime, groups) -> None:
        # Création de l'image de la particule
        self.image = pygame.Surface([2, 2])
        self.image.fill((255, 255, 255))

        super().__init__(world, x, y, 1, velocity, lifetime, groups)

        # Modification de la vitesse de la particule aléatoirement
        self.randomize_direction()
