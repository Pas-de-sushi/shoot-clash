from model.dynamic_object import DynamicObject
from utils.vector import Vector


class Entity(DynamicObject):
    """
    Classe représentant un objet de jeu "vivant".

    Paramètres:
        world: le monde dans lequel se trouve l'entité
        x: la position en x de l'entité
        y: la position en y de l'entité
        mass: la masse de l'entité
        max_health: la vie maximum de l'entité
        groups: les groupes dans lesquels se trouve l'entité

    Propriétés :
        - direction : direction de l'entité ("left" ou "right")
        - max_health : la vie maximum de l'entitée
        - health : la vie actuelle de l'entitée
    """

    def __init__(self, world, x, y, mass: int, max_health: int, groups) -> None:
        super().__init__(world, x, y, mass, groups)  # Appel du constructeur de la classe parente

        self.direction = "right"
        self.max_health = max_health
        self.health = self.max_health

    def move(self, vector: Vector):
        """
        Déplace l'entité d'un vecteur donné.
        Limite la vélocité à 10.
        """
        super(Entity, self).move(vector)

        # Limite la vélocité à 10
        if vector.x > 8:
            vector.x = 8
        if vector.x < -8:
            vector.x = -8

    def receive_damage(self, damage):
        """
        Méthode appelée lorsqu'une entité est attaquée.

        Paramètres:
            damage : le nombre de dégâts reçus
        """
        self.set_health(self.health - damage)

    def set_health(self, new_health):
        """
        Définit la vie de l'entité.

        Si la vie est inférieure à 0, l'entité meurt (méthode die()).
        """
        if new_health > 0:
            self.health = new_health
        else:
            self.health = 0
            self.die()

    def die(self):
        """
        Méthode appellée lorsque l'entité meurt.
        """
        self.kill()
