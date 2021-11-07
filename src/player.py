import pygame
import random

from constants import *
from particles.cartridge_particle import Cartridge
from bullet import Bullet, Weapon
from enemy import Enemy
from model.entity import Entity
from utils.collision import check_collision
from utils.vector import Vector


class Player(Entity):
    """
    Classe qui represente le joueur. Hérite de la classe Entity.

    Paramètres:
    - scene: instance de la classe scene
    - x, y: position du joueur
    - mass: masse du joueur
    - groups: tuple des groupes d'entités

    Propriétés:
    """

    def __init__(self, scene, x, y, mass, groups, weapon) -> None:
        super().__init__(scene, x, y, "assets/player.png", mass, PLAYER_MAX_HEALTH, groups)

        self.jump_count = 0  # Nombre de sauts effectués
        self.direction = "right"  # Direction du joueur (left/right)
        self.previous_jump = False  # Permet d'éviter un appui long pour le saut
        self.last_shoot = 0  # Temps depuis le dernier tir
        self.last_damage = 0  # Temps depuis les derrières dommages reçus

        self.friction = 0.5
        self.weapon = weapon

    def type(self):
        return "player"

    def update(self):
        """
        Mise à jour de l'état du joueur.
        Gestion des touches.
        """

        # Récupération des touches pressées par l'utilisateur
        pressed_keys = pygame.key.get_pressed()
        movement = Vector(0, 0)

        # Déplacement gauche
        if pressed_keys[pygame.K_LEFT]:
            movement.x = -SPEED
            self.direction = "left"

        # Déplacement droit
        if pressed_keys[pygame.K_RIGHT]:
            movement.x += SPEED
            self.direction = "right"

        # Saut
        if pressed_keys[pygame.K_UP] and not self.previous_jump:
            if self.jump_count < MAX_JUMP:
                movement.y = -JUMP_HEIGHT
                self.jump_count += 1

        # Tir
        if self.last_shoot >= self.weapon.cadence:
            if pressed_keys[pygame.K_SPACE]:
                self.shoot()
                self.last_shoot = 0
        else:
            self.last_shoot += self.scene.elapsed

        self.velocity += movement
        self.last_damage += self.scene.elapsed
        super().update()

    def shoot(self):
        """
        Gestion du tir : création d'une balle et recul sur le joueur.
        """

        self.weapon.shoot(
            self.scene,
            self.rect.x - self.image.get_width() / 2,
            self.rect.y + self.image.get_height() / 2,
            self.direction,
            (self.scene.bullet_group),
        )

        # Cartouches
        Cartridge(
            self.scene,
            self.rect.x,
            self.rect.y,
            Vector(random.randint(1, 4) if self.direction == "left" else
                   random.randint(-4, -1),
                   random.randint(2, 5)),
            2000,
            self.scene.particle_group,
        )

        # Recul de l'arme
        if self.direction == "left":
            self.velocity.x += (self.weapon.recoil * 3) / self.mass
        else:
            self.velocity.x += (self.weapon.recoil * -3) / self.mass

    def show_health(self):
        """
        Affiche la barre de vie du joueur.
        """

        # Pourcentage de vie du joueur
        health_percent = self.health / PLAYER_MAX_HEALTH

        # Milieu de la position x du joueur
        x = self.rect.x + self.rect.width / 2
        # Taille de la barre en fonction de la vie du joueur
        width = 40 * (self.health / PLAYER_MAX_HEALTH)
        # Couleur de la barre en fonction de la vie du joueur
        color = (255 - health_percent * 255, health_percent * 255, 0)

        pygame.draw.rect(
            self.scene.screen,
            color,
            (x - 20, self.rect.y - 15, width, 3),
        )

    def receive_damage(self, damage):
        """
        Gestion des dommages reçus.
        """
        if self.last_damage >= DAMAGE_COOLDOWN:
            super().receive_damage(damage)
            self.last_damage = 0

    def handle_collision(self, old_rect):
        """
        Gestion des collisions entre le joueur et les blocs.
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

        # Collision avec les ennemis
        self.rect = check_collision(
            self.scene.enemy_group,
            old_rect,
            self.rect,
            self.right,
            self.left,
            self.top,
            self.bottom,
        )

    def enemy_collision(self, block):
        """
        Collision avec un ennemi (rebond et dommages).
        *
        Vélocité maximale de 15.
        """
        if isinstance(block, Entity) and block.type() == "enemy":
            # Les dommages sont gérés à la fois au niveau de l'ennemi et au niveau du joueur
            # en fonction de quelle entité avance.
            self.receive_damage(block.damages)

            velocity = self.velocity * 3
            velocity.limit(15, 15)
            self.velocity = velocity

    def right(self, block):
        """
        Collision avec un bloc à droite du joueur.
        """
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = "left"
        self.enemy_collision(block)

    def left(self, block):
        """
        Collision avec un bloc à gauche du joueur.
        """
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = "right"
        self.enemy_collision(block)

    def top(self, block):
        """
        Collision avec un bloc en haut du joueur.
        """
        self.velocity.y = 0
        self.enemy_collision(block)

    def bottom(self, block):
        """
        Collision avec un bloc en bas du joueur.
        """
        self.velocity.y *= -0.25
        self.velocity *= block.friction
        self.jump_count = 0
        self.enemy_collision(block)
