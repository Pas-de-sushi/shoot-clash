import random

import pygame

from src.particles.blood import Blood
from src.model.dynamic_object import DynamicObject
from utils.vector import Vector


class Bullet(DynamicObject):
    """
    Classe qui represente les projectiles
    """

    def __init__(self, world, x, y, velocity: Vector, *groups) -> None:
        self.image = pygame.Surface([10, 10])
        self.image.fill((0, 0, 250))
        super().__init__(world, x, y, 0.01, *groups)

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
            entity.receive_damage(10, self)
            # entity.velocity = entity.velocity + self.velocity * (self.mass / entity.mass)
            self.kill()
        if pygame.sprite.spritecollideany(self, self.world.map_group):
            #for i in range(10):
            #    Blood(self.world, self.rect.x + random.randint(0, self.rect.width),
            #          self.rect.y + random.randint(0, self.rect.height),
            #          Vector(self.velocity.x * (-1), self.velocity.y * (-1)), self.world.particle_group)
            #Blood(self.world, self.rect.x + random.randint(0, self.rect.width),
            #      self.rect.y + random.randint(0, self.rect.height), Vector(self.velocity.x * 0.1, 0),
            #      self.world.particle_group)
            self.kill()
