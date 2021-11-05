import pygame


class Block(pygame.sprite.Sprite):
    """
    Bloc du décors

    Propriétés:
    - x, y: position du bloc
    - width, height: taille du bloc
    - color: couleur du bloc
    - friction: coeficient de friction (multiplication de la vitesse du joueur)
    """

    def __init__(
            self, x, y, width, height, color, groups: tuple, friction=0.7,
    ):
        super().__init__(groups)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)

        self.friction = friction
