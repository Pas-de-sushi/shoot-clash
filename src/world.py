import pygame

from block import Block
from constants import *
from level import Level
from player import Player


class World:
    """
    Classe represente le monde
    Est passé aux objets
    """

    def __init__(self, screen):
        self.screen = screen

        self.enemy_group = pygame.sprite.Group()
        self.map_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.level = Level(self)
        self.elapsed = 0

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.map_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.player_group.draw(self.screen)

    def update(self, elapsed):
        self.elapsed = elapsed
        self.enemy_group.update()
        self.bullet_group.update()
        self.player_group.update()
