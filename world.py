import pygame

from block import Block
from constants import *
from level import Level
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

        self.level = Level(self)

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.map_group.draw(self.screen)

        self.player_group.update()
        self.player_group.draw(self.screen)
