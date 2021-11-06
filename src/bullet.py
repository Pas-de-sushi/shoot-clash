import pygame

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

    def __init__(self, world, x, y, velocity: Vector, groups) -> None:
        self.image = pygame.Surface([10, 10])
        self.image.fill((0, 0, 250))
        super().__init__(world, x, y, 0.01, groups)

        self.velocity = velocity

    def handle_collision(self, old_rect) -> pygame.rect:
        """
        Gestion des collisions entre la balle et les autres objets du monde.
        Détruit la balle si elle touche un autre objet.
        """

        for entity in pygame.sprite.spritecollide(self, self.world.enemy_group, False):
            # entity.kill()
            entity.receive_damage(10, self)
            # entity.velocity = entity.velocity + self.velocity * (self.mass / entity.mass)
            self.kill()
        if pygame.sprite.spritecollideany(self, self.world.map_group):
            # for i in range(10):
            #    Blood(self.world, self.rect.x + random.randint(0, self.rect.width),
            #          self.rect.y + random.randint(0, self.rect.height),
            #          Vector(self.velocity.x * (-1), self.velocity.y * (-1)), self.world.particle_group)
            # Blood(self.world, self.rect.x + random.randint(0, self.rect.width),
            #      self.rect.y + random.randint(0, self.rect.height), Vector(self.velocity.x * 0.1, 0),
            #      self.world.particle_group)
            self.kill()
