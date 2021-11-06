import pygame

from level import Level


class World:
    """
    Classe représentant le "monde" du jeu.

    Elle stocke différents données importantes :


    Une instance de cette classe est initialisée au démarrage
    et est passée à de nombreux objets.
    """

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        # Groupes de sprites
        self.enemy_group = pygame.sprite.Group()
        self.map_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.particle_group = pygame.sprite.Group()
        self.event_box_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()  # Ouverture des portes

        self.level = Level(self)   # Initialisation du niveau
        self.elapsed = 0  # Temps depuis la dernière image

    def draw(self):
        """
        Affiche les élements du jeu à l'écran.
        """
        self.screen.fill((0, 0, 0))  # On remplit l'écran de noir

        # Affichage des groupes de sprites
        self.map_group.draw(self.screen)
        self.particle_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.event_box_group.draw(self.screen)

        # Affichage de la barre de vie du joueur
        for player in self.player_group:
            player.show_health()

    def update(self, elapsed: int):
        """
        Mise à jour de tous les éléments du jeu (déplacements, physique, etc.)
        """
        self.elapsed = elapsed

        self.particle_group.update()
        self.enemy_group.update()
        self.bullet_group.update()
        self.player_group.update()
        self.event_box_group.update()
