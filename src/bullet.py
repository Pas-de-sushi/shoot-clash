import pygame
import random

from particles.wall_particle import Wall
from model.dynamic_object import DynamicObject
from utils.vector import Vector


class Bullet(DynamicObject):
    """
    Classe représentant une balle (projectile).

    Paramètres:
        world: le monde dans lequel la balle est créée
        x: la position en x de la balle
        y: la position en y de la balle
        velocity: la vitesse de la balle
        groups: les groupes de sprites dans lesquels la balle doit apparaître


    """

    def __init__(self, world, x, y, velocity: Vector, groups, damage) -> None:
        self.image = pygame.Surface([6, 6])
        self.image.fill((250, 250, 0))
        super().__init__(world, x, y, 0.01, groups)

        self.velocity = velocity
        self.damage = damage

    def handle_collision(self, old_rect) -> pygame.rect:
        """
        Gestion des collisions entre la balle et les autres objets du monde.
        Détruit la balle si elle touche un autre objet.
        """

        for entity in pygame.sprite.spritecollide(self, self.world.enemy_group, False):
            # entity.kill()
            entity.receive_damage(self.damage, self)
            # entity.velocity = entity.velocity + self.velocity * (self.mass / entity.mass)
            self.kill()

        collided_wall = pygame.sprite.spritecollideany(self, self.world.map_group)
        if collided_wall is not None:
            if self.velocity.x > 0:
                corrected_x = collided_wall.rect.x - 2 # Taille particule de 2
            else:
                corrected_x = collided_wall.rect.x + collided_wall.rect.width

        if pygame.sprite.spritecollideany(self, self.world.map_group):
            for i in range(4):
                Wall(
                    self.world,
                    corrected_x,
                    self.rect.y + random.randint(0, self.rect.height),
                    Vector(self.velocity.x / 7 * (-1), self.velocity.y / 7 * (-1)),
                    1500, # 1000 = 1 sec
                    self.world.particle_group,
            )
            self.kill()

class Weapon:
    """
    Arme du joueur.

    Attributs :
        cadence : cadence de tir de l'arme --> 0 = forte cadence et --> 10000+ = faible cadence
        recoil : recul produit par l'arme sur l'utilisateur
        damage : dégats de l'arme
        velocity : vitesse des balles

    Méthodes :
        shoot() : permet à l'arme de tirer --> méthode appelée par la méthode shoot() de Player
    """
    def __init__(self, cadence, recoil, damage, velocity=Vector(22,0)) -> None:
        self.cadence = cadence
        self.recoil = recoil
        self.damage = damage
        self.velocity = velocity

    def shoot(self, world, entity_rect_x, entity_rect_y, entity_direction, group):
        """
        Tire avec l'arme.

        Paramètres:
            world: le monde dans lequel la balle est créée
            entity_rect_x: la position en x de l'entité qui tire
            entity_rect_y: la position en y de l'entité qui tire
            entity_direction: la direction de l'entité qui tire
            group: les groupes de sprites dans lesquels la balle doit apparaître
        """

        Bullet(
            world,
            entity_rect_x,
            entity_rect_y,
            Vector(self.velocity.x if entity_direction == "right" else -self.velocity.x, 0),
            group,
            self.damage
        )
