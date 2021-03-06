from bullet import *
from constants import *
from enemy import Enemy


class Scene:
    """
    Classe représentant une scène du jeu (niveau ou menu).
    Tous les niveaux et les menus sont des scènes et héritent de cette classe.

    Propriétés:
        scene_manager (SceneManager): Scene manager.
        elapsed (float): le temps écoulé depuis la dernière frame.

    Méthodes à implémenter pour les classes filles:
        update(self): met à jour la scène (appelée à chaque frame).
        draw(self): dessine la scène (appelée à chaque frame).
    """

    def __init__(self, scene_manager) -> None:
        self.scene_manager = scene_manager
        self.screen = scene_manager.screen
        self.elapsed = 0
        

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
        last_enemy_spawn (int): temps écoulé depuis le dernier ennemi apparu.

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

    def __init__(self, scene_manager) -> None:
        super().__init__(scene_manager)

        self.enemy_max = self.get_enemy_max()  # Nombre maximal d'ennemis simultanés
        self.enemy_list = self.get_enemy_list()  # Liste des ennemis à faire apparaitre
        self.last_enemy_spawn = ENEMY_SPAWN_DELAY  # Temps écoulé depuis le dernier ennemi apparu

        # Groupes de sprites
        self.enemy_group = pygame.sprite.Group()  # Groupes d'ennemis
        self.map_group = pygame.sprite.Group()  # Groupes de blocs
        self.player_group = pygame.sprite.Group()  # Groupes de joueurs
        self.bullet_group = pygame.sprite.Group()  # Groupes des balles
        self.particle_group = pygame.sprite.Group()  # Groupes des particules
        self.event_box_group = pygame.sprite.Group()  # Groupes des event_box
        self.door_group = pygame.sprite.Group()  # Ouverture des portes

        self.load_level()

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
        Passe au niveau suivant.

        """
        self.scene_manager.next_level()

    def game_over(self):
        """
        Passe au menu de fin de partie.

        Doit être implémenté dans les classes filles.
        """
        pass

    def draw_background(self):
        """
        Dessine le fond du niveau.

        Peut être modifié dans les classes filles.
        """
        self.screen.fill((50, 52, 67))

    def draw(self) -> None:
        self.draw_background()

        # Affichage des groupes de sprites
        self.map_group.draw(self.screen)
        self.event_box_group.draw(self.screen)
        self.particle_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)

        # Affichage de la barre de vie et de la barre de reload
        for player in self.player_group:
            player.show_health()
            player.show_reload()

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

        # Mise à jour du rechargement de l'arme du joueur
        for player in self.player_group:
            player.update_reload(elapsed)

        # Supression des éléments qui sont hors de l'écran
        self.remove_outbound_items()
        # Apparition des ennemis manquants
        self.last_enemy_spawn += elapsed
        self.spawn_missing_ennemy()

    def spawn_missing_ennemy(self):
        """
        Fait apparaitre un nouvel ennemi si il y en a un manquant,
        et termine le niveau si il n'y en a plus.
        """

        # Apparition des ennemis manquants
        missing_enemys = self.enemy_max - len(self.enemy_group)  # Nombre d'ennemis manquants à faire apparaitre
        enemy_list_size = len(self.enemy_list)  # Taille de la liste d'ennemis

        if min(missing_enemys, enemy_list_size) > 0 and self.last_enemy_spawn > ENEMY_SPAWN_DELAY:
            enemy = self.enemy_list.pop()
            enemy.spawn(self.enemy_group)
            self.last_enemy_spawn = 0

        # Si il n'y a plus d'ennemis à faire apparaitre, on termine le niveau
        if not self.enemy_list and not self.enemy_group:
            self.finish()

    def finish(self):
        """
        Termine le niveau. La porte est ouverte pour passer au niveau suivant.
        """
        for door in self.door_group:
            door.set_locked(False)

    def remove_outbound_items(self):
        """
        Supprime les particules et les ennemis qui sortent de l'écran.
        """

        # Suppression des particules
        for particle in self.particle_group:
            if particle.rect.x < -particle.rect.width or particle.rect.x > self.screen.get_width() or \
                particle.rect.y < -particle.rect.height or particle.rect.y > self.screen.get_height():
                self.particle_group.remove(particle)

        # Supression des ennemis
        for enemy in self.enemy_group:
            if enemy.rect.x < -enemy.rect.width or enemy.rect.x > self.screen.get_width() or \
                enemy.rect.y < -enemy.rect.height or enemy.rect.y > self.screen.get_height():
                enemy.die()


class EnemySpawner:
    """
    Classe représentant un ennemi qui n'est pas encore apparu.

    Paramètres:
        scene: la scene dans lequel se trouve l'ennemi
        x: la position en x de l'ennemi
        y: la position en y de l'ennemi
        image: l'image de l'ennemi
        mass: la masse de l'ennemi
        damages: les dégâts infligés lors d'un attaque
        max_health: la vie maximum de l'ennemi
    """

    def __init__(self, scene, x, y, image, mass, damages, max_health):
        self.scene = scene
        self.x = x
        self.y = y
        self.mass = mass
        self.image = image
        self.damages = damages
        self.max_health = max_health

    def spawn(self, groups):
        """
        Fait apparaitre l'ennemi dans un groupe de sprites.

        Paramètres:
            groups: les groupes de sprites dans lesquels l'ennemi doit apparaitre (tuple)
        """
        Enemy(self.scene, self.x, self.y, self.image, self.mass, self.damages, self.max_health, groups)
