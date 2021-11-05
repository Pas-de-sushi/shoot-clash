import pygame

from constants import *
from bullet import Bullet
from model.entity import Entity
from utils.map_collision import check_map_collision
from utils.vector import Vector


class Player(Entity):
    """
    Classe qui represente le joueur. Hérite de la classe Entity.

    Propriétés:
    - world: instance de la classe World
    - x, y: position du joueur
    - mass: masse du joueur
    - groups: tuple des groupes d'entités
    """

    def __init__(self, world, x, y, mass, groups) -> None:
        self.image = pygame.Surface([10, 15])
        self.image.fill((0, 255, 0))

        super().__init__(world, x, y, mass, 100, groups)

        self.jump_count = 0  # Nombre de sauts effectués
        self.direction = "right"  # Direction du joueur (left/right)
        self.previous_jump = False  # Permet d'éviter un appui long pour le saut
        self.last_shoot = 0  # Temps depuis le dernier tir

        self.shoot_delay = 100  # une balle sec

    def update(self):
        """
        Mise à jour de l'état du joueur.
        Gestion des touches
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
        if self.last_shoot >= SHOOT_DELAY:
            if pressed_keys[pygame.K_SPACE]:
                self.shoot()
                self.last_shoot = 0
        else:
            self.last_shoot += self.world.elapsed

        self.velocity += movement
        super().update()

    def shoot(self):
        """
        Gestion du tir.
        """
        if self.direction == "left":
            velocity = -BULLET_SPEED
            self.velocity -= Vector(-3, 0)
        elif self.direction == "right":
            velocity = BULLET_SPEED
            self.velocity -= Vector(3, 0)

        Bullet(
            self.world,
            self.rect.x,
            self.rect.y,
            Vector(velocity, 0),
            (self.world.bullet_group),
        )

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
        self.jump_count = 0
