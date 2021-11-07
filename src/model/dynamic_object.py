import pygame

from utils.vector import Vector


class DynamicObject(pygame.sprite.Sprite):
    """
    Classe représentant un objet qui peut bouger.

    Paramètres:
        scene: monde dans lequel se trouve l'objet
        x, y: coordonnées de l'objet
        mass: masse de l'objet
        groups: groupes dans lesquels se trouve l'objet
    """

    def __init__(self, scene, x, y, mass, groups) -> None:
        """
        Constructeur de la classe DynamicObject.

        Attention, il faut initialiser self.image avant de faire appel au constructeur.
        """
        super().__init__(groups)

        # On vérfie que l'image est bien initialisée
        assert self.image is not None, "Initialisez self.image : pygame.Surface avant super.__init__"

        # Positionne l'objet
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)

        self.velocity = Vector(0, 0)
        self.mass = mass  # Utilisée pour la gravité et les collisions
        self.scene = scene

    def update(self):
        """
        Met à jour l'objet. Cette méthode est appelée par pygame.

        - Gestion de la gravité
        - Gestion des collisions
        """
        super().update(self)

        # Sauvegarde de la position avant la mise à jour
        old_rect = self.rect

        # Gravité
        self.velocity.y += self.mass
        self.move(self.velocity)

        # Collisions
        self.handle_collision(old_rect)

    def move(self, vector: Vector):
        """
        Déplace l'objet selon un vecteur.
        """
        self.rect = self.rect.move(vector.x, vector.y)

    def handle_collision(self, old_rect):
        """
        Méthode qui gère les collisions. Doit être implémentée par les classes filles.
        """
        pass
