import pygame

from block import Block


class EventBox(Block):
    """
    Bloc de gestion des collisions.

    Paramètres:
        - x, y: coordonnées du sprite
        - width, height: dimensions du sprite
        - watch_groups: liste des groupes à surveiller
        - groups: liste des groupes dans lesquels le sprite est ajouté

    """

    def __init__(self, x, y, width, height, watch_groups, groups):
        super().__init__(x, y, width, height, (150, 150, 0), groups, 1)
        self.watch_groups = watch_groups

    def update(self):
        super().update(self)
        self.check_collisions()

    def check_collisions(self):
        """
        Déclanche la métode on_collision si un sprite present dans les groupes watch_groups rentre en collision
        avec le sprite.
        """
        for groups in self.watch_groups:
            collided_sprites = pygame.sprite.spritecollide(self, groups, False)
            for sprite in collided_sprites:
                self.on_collision(sprite)

    def on_collision(self, entity):
        """
        Méthode déclenchée lorsqu'une collision est détectée.
        Doit être implémentée par les classes filles.

        Paramètres:
            - entity: entité sur laquelle la collision a été détectée
        """
        pass
