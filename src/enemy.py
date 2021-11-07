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
        width, height: la taille de l'ennemi
        image: l'image de l'ennemi
        mass: la masse de l'ennemi
        damages: les dégâts infligés lors d'un attaque
        max_health: la vie maximale de l'ennemi
        groups: les groupes dans lesquels l'ennemi doit être ajouté
    """

    def __init__(self, scene, x, y, image, mass, damages, max_health, groups) -> None:
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.image.fill((0, 100, 150))

        super(Enemy, self).__init__(
            scene, x, y, image, mass, max_health, groups)
        self.friction = 0.5
        self.damages = damages
        self.die_sound = [
            # pygame.mixer.Sound("assets/sounds/death_ennemy/vo_teefault_pain_short-0" + str(i) + ".wav") for i
            # pygame.mixer.Sound("assets/sounds/pop/sfx_pickup_hrt-0" + str(i) + ".wav") for i in range(1, 3)]
            pygame.mixer.Sound("assets/sounds/death_enemy/foley_body_splat-0" + str(i) + ".wav") for i in range(1, 5)]

        self.pain_sound = [
            pygame.mixer.Sound("assets/sounds/pain_enemy/foley_body_impact-0" + str(i) + ".wav") for i in range(1, 4)]

    def type(self):
        return "enemy"

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
        self.player_collision(block)

    def left(self, block):
        """
        Collision avec un bloc à gauche.
        """
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = "right"
        self.player_collision(block)

    def top(self, block):
        """
        Collision avec un bloc en haut.
        """
        self.velocity.y = 0
        self.player_collision(block)

    def bottom(self, block):
        """
        Collision avec un bloc en bas.
        """
        self.velocity.y *= -0.25
        self.velocity *= block.friction
        self.player_collision(block)
        # if abs(self.velocity.y) > 10: #particules de chute
        #    for i in range(10):
        #        Blood(self.scene, self.rect.x + random.randint(0, self.rect.width),
        #              self.rect.y + random.randint(0, self.rect.height),
        #              Vector(self.velocity.x, self.velocity.y), self.scene.particle_group)

    def player_collision(self, block):
        """
        Méthode appelée lorsqu'un ennemi touche le joueur.
        """
        if isinstance(block, Entity) and block.type() == "player":
            block.receive_damage(self.damages)

    def receive_damage(self, damage, entity):
        """
        Méthode appelée lorsqu'un ennemi est attaqué.
        """
        self.velocity = self.velocity + \
            entity.velocity * (entity.mass / self.mass)
        for i in range(20):
            Blood(
                self.scene,
                self.rect.x + random.randint(0, self.rect.width),
                self.rect.y + random.randint(0, self.rect.height),
                Vector(entity.velocity.x, entity.velocity.y),
                5000,
                self.scene.particle_group,
            )
        # random.choice(self.pain_sound).play()
        super().receive_damage(damage)

    def set_health(self, new_health):
        """
        Met à jour la vie de l'ennemi. Sa couleur est modifiée en fonction de sa vie.
        """
        super(Enemy, self).set_health(new_health)

    def die(self):
        """
        Méthode appelée lorsque l'ennemi meurt.
        """
        random.choice(self.die_sound).play()
        super().die()
        self.scene.on_enemy_death()
