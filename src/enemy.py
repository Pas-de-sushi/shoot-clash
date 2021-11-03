import random

import pygame

from model.entity import Entity
from particles.blood import Blood
from utils.map_collision import check_map_collision
from utils.vector import Vector


class Enemy(Entity):
    """
    Classe qui represente les ennemis
    """

    def __init__(self, world, x, y, mass, *groups) -> None:
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.image.fill((0, 100, 150))

        super(Enemy, self).__init__(world, x, y, mass, 100, groups)
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
            self.velocity.x += 0.2
        else:
            self.velocity.x -= 0.2
        # self.move(Vector(move_x, 0))

    def handle_collision(self, old_rect):
        self.rect = check_map_collision(
            self.world.map_group,
            old_rect,
            self.rect,
            self.right,
            self.left,
            self.top,
            self.bottom,
        )
        self.rect = check_map_collision(
            self.world.enemy_group,
            old_rect,
            self.rect,
            self.right,
            self.left,
            self.top,
            self.bottom,
        )

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
        self.velocity.y *= -0.25
        self.velocity *= block.friction
        # if abs(self.velocity.y) > 10: #particules de chute
        #    for i in range(10):
        #        Blood(self.world, self.rect.x + random.randint(0, self.rect.width),
        #              self.rect.y + random.randint(0, self.rect.height),
        #              Vector(self.velocity.x, self.velocity.y), self.world.particle_group)

    def receive_damage(self, damage, entity):
        self.velocity = self.velocity + entity.velocity * (entity.mass / self.mass)
        for i in range(20):
            Blood.random_direction(
                self.world,
                self.rect.x + random.randint(0, self.rect.width),
                self.rect.y + random.randint(0, self.rect.height),
                Vector(entity.velocity.x, entity.velocity.y),
                self.world.particle_group,
            )
        super(Enemy, self).receive_damage(damage)

    def set_health(self, new_health):
        super(Enemy, self).set_health(new_health)
        self.image.fill((255 - int(255 * self.health / self.max_health), 100, 150))
