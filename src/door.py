from model.event_box import EventBox


class Door(EventBox):
    """
    Porte permet au joueur de passer au niveau superieur
    groups: tuple groupe auquel la boite appartient
    """

    def __init__(self, world, x, y, width, height, groups: tuple):
        self.world = world
        super().__init__(x, y, width, height, (self.world.player_group, self.world.enemy_group), groups)
        self.locked = False
        self.set_locked(True)

    def on_collision(self, entity):
        super().on_collision(entity)
        if self.locked == False:
            print('Exit !')
            self.set_locked(True)

    def set_locked(self, state):
        """
        Actualise la vue
        """
        self.locked = state
        if self.locked:
            self.image.fill((225, 0, 0))
        else:
            self.image.fill((155, 155, 0))
