from block import Block
from bullet import Weapon
from constants import *
from door import Door
from player import Player
from scene import EnemySpawner, Level
from scenes.level2 import Level2


class Level1(Level):
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
            10,
            SCREEN_HEIGHT - 10,
            (255, 255, 255),
            self.map_group,
        )
        Block(
            SCREEN_WIDTH - 100,
            10,
            100,
            SCREEN_HEIGHT - 10,
            (255, 255, 255),
            self.map_group,
        )

        # Plateformes
        Block(
            0,
            SCREEN_HEIGHT - 200,
            SCREEN_WIDTH - 300,
            20,
            (255, 255, 255),
            self.map_group,
        )

        # Porte
        Door(
            self,
            30,
            SCREEN_HEIGHT - 60,
            50,
            50,
            (self.event_box_group, self.door_group)
        )

        w1 = Weapon(cadence=1500, recoil=3, damage=100)
        Player(self, 10, 10, 1, self.player_group, weapon=w1)

    def get_enemy_list(self):
        enemy_list = []

        for i in range(10):
            enemy_list.append(
                EnemySpawner(self, 10, 50 * (i + 1), 1, 20)
            )

        return enemy_list

    def get_enemy_max(self):
        return 5

    def next_level(self):
        self.is_finished = True
        self.next_scene = Level2(self.screen)
