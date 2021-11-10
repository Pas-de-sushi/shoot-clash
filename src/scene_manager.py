from scenes.end import GameOver, Victory
from scenes.intro import Intro
from scenes.level1 import Level1


class SceneManager:
    """
    Stocke et initialise les scenes
    """

    def __init__(self, screen) -> None:
        self.screen = screen

        self.scene_map = {"intro": Intro, "game_over": GameOver, "victory": Victory, "level1": Level1}
        self.levels_order = ["intro", "level1", "victory"]

        self.current_level_index = 0
        self.current_scene_id = self.levels_order[self.current_level_index]
        self.current_scene = Intro(self)

    def load_scene(self, scene_id):
        self.current_scene_id = scene_id
        self.current_scene = self.scene_map[self.current_scene_id](self)

    def load_level(self, level_index):
        self.current_level_index = level_index
        self.load_scene(self.levels_order[level_index])

    def load_level_by_name(self, level_name):
        self.current_level_index = self.levels_order.index(level_name)
        self.load_scene(level_name)

    def next_level(self):
        self.current_level_index = (self.current_level_index + 1) % len(self.levels_order)
        self.load_scene(self.levels_order[self.current_level_index])

    def update(self, elapsed):
        self.current_scene.update(elapsed)

    def draw(self):
        self.current_scene.draw()
