import pygame

from block import Block


class EventBox(Block):
    """
    Boite evenement declanche evenement lors de collision
    watch_groups: groupes surveillés pour les evenements
    groups: tuple groupe auquel la boite appartient
    """

    def __init__(self, x, y, width, height, watch_groups, groups):
        super().__init__(x, y, width, height, (150, 150, 0), groups, 1)

        self.watch_groups = watch_groups

    def update(self):
        super().update(self)
        self.check_collisions()

    def check_collisions(self):
        """
        Declanche on_collision quand un sprite present dans les groupes watch_groups rentre en collision
        """
        for groups in self.watch_groups:
            collided_sprites = pygame.sprite.spritecollide(self, groups, False)
            for sprite in collided_sprites:
                self.on_collision(sprite)

    def on_collision(self, entity):
        """
        Est declanché quand un sprite present dans les groupes watch_groups rentre en collision
        Propriétés:
        - entity: objet qui est en collision
        """

        pass
