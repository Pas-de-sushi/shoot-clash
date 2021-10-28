from block import Block
from constants import *
from player import Player
from src.enemy import Enemy


class Level:
    """
    Classe en charge d'initialiser le niveau
    """

    def __init__(self, world):
        self.world = world
        self.load_level()

    def load_level(self):
        # Block(300, 300, 100, 400, (100, 255, 100), 1.5, self.world.map_group)
        # Block(0, 200, 300, 100, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        # Block(400, 150, 400, 400, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        # Block(800, 50, 100, 100, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        # Block(0, 50, 100, 150, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        Block(0, 0, SCREEN_WIDTH, 10, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        Block(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        Block(0, 10, 10, SCREEN_HEIGHT - 10, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)
        Block(SCREEN_WIDTH - 100, 10, 100, SCREEN_HEIGHT - 10, (255, 255, 255), BLOCK_FRICTION,
              self.world.map_group)  # Droite
        Block(0, SCREEN_HEIGHT - 200, SCREEN_WIDTH - 300, 10, (255, 255, 255), BLOCK_FRICTION, self.world.map_group)

        Player(self.world, 10, 10, 1, self.world.player_group)

        for i in range(4):
            Enemy(self.world, 10, 50 * (i + 1), 1, self.world.enemy_group)
