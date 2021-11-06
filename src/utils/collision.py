import pygame


def check_collision(
    map_group: pygame.sprite.Group,
    old_rect: pygame.rect,
    new_rect: pygame.rect,
    right_callback,
    left_callback,
    top_callback,
    bottom_callback,
) -> pygame.rect:
    """
    Gestion des collisions. La position du sprite est modifiée en fonction de la collision.

    Paramètres:
    - map_group: groupe de sprites représentant la carte
    - old_rect: ancienne position du sprite
    - new_rect: nouvelle position voulue du sprite
    - right_callback: fonction à exécuter quand le sprite va vers la droite
    - left_callback: fonction à exécuter quand le sprite va vers la gauche
    - top_callback: fonction à exécuter quand le sprite va vers le haut
    - bottom_callback: fonction à exécuter quand le sprite va vers le bas

    Retourne la position du sprite après la collision.
    """

    corrected_rect = new_rect  # Position du sprite après la collision

    for block in map_group:  # Collision avec les blocs du groupe
        if new_rect.colliderect(block) and new_rect != block:
            if (new_rect.x + new_rect.width > block.rect.x) and (
                old_rect.x + old_rect.width <= block.rect.x
            ):
                corrected_rect.x = (
                    block.rect.x - new_rect.width - 1
                )  # le 1 desactive la collision (perf)
                right_callback(block)

            if (new_rect.x < block.rect.x + block.rect.width) and (
                old_rect.x >= block.rect.x + block.rect.width
            ):
                corrected_rect.x = block.rect.x + block.rect.width + 1
                left_callback(block)

            if (new_rect.y < block.rect.y + block.rect.height) and (
                old_rect.y >= block.rect.y + block.rect.height
            ):
                corrected_rect.y = block.rect.y + new_rect.height + 1

                top_callback(block)
            if (new_rect.y + new_rect.height > block.rect.y) and (
                old_rect.y + old_rect.height <= block.rect.y
            ):
                corrected_rect.y = block.rect.y - new_rect.height

                bottom_callback(block)

    return corrected_rect
