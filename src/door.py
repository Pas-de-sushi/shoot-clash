from model.event_box import EventBox


class Door(EventBox):
    """
    Porte
    permet au joueur de passer au niveau superieur

    Propriétés:
    - x, y: position de la porte
    - width, height: taille de la porte
    - groups: tuple groupe auquel de la porte appartient
    """

    def __init__(self, world, x, y, width, height, groups: tuple):
        self.world = world
        super().__init__(x, y, width, height, (self.world.player_group, self.world.enemy_group), groups)
        self.locked = False
        self.set_locked(True)

    def on_collision(self, entity):
        """
        Est appelé lorsque un joueur est entré en collision avec la porte
        
        Propriétés:
        - entity: entité qui est entré en colision
        """
        super().on_collision(entity)
        if self.locked == False:
            self.world.level.player_access_door()
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
