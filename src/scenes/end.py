import pygame
from scene import Scene


class GameOver(Scene):
    """
    Scène de fin de jeu.
    """

    def __init__(self, scene_manager) -> None:
        super().__init__(scene_manager)
        self.background = pygame.image.load("assets/scenes/game-over.png").convert()

    def update(self, elapsed: int) -> None:
        """
        Mets à jour la scène. Recommence le jeu si le joueur appuie sur espace.
        """
        super().update(elapsed)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            self.scene_manager.load_level_by_name("intro")

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))


class Victory(Scene):
    """
    Scène de victoire.
    """

    def __init__(self, scene_manager) -> None:
        super().__init__(scene_manager)
        self.background = pygame.image.load("assets/scenes/victory.png").convert()

    def update(self, elapsed: int) -> None:
        """
        Mets à jour la scène. Recommence le jeu si le joueur appuie sur espace.
        """
        super().update(elapsed)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            self.scene_manager.load_level_by_name("intro")

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))
