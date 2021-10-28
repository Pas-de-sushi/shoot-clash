import pygame


def check_map_collision(map_group: pygame.sprite.Group, old_rect: pygame.rect, new_rect: pygame.rect, right_callback,
                        left_callback, top_callback,
                        bottom_callback) -> pygame.rect:
    """
    Corrige la position avec la collision

    :param map_group: groupe pygame de la carte
    :param old_rect: position actuelle
    :param new_rect: position voulue
    :param right_callback: callback quand droite touché
    :param left_callback: callback quand gauche touché
    :param top_callback: callback quand haut touché
    :param bottom_callback: callback quand bas touché

    :return: rect : Position corrigée

    """

    corrected_rect = new_rect
    for block in map_group:
        if new_rect.colliderect(block) and new_rect != block:

            if (new_rect.x + new_rect.width > block.rect.x) and (old_rect.x + old_rect.width <= block.rect.x):
                corrected_rect.x = block.rect.x - new_rect.width - 1  # le 1 desactive la collision (perf)
                right_callback(block)

            if (new_rect.x < block.rect.x + block.rect.width) and (old_rect.x >= block.rect.x + block.rect.width):
                corrected_rect.x = block.rect.x + block.rect.width + 1
                left_callback(block)

            if (new_rect.y < block.rect.y + block.rect.height) and (
                    old_rect.y >= block.rect.y + block.rect.height):
                corrected_rect.y = block.rect.y + new_rect.height + 1

                top_callback(block)
            if (new_rect.y + new_rect.height > block.rect.y) and (old_rect.y + old_rect.height <= block.rect.y):
                corrected_rect.y = block.rect.y - new_rect.height - 1

                bottom_callback(block)

    return corrected_rect
