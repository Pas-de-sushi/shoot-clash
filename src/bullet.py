import pygame
import random

from particles.wall_particle import Wall
from model.dynamic_object import DynamicObject
from utils.vector import Vector


class Bullet(DynamicObject):
    """
    Classe représentant une balle (projectile).

    Paramètres:
        scene: la scene dans lequel la balle est créée
        x: la position en x de la balle
        y: la position en y de la balle
        velocity: la vitesse de la balle
        groups: les groupes de sprites dans lesquels la balle doit apparaître


    """

    def __init__(self, scene, x, y, velocity: Vector, groups, damage) -> None:
        self.image = pygame.Surface([13, 8])
        self.image.fill((250, 250, 0))
        super().__init__(scene, x, y, 0.01, groups)

        self.velocity = velocity
        self.damage = damage

    def handle_collision(self, old_rect) -> pygame.rect:
        """
        Gestion des collisions entre la balle et les autres objets de la scene.
        Détruit la balle si elle touche un autre objet.
        """

        for entity in pygame.sprite.spritecollide(self, self.scene.enemy_group, False):
            entity.receive_damage(self.damage, self)
            self.kill()

        collided_wall = pygame.sprite.spritecollideany(
            self, self.scene.map_group)
        if collided_wall is not None:
            if self.velocity.x > 0:
                corrected_x = collided_wall.rect.x - 2  # Taille particule de 2
            else:
                corrected_x = collided_wall.rect.x + collided_wall.rect.width

        if pygame.sprite.spritecollideany(self, self.scene.map_group):
            for i in range(4):
                Wall(
                    self.scene,
                    corrected_x,
                    self.rect.y + random.randint(0, self.rect.height),
                    Vector(self.velocity.x / 7 * (-1),
                           self.velocity.y / 7 * (-1)),
                    1500,  # 1000 = 1 sec
                    self.scene.particle_group,
                )
            self.kill()


class Weapon:
    """
    Arme du joueur.

    Système de rechargement de l'arme: l'arme possède un nombre maximal de munitions avant le rechargement,
    ainsi qu'un temps de rechargement. Si le joueur dépasse le nombre maximal de munitions,
    il doit attendre le rechargement de toutes les balles pour tirer à nouveau. Le rechargement commence
    une seconde après le dernier tir.

    Attributs :
        image : image de l'arme
        cadence : cadence de tir de l'arme --> 0 = forte cadence et --> 10000+ = faible cadence
        recoil : recul produit par l'arme sur l'utilisateur
        damage : dégats de l'arme
        reload_count : nombre de tirs possibles avant le rechargement
        reload_time : temps pour recharger une munition
        velocity : vitesse des balles

    Propriétés:
        last_shoot: temps depuis le dernier tir
        reload_progress: temps de rechargement actuel
        reload_total: temps de rechargement total (reload_time * reload_count)
        is_burst: True si le joueur est bloquer par le rechargement

    Méthodes :
        shoot() : permet à l'arme de tirer --> méthode appelée par la méthode shoot() de Player
    """

    def __init__(self, image: pygame.Surface, cadence, recoil, damage, reload_count, reload_time, velocity=Vector(22, 0)) -> None:
        self.image = image
        self.cadence = cadence
        self.recoil = recoil
        self.damage = damage
        self.reload_count = reload_count
        self.reload_time = reload_time
        self.reload_total = reload_time * reload_count
        self.velocity = velocity
        self.shoot_sound = pygame.mixer.Sound(
            "assets/sounds/pistolet_tontons_flingueurs.wav")

        self.last_shoot = 0
        self.reload_progress = 0
        self.is_burst = False

    def shoot(self, scene, entity_rect_x, entity_rect_y, entity_direction, group):
        """
        Tire avec l'arme.

        Retourne True si l'arme a tiré, False sinon.

        Paramètres:
            scene: la scene dans lequel la balle est créée
            entity_rect_x: la position en x de l'entité qui tire
            entity_rect_y: la position en y de l'entité qui tire
            entity_direction: la direction de l'entité qui tire
            group: les groupes de sprites dans lesquels la balle doit apparaître
        """
        if not self.is_burst:
            self.last_shoot = 0
            self.reload_progress += self.reload_time

            pygame.mixer.Sound.play(self.shoot_sound)
            Bullet(
                scene,
                entity_rect_x,
                entity_rect_y,
                Vector(self.velocity.x if entity_direction ==
                       "right" else -self.velocity.x, 0),
                group,
                self.damage
            )
            return True
        else:
            return False

    def update_reload(self, elapsed):
        """
        Mets à jour le temps de rechargement. Appelé à chaque frame.
        """
        self.last_shoot += elapsed

        if self.last_shoot > 1000:
            self.reload_progress = max(0, self.reload_progress - elapsed)

        if self.reload_progress >= self.reload_total:
            self.reload_progress = self.reload_total
            self.is_burst = True

        if self.reload_progress == 0:
            self.is_burst = False
