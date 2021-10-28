import random

import pygame

from src.particles.blood import Blood
from src.model.dynamic_object import DynamicObject
from src.utils.map_collision import check_map_collision
from src.utils.vector import Vector


class Enemy(DynamicObject):
    """
    Classe qui represente les enemis
    """

    def __init__(self, world, x, y, mass, *groups) -> None:
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.image.fill((0, 100, 150))

        super().__init__(world, x, y, mass, *groups)

        self.direction = True  # True : ennemi se dirige vers la droite False gauche

        self.max_health = 100
        self.health = self.max_health
        self.friction = 0.5

    def update(self):
        if self.health > 0:
            self.check_input()
        super().update()

    def check_input(self):
        """
        ici l'ia des enemies choisi le mouvement
        """
        if self.direction:
            self.velocity.x += 0.1
        else:
            self.velocity.x -= 0.1
        # self.move(Vector(move_x, 0))

    def handle_collision(self, old_rect) -> pygame.rect:
        self.rect = check_map_collision(self.world.map_group, old_rect, self.rect, self.right, self.left, self.top,
                                        self.bottom)
        self.rect = check_map_collision(self.world.enemy_group, old_rect, self.rect, self.right, self.left, self.top,
                                        self.bottom)

    def right(self, block):
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = False

    def left(self, block):
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = True

    def top(self, block):
        self.velocity.y = 0

    def bottom(self, block):
        self.velocity.y *= -1
        self.velocity *= block.friction
        #if abs(self.velocity.y) > 10: #particules de chute
        #    for i in range(10):
        #        Blood(self.world, self.rect.x + random.randint(0, self.rect.width),
        #              self.rect.y + random.randint(0, self.rect.height),
        #              Vector(self.velocity.x, self.velocity.y), self.world.particle_group)

    def receive_damage(self, damage, entity):
        self.velocity = self.velocity + entity.velocity * (entity.mass / self.mass)
        self.set_health(self.health - 10)
        for i in range(20):
            Blood.random_direction(self.world, self.rect.x + random.randint(0, self.rect.width),
                                   self.rect.y + random.randint(0, self.rect.height),
                                   Vector(entity.velocity.x, entity.velocity.y), self.world.particle_group)

    def set_health(self, new_health):

        if new_health > 0:
            self.health = new_health
            self.image.fill((255 - int(255 * self.health / self.max_health), 100, 150))

        else:
            self.health = 0
            self.die()

    def die(self):
        # self.mass = 0.1
        # self.velocity *= 2
        self.kill()
