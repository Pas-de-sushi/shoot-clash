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
        self.enemy_list = [0, 0, 0, 0, 0, 0, 0, 0,
                           0]  # Liste avec le type et stats enemis qui doivent spawn TODO: Faire vraiment
        self.enemy_max = 5  # enemis max en meme temps # TODO: suivant leurs type certains types valent 2 ou plus
        self.is_finished = False  # plus d'ennemis, portes ouvertes
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
            (self.world.event_box_group, self.world.door_group)
        )
        Player(self.world, 10, 10, 1, self.world.player_group)

        self.spawn_enemys()

    def on_enemy_death(self):
        self.spawn_enemys()
        if not self.enemy_list:  # check list empty : https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
            if not self.world.enemy_group:  # Plus d'ennemis
                self.finish()

    def spawn_enemys(self):
        enemy_spawn_list_lenght = len(self.enemy_list)
        should_spawn_count = self.enemy_max - len(self.world.enemy_group)  # Nb Ennemis manquants
        final_spawn_count = (
            enemy_spawn_list_lenght if enemy_spawn_list_lenght < should_spawn_count else should_spawn_count)
        # Limite si il n'y a plus d'elements
        for i in range(final_spawn_count):
            Enemy(self.world, 10, 50 * (i + 1), 1, self.world.enemy_group)
            self.enemy_list.pop()

    def finish(self):
        self.is_finished = True
        for door in self.world.door_group:
            door.set_locked(False)

    def player_access_door(self):
        pass  # Next Level
