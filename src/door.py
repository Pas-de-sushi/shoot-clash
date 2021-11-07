from model.event_box import EventBox
import pygame


class Door(EventBox):
    """
    Porte qui permet de passer au niveau suivant.
    Se déclanche lorsque le joueur est entré en collision avec.

    Propriétés:
    - x, y: position de la porte
    - width, height: taille de la porte
    - groups: tuple groupe auquel de la porte appartient
    """

    def __init__(self, scene, x, y, width, height, groups):
        self.scene = scene
        super().__init__(x, y, width, height,
                         (self.scene.player_group, self.scene.enemy_group), groups)
        self.locked = False
        self.shoot_sound = pygame.mixer.Sound(
            "assets/sounds/door/door_lock_open_01.wav")
        self.set_locked(True)

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
            self.image.fill((225, 0, 0))
        else:
            self.image.fill((155, 155, 0))
            self.shoot_sound.play()
