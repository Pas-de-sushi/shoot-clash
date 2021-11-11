from scenes.end import GameOver, Victory
from scenes.intro import Intro
from scenes.level1 import Level1


class SceneManager:
    """
    Stocke et initialise les scenes

    Propriétés:
        screen (pygame.Surface): Surface de la fenêtre de jeu.
    """

    def __init__(self, screen) -> None:
        self.screen = screen

        self.scene_map = {"intro": Intro, "game_over": GameOver, "victory": Victory, "level1": Level1}
        self.levels_order = ["intro", "level1", "victory"]

        self.current_level_index = 0
        self.current_scene_id = self.levels_order[self.current_level_index]
        self.current_scene = Intro(self)

    def load_scene(self, scene_id):
        """
        Charge une scene
        """
        self.current_scene_id = scene_id
        self.current_scene = self.scene_map[self.current_scene_id](self)

    def load_level(self, level_index):
        """
        Passe a un niveau specifique (par index)
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
        self.current_level_index = (self.current_level_index + 1) % len(self.levels_order)
        self.load_scene(self.levels_order[self.current_level_index])

    def update(self, elapsed):
        """
        Met à jour la scène active (appelée à chaque frame).
        elapsed (float): le temps écoulé depuis la dernière frame.
        """

        self.current_scene.update(elapsed)

    def draw(self):
        """
        Dessine la scène active (appelée à chaque frame).
        """
        self.current_scene.draw()
