from typing import NamedTuple, Optional

import pygame

# rgba range: 0-255
RGBA = NamedTuple('rgba', [('r', int), ('g', int), ('b', int), ('a', int)])
MouseClickPos = NamedTuple('mouse_click_position', [('x', int), ('y', int)])


# Todo: implement this function
def game_logic(screen: pygame.Surface) -> Optional[MouseClickPos]:
    """This is where the game logic will be implemented."""
    p = RGBA(*screen.get_at((0, 0)))  # get pixel color at (0, 0)
    print(p.r, p.g, p.b, p.a)
    return MouseClickPos(0, 0)
