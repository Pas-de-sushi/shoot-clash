from random import randint

from block import Block
from bullet import Weapon
from constants import *
from door import Door
from player import Player
from scene import EnemySpawner, Level


class Level2(Level):
    def load_level(self) -> None:
        # Bordures du niveau
        Block(
            0,
            0,
            SCREEN_WIDTH,
            10,
            (255, 255, 255),
            self.map_group,
        )
        Block(
            0,
            SCREEN_HEIGHT - 10,
            SCREEN_WIDTH,
            10,
            (255, 255, 255),
            self.map_group,
        )
        Block(
            0,
            10,
            50,
            SCREEN_HEIGHT - 10,
            (255, 255, 255),
            self.map_group,
        )
        Block(
            SCREEN_WIDTH - 50,
            10,
            50,
            SCREEN_HEIGHT - 10,
            (255, 255, 255),
            self.map_group,
        )

        # Plateformes
        Block(
            SCREEN_WIDTH - 500,
            SCREEN_HEIGHT - 100,
            500,
            100,
            (255, 255, 255),
            self.map_group,
        )
        Block(
            0,
            SCREEN_HEIGHT - 170,
            SCREEN_WIDTH - 600,
            15,
            (255, 255, 255),
            self.map_group,
        )
        Block(
            SCREEN_WIDTH - 430,
            SCREEN_HEIGHT - 220,
            75,
            10,
            (255, 255, 255),
            self.map_group,
        )
        Block(
            SCREEN_WIDTH - 250,
            SCREEN_HEIGHT - 270,
            250,
            10,
            (255, 255, 255),
            self.map_group,
        )

        # Portes
        Door(
            self,
            SCREEN_WIDTH - 100,
            SCREEN_HEIGHT - 320,
            50,
            50,
            (self.event_box_group, self.door_group)
        )

        w2 = Weapon(cadence=300, recoil=0.5, damage=30)
        Player(self, 80, SCREEN_HEIGHT - 50, 1, self.player_group, weapon=w2)

    def get_enemy_list(self):
        enemy_list = []

        for i in range(5):
            enemy_list.append(
                EnemySpawner(self, SCREEN_WIDTH - 200, randint(50, 150), 1, 30)
            )
            enemy_list.append(
                EnemySpawner(self, 50, randint(50, 150), 1, 30)
            )

        return enemy_list

    def get_enemy_max(self):
        return 3
