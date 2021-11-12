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
        if pressed_keys[pygame.K_RIGHT] and not self.last_keys_state[pygame.K_RIGHT]:
            self.scene_manager.selected_weapon_index = (
                self.scene_manager.selected_weapon_index + 1) % len(self.scene_manager.weapon_list)
        if pressed_keys[pygame.K_LEFT] and not self.last_keys_state[pygame.K_LEFT]:
            self.scene_manager.selected_weapon_index = (
                self.scene_manager.selected_weapon_index - 1) % len(self.scene_manager.weapon_list)
        self.last_keys_state = pressed_keys

    def draw(self) -> None:
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.scene_manager.weapon_list[self.scene_manager.selected_weapon_index].image,
                         ((535 - self.scene_manager.weapon_list[self.scene_manager.selected_weapon_index].image.get_width() / 2),
                          429 - self.scene_manager.weapon_list[self.scene_manager.selected_weapon_index].image.get_height() / 2))
