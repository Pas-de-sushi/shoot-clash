import pygame

from model.dynamic_object import DynamicObject
from utils.vector import Vector


class Entity(DynamicObject):
    """
    Classe représentant un objet de jeu "vivant".

    Paramètres:
        scene: la scene dans lequel se trouve l'entité
        x, y: coordonnées de l'entité
        width, height: dimensions de l'entité
        image: l'image de l'entité (direction droite)
        mass: la masse de l'entité
        max_health: la vie maximum de l'entité
        groups: les groupes dans lesquels se trouve l'entité

    Propriétés :
        - image_right : l'image de l'entité en direction droite
        - image_left : l'image de l'entité en direction gauche
        - image: l'image de l'entité actuelle
        - direction : direction de l'entité ("left" ou "right")
        - max_health : la vie maximum de l'entitée
        - health : la vie actuelle de l'entitée
    """

    def __init__(self, scene, x, y, width, height, image, mass: int, max_health: int, groups) -> None:
        # Charge l'image et la redimensionne
        image = pygame.image.load(image).convert_alpha()
        image = pygame.transform.scale(image, (width, height))

        self.image_right = image
        self.image_left = pygame.transform.flip(image, True, False)
        self.image = image

        super().__init__(scene, x, y, mass, groups)  # Appel du constructeur de la classe parente


        self.direction = "right"
        self.max_health = max_health
        self.health = self.max_health

    def type(self):
        """
        Retourne le type de l'entité.
        """
        return "entity"

    def move(self, vector: Vector):
        """
        Déplace l'entité d'un vecteur donné.
        Limite la vélocité à 8 et mets à jour l'image en fonction de la direction.
        """
        if self.direction == "right":
            self.image = self.image_right
        else:
            self.image = self.image_left

        vector.limit(8, None)
        super(Entity, self).move(vector)

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
