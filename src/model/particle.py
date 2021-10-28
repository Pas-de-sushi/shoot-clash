import random

import pygame

from src.model.dynamic_object import DynamicObject
from src.utils.vector import Vector


class Particle(DynamicObject):
    """
    Classe qui represente les particules de sang
    Se figent lors du contact avec la map
    params:
    world : Object World
    x : localisation spawn x int
    y : localisation spawn y int
    velocity: velocité de depart
    lifetime: int temps apres lequel la particule est detruite en ms: -1 infini
    groups: groupe au quel la particule appartient : pygame.Groups
    ex:particle_group

    """

    def __init__(self, world, x: int, y: int, mass, velocity: Vector, lifetime, *groups) -> None:
        """
        Declarer self.image avant d'appeler super.init
        ex:
            self.image = pygame.Surface([5, 5])
            self.image.fill((200, 0, 0))
        """
        # self.image = pygame.Surface([5, 5])
        #        self.image.fill((200, 0, 0))
        # self.image.fill((200, 0, 0))

        super().__init__(world, x, y, mass, *groups)

        self.velocity = Vector(velocity.x, velocity.y)
        self.mass = 1
        self.lifetime = lifetime

    def randomize_direction(self):
        """
        Constructeur qui ajoute de la randomisation sur l'axe y de la particule
        """
        self.velocity.y += random.randint(-10, 10)

    def update(self):
        if self.lifetime != -1:
            _new_lifetime = self.lifetime - self.world.elapsed
            if _new_lifetime < 0:
                self.lifetime = 0
                self.kill()
            else:
                self.lifetime = _new_lifetime
        super().update()

    def handle_collision(self, old_rect) -> pygame.rect:
        """
        Fige la particule en cas de contact avec le terrain
        """

        if pygame.sprite.spritecollideany(self, self.world.map_group):
            self.velocity = Vector(0, 0)
            self.mass = 0
            # self.rect
