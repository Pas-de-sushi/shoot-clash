import pygame
from scene import Scene


class Intro(Scene):
    """
    Scène d'introduction du jeu.
    """

    def __init__(self, scene_manager) -> None:
        super().__init__(scene_manager)
        self.background = pygame.image.load("assets/scenes/intro.png").convert()
        self.last_keys_state = pygame.key.get_pressed()

    def update(self, elapsed: int) -> None:
        """
        Mets à jour la scène. Passe à la scène suivante si le joueur appuie sur espace.
        """
        super().update(elapsed)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE] and not self.last_keys_state[pygame.K_SPACE]:
            self.scene_manager.next_level()
        self.last_keys_state = pressed_keys

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))
