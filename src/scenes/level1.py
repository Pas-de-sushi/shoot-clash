import random

import pygame

from block import Block
from bullet import Weapon
from constants import *
from door import Door
from player import Player
from scene import EnemySpawner, Level


class Level1(Level):
    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.background = pygame.image.load(
            "assets/level1/background.png").convert()

    def load_level(self) -> None:
        # Murs du niveau
        Block(
            256,
            0,
            "assets/level1/wall1.png",
            self.map_group,
        )
        Block(
            0,
            384,
            "assets/level1/wall2.png",
            self.map_group,
        )
        Block(
            0,
            448,
            "assets/level1/wall3.png",
            self.map_group,
        )
        Block(
            64,
            640,
            "assets/level1/wall4.png",
            self.map_group,
        )
        Block(
            1024,
            0,
            "assets/level1/wall5.png",
            self.map_group,
        )
        Block(
            320,
            0,
            "assets/level1/wall6.png",
            self.map_group,
        )

        # Plateformes
        Block(
            832,
            192,
            "assets/level1/platform1.png",
            self.map_group,
        )
        Block(
            640,
            480,
            "assets/level1/platform2.png",
            self.map_group,
        )
        Block(
            320,
            320,
            "assets/level1/platform3.png",
            self.map_group,
        )

        # Porte
        Door(
            self,
            856,
            96,
            (self.event_box_group, self.door_group)
        )

        w1 = Weapon(cadence=1500, recoil=3, damage=100)
        Player(self, 140, 470, 1, self.player_group, weapon=w1)

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def get_enemy_list(self):
        enemy_list = []

        for i in range(10):
            enemy_list.append(
                EnemySpawner(self, random.randint(380, 450), random.randint(
                    80, 200), "assets/enemy/pig.png", 1, 20, 100)
            )
            enemy_list.append(
                EnemySpawner(self, random.randint(380, 450), random.randint(
                    80, 200), "assets/enemy/crab.png", 1, 30, 200)
            )

        for i in range(3):
            enemy_list.append(
                EnemySpawner(self, random.randint(380, 450), random.randint(
                    80, 200), "assets/enemy/cucumber.png", 1, 40, 100)
            )
            enemy_list.append(
                EnemySpawner(self, random.randint(380, 450), random.randint(
                    80, 200), "assets/enemy/dude.png", 1, 70, 300)
            )

        random.shuffle(enemy_list)
        return enemy_list

    def get_enemy_max(self):
        return 3

    def next_level(self):
        self.is_finished = True
        self.next_scene = self
