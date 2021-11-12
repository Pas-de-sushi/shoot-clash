import pygame
from bullet import Weapon
from scenes.end import GameOver, Victory
from scenes.intro import Intro
from scenes.level1 import Level1


class SceneManager:
    """
    Gestion des scènes et stockage de l'état de l'arme.

    Paramètres:
        screen (pygame.Surface): Surface de la fenêtre de jeu.

    Propriétés:
        - scene_map (dict): Dictionnaire de toutes les scènes.
        - level_order (list): Liste des niveaux dans l'ordre d'affichage.
        - current_level_index (int): Index du niveau actuel.
        - current_scene_id (str): ID de la scène actuelle.
        - current_scene (Scene): Scène actuelle.
        - weapon_list (list): Liste des armes disponibles.
        - selected_weapon_index (int): Index de l'arme sélectionnée.
    """

    def __init__(self, screen) -> None:
        self.screen = screen

        self.scene_map = {
            "intro": Intro,
            "game_over": GameOver,
            "victory": Victory,
            "level1": Level1
        }
        self.levels_order = ["intro", "level1", "victory"]

        self.current_level_index = 0
        self.current_scene_id = self.levels_order[self.current_level_index]
        self.current_scene = Intro(self)

        pistol_image = pygame.image.load("assets/guns/pistol.png").convert_alpha()
        assault_image = pygame.image.load("assets/guns/assault_riffle.png").convert_alpha()

        pistol_weapon = Weapon(pistol_image, cadence=700, recoil=3, damage=100, reload_count=2, reload_time=700)
        assault_weapon = Weapon(assault_image, cadence=100, recoil=1, damage=20, reload_count=20, reload_time=200)

        self.weapon_list = [assault_weapon, pistol_weapon]
        self.selected_weapon_index = 0

    def load_scene(self, scene_id):
        """
        Charge une scene avec un identifiant donné.
        """
        self.current_scene_id = scene_id
        self.current_scene = self.scene_map[self.current_scene_id](self)

    def load_level(self, level_index):
        """
        Passe a un niveau specifique à partir de son index.
        """
        self.current_level_index = level_index
        self.load_scene(self.levels_order[level_index])

    def load_level_by_name(self, level_name):
        """
        Passe a un niveau specifique (par nom)
        """
        self.current_level_index = self.levels_order.index(level_name)
        self.load_scene(level_name)

    def next_level(self):
        """
        Passe au niveau suivant
        """
        self.current_level_index = (
            self.current_level_index + 1) % len(self.levels_order)
        self.load_scene(self.levels_order[self.current_level_index])

    def update(self, elapsed):
        """
        Met à jour la scène active (appelée à chaque frame).

        Paramètres:
        - elapsed (float): le temps écoulé depuis la dernière frame.
        """

        self.current_scene.update(elapsed)

    def draw(self):
        """
        Dessine la scène active (appelée à chaque frame).
        """
        self.current_scene.draw()

    def get_selected_weapon(self):
        return self.weapon_list[self.selected_weapon_index]
