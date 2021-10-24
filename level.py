import pygame

from block import Block
from constants import *
from sprites import Player


class Level:
    """
    Classe en charge d'initialiser le niveau
    """

    def __init__(self, world):
        self.world = world
        self.load_level()

    def load_level(self):
        Block(300, 300, 100, 400, (100, 255, 100), 1.5, self.world.map_group)
        Block(0, 200, 300, 100, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        Block(400, 150, 400, 400, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        Block(800, 50, 100, 100, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        Block(0, 50, 100, 150, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)

        Player(self.world, 10, 10, self.world.player_group)
