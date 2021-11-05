import pygame


class Block(pygame.sprite.Sprite):
    """
    Block de decors
    friction: vitesse joueur multiplié par celui-ci lorsqu'il marche dessus
    """

    def __init__(
            self, x, y, width, height, color, groups: tuple, friction=0.7,
    ):  # TODO : probleme valeur par defaut ne marche pas avec groups
        super().__init__(groups)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)

        self.friction = friction
