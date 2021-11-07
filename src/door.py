import pygame
from model.event_box import EventBox


class Door(EventBox):
    """
    Porte qui permet de passer au niveau suivant.
    Se déclanche lorsque le joueur est entré en collision avec.

    Paramètres:
    - scene: scene où se trouve la porte
    - x, y: position de la porte
    - groups: tuple groupe auquel de la porte appartient
    """

    def __init__(self, scene, x, y, groups):
        self.scene = scene
        self.image_closed = pygame.image.load("assets/door-closed.png").convert_alpha()
        self.image_open = pygame.image.load("assets/door-open.png").convert_alpha()
        self.locked = False

        super().__init__(x, y, "assets/door-closed.png", (self.scene.player_group, self.scene.enemy_group), groups)

    def on_collision(self, entity):
        """
        Est appelé lorsque un joueur est entré en collision avec la porte

        Propriétés:
        - entity: entité qui est entré en colision
        """
        super().on_collision(entity)
        if self.locked == False:
            self.scene.next_level()
            self.set_locked(True)

    def set_locked(self, state: bool):
        """
        Definie si la porte est verouillé ou non et actualise la vue
        """
        self.locked = state
        if self.locked:
            self.image = self.image_closed
        else:
            self.image = self.image_open
