import pygame

from src.model.dynamic_object import DynamicObject
from src.utils.map_collision import check_map_collision


class Enemy(DynamicObject):
    """
    Classe qui represente les enemis
    """

    def __init__(self, world, x, y, mass, *groups) -> None:
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        super().__init__(world, x, y, mass, *groups)

        self.direction = True  # True : enemi se dirige vers la droite False gauche

    def update(self):
        self.check_input()
        super().update()

    def check_input(self):
        """
        ici l'ia des enemies choisi le mouvement
        """
        if self.direction:
            self.velocity.x += 00
        else:
            self.velocity.x -= 0
        # self.move(Vector(move_x, 0))

    def handle_collision(self, old_rect) -> pygame.rect:
        self.rect = check_map_collision(self.world.map_group, old_rect, self.rect, self.right, self.left, self.top,
                                        self.bottom)

    def right(self, block):
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = False

    def left(self, block):
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = True

    def top(self, block):
        self.velocity.y = 0

    def bottom(self, block):
        self.velocity.y *= -1
        self.velocity *= block.friction
