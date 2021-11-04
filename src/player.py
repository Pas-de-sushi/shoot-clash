import pygame

from bullet import Bullet
from model.entity import Entity
from utils.map_collision import check_map_collision
from utils.vector import Vector


class Player(Entity):
    """
    Classe qui represente le joueur
    """

    def __init__(self, world, x, y, mass, groups: tuple) -> None:
        self.image = pygame.Surface([10, 15])
        self.image.fill((0, 255, 0))
        super(Player, self).__init__(world, x, y, mass, 100, groups)

        self.jump_count = 0
        self.max_jump = 1
        self._old_jump_state = False  # Detection relachement

        self.shoot_time = 0
        self.shoot_delay = 100  # une balle sec

    def update(self):
        self.check_input()
        super().update()

    def check_input(self):
        """
        Controles du joueur
        """
        pressed_keys = pygame.key.get_pressed()
        move = Vector(0, 0)
        if pressed_keys[pygame.K_LEFT]:
            move.x -= 1
            self.direction = False
        if pressed_keys[pygame.K_RIGHT]:
            move.x += 1
            self.direction = True

        if pressed_keys[pygame.K_UP]:
            if not self._old_jump_state:  # Attend relachement de la touche
                self._old_jump_state = True
                if self.jump_count < self.max_jump:
                    move.y -= 10
                    self.jump_count += 1

        else:
            self._old_jump_state = False

        if self.shoot_time >= self.shoot_delay:
            if pressed_keys[pygame.K_SPACE]:
                self.shoot()
                self.shoot_time = 0
        else:
            self.shoot_time += self.world.elapsed

        self.velocity += move

    def shoot(self):
        bullet = Bullet(
            self.world,
            self.rect.x,
            self.rect.y,
            Vector(self.velocity.x + (15 if self.direction else -15), 0),
            (self.world.bullet_group),
        )
        self.velocity = self.velocity + (bullet.velocity * (-0.5)) * (
                bullet.mass / self.mass
        )
        # coef 0,5 de recul|Recul du joueur TODO: Suivant type arme ?

    def handle_collision(self, old_rect):
        self.rect = check_map_collision(
            self.world.map_group,
            old_rect,
            self.rect,
            self.right,
            self.left,
            self.top,
            self.bottom,
        )

    def right(self, block):
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = False

    def left(self, block):
        self.velocity.x *= -1
        self.velocity *= block.friction
        self.direction = True

    def top(self, block):
        self.velocity.y = 0

    def bottom(self, block):
        self.velocity.y *= -0.25
        self.velocity *= block.friction
        self.jump_count = 0
