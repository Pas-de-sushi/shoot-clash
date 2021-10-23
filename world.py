import pygame

from block import Block
from constants import *
from sprites import Player


class World:
    """
    Classe represente le monde
    Est passé aux objets
    """

    def __init__(self, screen):
        self.screen = screen

        self.player_group = pygame.sprite.Group()
        self.map_group = pygame.sprite.Group()

        self.player = [Player(self, i * 10, i * 10, self.player_group) for i in range(5)]

        self.block = Block(300, 300, 100, 400, (100, 255, 100), 1.5, self.map_group)
        self.block = Block(0, 200, 300, 100, (255, 255, 255), BLOCK_FRICTION, self.map_group)
        self.block = Block(400, 150, 400, 400, (255, 255, 255), BLOCK_FRICTION, self.map_group)

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.map_group.draw(self.screen)

        self.player_group.update()
        self.player_group.draw(self.screen)
