import pygame
from scene import Scene
from scenes.level1 import Level1


class Intro(Scene):
    """
    Scène d'introduction du jeu.
    """

    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.background = pygame.image.load("assets/scenes/intro.png").convert()

    def update(self, elapsed: int) -> None:
        """
        Mets à jour la scène. Passe à la scène suivante si le joueur appuie sur espace.
        """
        super().update(elapsed)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            self.is_finished = True
            self.next_scene = Level1(self.screen)

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))
