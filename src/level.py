from block import Block
from constants import *
from door import Door
from enemy import Enemy
from player import Player


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
        Block(
            0,
            0,
            SCREEN_WIDTH,
            10,
            (255, 255, 255),
            self.world.map_group,
            BLOCK_FRICTION,
        )
        Block(
            0,
            SCREEN_HEIGHT - 10,
            SCREEN_WIDTH,
            10,
            (255, 255, 255),
            self.world.map_group,
            BLOCK_FRICTION,
        )
        Block(
            0,
            10,
            10,
            SCREEN_HEIGHT - 10,
            (255, 255, 255),
            self.world.map_group,
            BLOCK_FRICTION,
        )
        Block(
            SCREEN_WIDTH - 100,
            10,
            100,
            SCREEN_HEIGHT - 10,
            (255, 255, 255),
            self.world.map_group,
            BLOCK_FRICTION,
        )  # Droite
        Block(
            0,
            SCREEN_HEIGHT - 200,
            SCREEN_WIDTH - 300,
            10,
            (255, 255, 255),
            self.world.map_group,
            BLOCK_FRICTION,
        )
        Door(
            self.world,
            30,
            SCREEN_HEIGHT - 60,
            50,
            50,
            (self.world.event_box_group)
        )
        Player(self.world, 10, 10, 1, self.world.player_group)

        for i in range(4):
            Enemy(self.world, 10, 50 * (i + 1), 1, self.world.enemy_group)
