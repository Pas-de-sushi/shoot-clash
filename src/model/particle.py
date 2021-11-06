import random

import pygame
from model.dynamic_object import DynamicObject
from utils.vector import Vector


class Particle(DynamicObject):
    """
    Classe représentant une particule qui se fixe sur le terrain.

    Paramètres:
        world: le monde dans lequel la particule est créée
        x, y: coordonnées de la particule
        mass: la masse de la particule
        velocity: la vitesse de la particule
        lifetime: le temps de vie de la particule (en ms / -1 pour infini)
        groups: les groupes dans lesquels la particule est ajoutée

    """

    def __init__(
            self, world, x: int, y: int, mass, velocity: Vector, lifetime, groups: tuple
    ) -> None:
        """
        Constructeur de la classe Particle.

        Important: il faut déclarer self.image avant de faire appel à super().__init__()
        dans les classes filles.

        Exemple:
            self.image = pygame.Surface([5, 5])
            self.image.fill((200, 0, 0))
        """
        super().__init__(world, x, y, mass, groups)

        self.velocity = Vector(velocity.x, velocity.y)
        self.mass = 1
        self.lifetime = lifetime

    def randomize_direction(self, delta: int = 10) -> None:
        """
        Permet de modifier la vitesse y de la particule de manière aléatoire.

        Paramètres:
            delta: la variation maximale de la position y de la particule (+delta, -delta)
        """
        self.velocity.y += random.randint(-delta, delta)

    def update(self):
        """
        Mets à jour la durée de vie de la particule.
        """

        # Si la particule est infinie, elle ne se détruit pas
        if self.lifetime != -1:
            new_lifetime = self.lifetime - self.world.elapsed  # Met à jour la durée de vie
            if new_lifetime < 0:  # Si la durée de vie est inférieure à 0, la particule est détruite
                self.lifetime = 0
                self.kill()
            else:
                self.lifetime = new_lifetime
        super().update()

    def handle_collision(self, old_rect) -> pygame.rect:
        """
        Fige la particule lorsqu'elle entre en collision avec le terrain.
        """
        if pygame.sprite.spritecollideany(self, self.world.map_group):
            self.velocity = Vector(0, 0)
            self.mass = 0  # Ignore la gravité
