from constants import *
from enemy import Enemy
from bullet import *

class Scene:
    """
    Classe représentant une scène du jeu (niveau ou menu).
    Tous les niveaux et les menus sont des scènes et héritent de cette classe.

    Propriétés:
        screen (pygame.Surface): Surface de la fenêtre de jeu.
        elapsed (float): le temps écoulé depuis la dernière frame.
        is_finished (bool): indique si la scène est terminée.
        next_scene (Scene): la scène suivante (à affiché si la scène est terminée).

    Méthodes à implémenter pour les classes filles:
        update(self): met à jour la scène (appelée à chaque frame).
        draw(self): dessine la scène (appelée à chaque frame).
    """

    def __init__(self, screen) -> None:
        self.screen = screen
        self.elapsed = 0
        self.is_finished = False
        self.next_scene = None

    def update(self, elapsed: int) -> None:
        """
        Met à jour la scène (appelée à chaque frame).
        """
        self.elapsed = elapsed

    def draw(self) -> None:
        """
        Dessine la scène (appelée à chaque frame).
        """
        pass


class Level(Scene):
    """
    Scène représentant un niveau.

    Propriétés:
        enemy_list (list EnemySpawner): liste des ennemis qui doivent apparaitre.
        enemy_max (int): nombre d'ennemis maximum simultanés.

        enemy_group (pygame.sprite.Group): groupe d'ennemis.
        map_group (pygame.sprite.Group): groupe de blocs.
        player_group (pygame.sprite.Group): groupe de joueurs.
        bullet_group (pygame.sprite.Group): groupe de balles.
        particle_group (pygame.sprite.Group): groupe de particules.
        event_box_group (pygame.sprite.Group): groupe de event_box.
        door_group (pygame.sprite.Group): groupe de portes.

    Méthodes à implémenter pour les classes filles:
        load_level(self): initialisation du niveau (création des blocs, personnage, ennemis, etc.).
        get_ennemy_list(self): retourne la liste des ennemis qui doivent apparaitre.
        get_enemy_max(self): retourne le nombre d'ennemis maximum simultanés.
    """

    def __init__(self, screen) -> None:
        super().__init__(screen)

        self.enemy_max = self.get_enemy_max()  # Nombre maximal d'ennemis simultanés
        self.enemy_list = self.get_enemy_list()  # Liste des ennemis à faire apparaitre

        # Groupes de sprites
        self.enemy_group = pygame.sprite.Group()  # Groupes d'ennemis
        self.map_group = pygame.sprite.Group()  # Groupes de blocs
        self.player_group = pygame.sprite.Group()  # Groupes de joueurs
        self.bullet_group = pygame.sprite.Group()  # Groupes des balles
        self.particle_group = pygame.sprite.Group()  # Groupes des particules
        self.event_box_group = pygame.sprite.Group()  # Groupes des event_box
        self.door_group = pygame.sprite.Group()  # Ouverture des portes

        self.load_level()
        self.on_enemy_death()  # Déclanche l'apparition initiale des ennemis

    def load_level(self) -> None:
        """
        Initialisation du niveau (création des blocs, personnage, ennemis, etc.).

        Doit être implémenté dans les classes filles.
        """
        pass

    def get_enemy_list(self):
        """
        Retourne la liste des ennemis qui doivent apparaitre (EnemySpawner).
        Les ennemis doivent être dans un groupe unique pour chaque.

        Doit être implémenté dans les classes filles.
        """
        pass

    def get_enemy_max(self):
        """
        Retourne le nombre d'ennemis maximum simultanés.

        Doit être implémenté dans les classes filles.
        """
        return 5

    def next_level(self):
        """"
        Passe au niveau suivant. Définir la scène suivante.

        Doit être implémenté dans les classes filles.
        """
        pass

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))  # On remplit l'écran de noir

        # Affichage des groupes de sprites
        self.map_group.draw(self.screen)
        self.event_box_group.draw(self.screen)
        self.particle_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.bullet_group.draw(self.screen)

        # Affichage de la barre de vie du joueur
        for player in self.player_group:
            player.show_health()

    def update(self, elapsed: int):
        """
        Mise à jour de tous les éléments du jeu (déplacements, physique, etc.)
        """
        super().update(elapsed)

        self.particle_group.update()
        self.enemy_group.update()
        self.bullet_group.update()
        self.player_group.update()
        self.event_box_group.update()

    def on_enemy_death(self):
        """
        Fonctionne appelée lorsqu'un ennemi est tué.

        Elle fait apparaitre un nouvel ennemi si il y en a un manquant,
        et termine le niveau si il n'y en a plus.
        """

        # Apparition des ennemis manquants
        missing_enemys = self.enemy_max - len(self.enemy_group)  # Nombre d'ennemis manquants à faire apparaitre
        enemy_list_size = len(self.enemy_list)  # Taille de la liste d'ennemis

        for i in range(min(missing_enemys, enemy_list_size)):
            enemy = self.enemy_list.pop()
            enemy.spawn(self.enemy_group)

        # Si il n'y a plus d'ennemis à faire apparaitre, on termine le niveau
        if not self.enemy_list and not self.enemy_group:
            self.finish()

    def finish(self):
        """
        Termine le niveau. La porte est ouverte pour passer au niveau suivant.
        """
        for door in self.door_group:
            door.set_locked(False)

class EnemySpawner:
    """
    Classe représentant un ennemi qui n'est pas encore apparu.

    Paramètres:
        scene: la scene dans lequel se trouve l'ennemi
        x: la position en x de l'ennemi
        y: la position en y de l'ennemi
        mass: la masse de l'ennemi
        damages: les dégâts infligés lors d'un attaque
    """

    def __init__(self, scene, x, y, mass, damages):
        self.scene = scene
        self.x = x
        self.y = y
        self.mass = mass
        self.damages = damages

    def spawn(self, groups):
        """
        Fait apparaitre l'ennemi dans un groupe de sprites.

        Paramètres:
            groups: les groupes de sprites dans lesquels l'ennemi doit apparaitre (tuple)
        """
        Enemy(self.scene, self.x, self.y, self.mass, self.damages, groups)