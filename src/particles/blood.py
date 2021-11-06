import pygame

from model.particle import Particle
from utils.vector import Vector


class Blood(Particle):
    """
    Représente un particule de sang.

    Paramètres:
        world: le monde dans lequel se déroule la simulation
        x: la position en x de la particule
        y: la position en y de la particule
        velocity: la vitesse de la particule
        groups: les groupes dans lesquels la particule doit apparaître

    Modifie la vitesse de la particule de manière aléatoire.
    """

    def __init__(self, world, x, y, velocity: Vector, groups) -> None:
        # Création de l'image de la particule
        self.image = pygame.Surface([5, 5])
        self.image.fill((200, 0, 0))

        super().__init__(world, x, y, 1, velocity, -1, groups)

        # Modification de la vitesse de la particule aléatoirement
        self.randomize_direction()
