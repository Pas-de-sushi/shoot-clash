import pygame

from model.particle import Particle
from utils.vector import Vector


class Cartridge(Particle):
    """
    Représente un particule de la cartouche.

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
        self.image = pygame.Surface([4, 3])
        self.image.fill((250, 250, 0))

        super().__init__(world, x, y, 1, velocity, lifetime, groups)

        self.velocity.y = -6

        def handle_collision(self, old_rect):
            self.rect = check_collision(
                self.world.map_group,
                old_rect,
                self.rect,
                self.right,
                self.left,
                self.top,
                self.bottom
            )

    def right(self, block):
        self.velocity.x *= -1
        self.velocity *= block.friction

    def left(self, block):
        self.velocity.x *= -1
        self.velocity *= block.friction

    def top(self, block):
        self.velocity.y = 0

    def bottom(self, block):
        self.velocity.y *= -0.95
        self.velocity *= block.friction