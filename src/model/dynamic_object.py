import pygame

from utils.vector import Vector


class DynamicObject(pygame.sprite.Sprite):
    """
    Classe qui represente les mouvants
    """

    def __init__(self, world, x, y, mass, groups: tuple) -> None:
        """
        Creer  self.image avant d'appeler
        """
        super().__init__(groups)
        assert (
            self.image is not None,
            "Initialisez self.image : pygame.Surface avant super.__init__",
        )
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.velocity = Vector(0, 0)
        self.mass = mass  # Sert pour la gravité et le transfer de vitesse (collisions)
        self.world = world

    def update(self):
        super().update(self)
        old_rect = self.rect
        self.velocity.y += self.mass
        self.move(self.velocity)
        self.handle_collision(old_rect)

    def move(self, vector: Vector):
        self.rect = self.rect.move(vector.x, vector.y)

    def handle_collision(self, old_rect):
        """
        Executé a la fin de update
        """
        pass
