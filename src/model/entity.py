from model.dynamic_object import DynamicObject
from utils.vector import Vector


class Entity(DynamicObject):
    """
    Classe qui represente les objets dynamiques Vivants
    - vie
    - recevoir dégats
    """

    def __init__(self, world, x, y, mass: int, max_health: int, groups: tuple) -> None:

        super().__init__(world, x, y, mass, groups)

        self.direction = True  # True : l'entitée se dirige vers la droite False gauche
        self.max_health = max_health
        self.health = self.max_health

    def update(self):
        self.check_input()
        super().update()

    def handle_collision(self, old_rect):
        super().handle_collision(old_rect)
        pass

    def move(self, vector: Vector):
        super(Entity, self).move(vector)
        # Système de vitesse max --> collision avec l'air c'est galère
        if vector.x > 10:
            vector.x = 10
        if vector.x < -10:
            vector.x = -10

    def receive_damage(self, damage):
        self.set_health(self.health - damage)

    def set_health(self, new_health):
        if new_health > 0:
            self.health = new_health

        else:
            self.health = 0
            self.die()

    def die(self):
        self.kill()
