import pygame

from level import Level


class World:
    """
    Classe represente le monde
    Est passé aux objets
    """

    def __init__(self, screen):
        self.screen = screen

        self.enemy_group = pygame.sprite.Group()
        self.map_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.particle_group = pygame.sprite.Group()
        self.event_box_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()  # sert pour ouverture des portes

        self.level = Level(self)
        self.elapsed = 0

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.map_group.draw(self.screen)
        self.particle_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.event_box_group.draw(self.screen)

    def update(self, elapsed):
        self.elapsed = elapsed
        self.particle_group.update()
        self.enemy_group.update()
        self.bullet_group.update()
        self.player_group.update()
        self.event_box_group.update()
