import pygame

from model.particle import Particle
from utils.vector import Vector


class Blood(Particle):
    """
    Classe qui represente les particules de sang
    Se figent lors du contact avec la map
    params:
    world : Object World
    x : localisation spawn x int
    y : localisation spawn y int
    velocity: velocité de depart
    groups: groupe au quel la particule appartient : pygame.Groups
    ex:particle_group

    """

    def __init__(self, world, x, y, velocity: Vector, groups: tuple) -> None:
        self.image = pygame.Surface([5, 5])
        self.image.fill((200, 0, 0))

        super().__init__(world, x, y, 1, velocity, -1, groups)

    @classmethod
    def random_direction(cls, world, x, y, velocity: Vector, groups: tuple):
        """
        Constructeur qui ajoute de la randomisation sur l'axe y de la particule
        """
        _instance = cls(world, x, y, velocity, groups)
        _instance.randomize_direction()
        return _instance
