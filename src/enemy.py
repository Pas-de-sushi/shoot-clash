import random

import pygame

from model.entity import Entity
from particles.blood import Blood
from utils.collision import check_collision
from utils.vector import Vector


class Enemy(Entity):
    """
    Classe représentant un ennemi.

    Paramètres:
        scene: la scene dans lequel se trouve l'ennemi
        x: la position en x de l'ennemi
        y: la position en y de l'ennemi
        mass: la masse de l'ennemi
        damages: les dégâts infligés lors d'un attaque
        groups: les groupes dans lesquels l'ennemi doit être ajouté
    """

    def __init__(self, scene, x, y, mass, damages, groups) -> None:
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.image.fill((0, 100, 150))

        super(Enemy, self).__init__(scene, x, y, mass, 100, groups)
        self.friction = 0.5
        self.damages = damages
        self.die_sound = [
            pygame.mixer.Sound("assets/sounds/death_ennemy/vo_teefault_pain_short-0" + str(i) + ".wav") for i
            in
            range(1, 10)]

    def update(self):
        """
        Déplacement automatique de l'ennemi.
        """
        if self.health > 0:
            if self.direction == "right":
                self.velocity.x += 0.2
            elif self.direction == "left":
                self.velocity.x -= 0.2
        super().update()

    def handle_collision(self, old_rect):
        """
        Gère les collisions entre l'ennemi et les blocs.
        """

        # Collision avec les blocs
        self.rect = check_collision(
            self.scene.map_group,
            old_rect,
            self.rect,
            self.right,
            self.left,
            self.top,
            self.bottom,
        )

        # Collision avec les autres ennemis
        self.rect = check_collision(
            self.scene.enemy_group,
            old_rect,
            self.rect,
            self.right,
            self.left,
            self.top,
            self.bottom,
        )

        # Collision avec le joueur
        self.rect = check_collision(
            self.scene.player_group,
            old_rect,
            self.rect,
            self.right,
            self.left,
            self.top,
            self.bottom,
        )

    def right(self, block):
        """
        Collision avec un bloc à droite.
        """
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = "left"

    def left(self, block):
        """
        Collision avec un bloc à gauche.
        """
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = "right"

    def top(self, block):
        """
        Collision avec un bloc en haut.
        """
        self.velocity.y = 0

    def bottom(self, block):
        """
        Collision avec un bloc en bas.
        """
        self.velocity.y *= -0.25
        self.velocity *= block.friction
        # if abs(self.velocity.y) > 10: #particules de chute
        #    for i in range(10):
        #        Blood(self.scene, self.rect.x + random.randint(0, self.rect.width),
        #              self.rect.y + random.randint(0, self.rect.height),
        #              Vector(self.velocity.x, self.velocity.y), self.scene.particle_group)

    def receive_damage(self, damage, entity):
        """
        Méthode appelée lorsqu'un ennemi est attaqué.
        """
        self.velocity = self.velocity + entity.velocity * (entity.mass / self.mass)
        for i in range(20):
            Blood(
                self.scene,
                self.rect.x + random.randint(0, self.rect.width),
                self.rect.y + random.randint(0, self.rect.height),
                Vector(entity.velocity.x, entity.velocity.y),
                5000,
                self.scene.particle_group,
            )
        super(Enemy, self).receive_damage(damage)

    def set_health(self, new_health):
        """
        Met à jour la vie de l'ennemi. Sa couleur est modifiée en fonction de sa vie.
        """
        super(Enemy, self).set_health(new_health)
        self.image.fill((255 - int(255 * self.health / self.max_health), 100, 150))

    def die(self):
        """
        Méthode appelée lorsque l'ennemi meurt.
        """
        random.choice(self.die_sound).play()
        super().die()
        self.scene.on_enemy_death()
