import pygame
from constants import *
from utils.vector import Vector


class Player(pygame.sprite.Sprite):
    """
    Classe qui represente le joueur
    """

    def __init__(self, world, x, y, *groups) -> None:
        super().__init__(*groups)

        self.image = pygame.Surface([10, 15])
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.velocity = Vector(0, 0)

        self.jump_count = 0
        self.max_jump = 1
        self._old_jump_state = False  # Detection relachement
        self.world = world

    def update(self):
        super().update(self)
        self.check_input()
        self.velocity.y += 1
        self.move(self.velocity)

    def check_input(self):
        pressed_keys = pygame.key.get_pressed()
        move = Vector(0, 0)
        if pressed_keys[pygame.K_LEFT]:
            move.x -= 1
        if pressed_keys[pygame.K_RIGHT]:
            move.x += 1

        if pressed_keys[pygame.K_UP]:
            if not self._old_jump_state:  # Attend relachement de la touche
                self._old_jump_state = True
                if self.jump_count < self.max_jump:
                    move.y -= 15
                    self.jump_count += 1

        else:
            self._old_jump_state = False
        self.velocity += move
        # self.move(Vector(move_x, 0))

    def move(self, vector: Vector):
        # TODO : executer check collisions seulement a la fin de update
        self.rect = self.check_collision(self.rect, self.rect.move(vector.x, vector.y))

    def check_collision(self, old_rect, new_rect) -> pygame.rect:
        """
        Corrige la position avec la collision
        :param x: deplacement effectué x
        :param y: deplacement effectué y
        :param rect: position voulue
        :return: rect : Position corrigée
        """

        corrected_rect = new_rect
        for block in self.world.map_group:
            if new_rect.colliderect(block):
                # print(block.rect.left)
                # Collision parfaite :
                """
                    """
                if (new_rect.x + new_rect.width > block.rect.x) and (old_rect.x + old_rect.width <= block.rect.x):
                    corrected_rect.x = block.rect.x - new_rect.width - 1  # le 1 desactive la collision (perf)
                    # print("right")
                    self.velocity.x *= -1
                    self.velocity *= block.friction
                    # self.velocity.x = 0
                if (new_rect.x < block.rect.x + block.rect.width) and (old_rect.x >= block.rect.x + block.rect.width):
                    corrected_rect.x = block.rect.x + block.rect.width + 1
                    # print("left")
                    self.velocity.x *= -1
                    self.velocity *= block.friction
                    # self.velocity.x = 0

                # corrected_rect.y = block.rect.y + block.rect.height + 1
                if (new_rect.y < block.rect.y + block.rect.height) and (
                        old_rect.y >= block.rect.y + block.rect.height):
                    # print("top")
                    self.velocity.y = 0
                if (new_rect.y + new_rect.height > block.rect.y) and (old_rect.y + old_rect.height <= block.rect.y):
                    # print("bottom")
                    self.velocity.y *= -1  # TODO: Sortir ça d'ici
                    self.velocity *= block.friction
                    self.jump_count = 0
                    # print(new_rect.y)
                    corrected_rect.y = block.rect.y - old_rect.height - 1
                    # self.velocity.y = 0

        return corrected_rect
