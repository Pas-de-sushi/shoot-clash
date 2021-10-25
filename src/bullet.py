import pygame
from constants import *
from src.model.dynamic_object import DynamicObject
from utils.vector import Vector


class Bullet(DynamicObject):
    """
    Classe qui represente les projectiles
    """

    def __init__(self, world, x, y, velocity: Vector, *groups) -> None:
        self.image = pygame.Surface([10, 15])
        self.image.fill((0, 0, 250))
        super().__init__(world, x, y, 0.1, *groups)

        self.velocity = velocity

    def update(self):
        super().update()

    def handle_collision(self, old_rect) -> pygame.rect:
        """
        Detruit la balle apres colision
        Donne vitesse a l'ennemi
        """
        for entity in pygame.sprite.spritecollide(self, self.world.enemy_group, False):
            # entity.kill()
            entity.velocity = entity.velocity + self.velocity * (self.mass / entity.mass)
            self.kill()
        if pygame.sprite.spritecollideany(self, self.world.map_group):
            self.kill()
