from block import Block
from constants import *
from door import Door
from enemy import Enemy
from player import Player
from bullet import *


class Level:
    """
    Classe stockant les informations sur un niveau
    """

    def __init__(self, world) -> None:
        self.world = world
        self.enemy_list = [0, 0, 0, 0, 0, 0, 0, 0,
                           0]  # Liste avec le type et stats enemis qui doivent spawn TODO: Faire vraiment
        self.enemy_max = 5  # enemis max en meme temps # TODO: suivant leurs type certains types valent 2 ou plus
        self.is_finished = False  # plus d'ennemis, portes ouvertes
        self.load_level()

    def load_level(self) -> None:
        """
        Initialisation du niveau.

        - Création des blocs
        - Création du personnage
        - Création des ennemis
        """
        Block(
            0,
            0,
            SCREEN_WIDTH,
            10,
            (255, 255, 255),
            self.world.map_group,
        )
        Block(
            0,
            SCREEN_HEIGHT - 10,
            SCREEN_WIDTH,
            10,
            (255, 255, 255),
            self.world.map_group,
        )
        Block(
            0,
            10,
            10,
            SCREEN_HEIGHT - 10,
            (255, 255, 255),
            self.world.map_group,
        )
        Block(
            SCREEN_WIDTH - 100,
            10,
            100,
            SCREEN_HEIGHT - 10,
            (255, 255, 255),
            self.world.map_group,
        )
        Block(
            0,
            SCREEN_HEIGHT - 200,
            SCREEN_WIDTH - 300,
            10,
            (255, 255, 255),
            self.world.map_group,
        )
        Door(
            self.world,
            30,
            SCREEN_HEIGHT - 60,
            50,
            50,
            (self.world.event_box_group, self.world.door_group)
        )

        w1 = Weapon(cadence=1500, recoil=3, damage=100)
        w2 = Weapon(500, 0.5, 12)
        Player(self.world, 10, 10, 1, self.world.player_group, weapon=w1)

        self.spawn_enemys()

    def on_enemy_death(self):
        """
        Est appelé lorsqu'un ennemi meurt
        puis
        - Fait spawner un nouvel ennemis si besoin
        - appel la fonction finish() si il ne reste plus d'ennemis (niveau terminé)
        (appelé directement par les ennemis)

        """
        self.spawn_enemys()
        if not self.enemy_list and not self.world.enemy_group:  # On vérifie si il n'y a plus d'ennemis
            self.finish()

    def spawn_enemys(self):
        """
        Fait apparaitre les ennemis en fonction la liste enemy_list
        Fait apparaitre le maximum d'ennemis tout en respectant le nombre d'ennemis max simultanés
        """
        # Nombre d'ennemis manquants à faire apparaitre
        missing_enemys = self.enemy_max - len(self.world.enemy_group)
        # Taille de la liste d'ennemis
        enemy_list_size = len(self.enemy_list)
        # Nombre d'ennemis à faire apparaitre
        spawn_enemys = min(missing_enemys, enemy_list_size)

        # Fait apparaitre les ennemis
        for i in range(spawn_enemys):
            Enemy(self.world, 10, 50 * (i + 1), 1, 20, self.world.enemy_group)
            self.enemy_list.pop()

    def finish(self):
        self.is_finished = True
        for door in self.world.door_group:
            door.set_locked(False)

    def player_access_door(self):
        pass  # Niveau terminé
