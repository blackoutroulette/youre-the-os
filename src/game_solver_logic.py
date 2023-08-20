from typing import NamedTuple, Optional

import pygame

# rgba range: 0-255
RGBA = NamedTuple('RGBA', [('r', int), ('g', int), ('b', int), ('a', int)])
MouseClickPos = NamedTuple('MouseClickPos', [('x', int), ('y', int)])


# Todo: implement this function
def game_logic(screen: pygame.Surface) -> Optional[MouseClickPos]:
    """This is where the game logic will be implemented."""
    p = RGBA(*screen.get_at((0, 0)))  # get pixel color at (0, 0)
    height = screen.get_height()  # get screen height
    width = screen.get_width()  # get screen width
    print(p.r, p.g, p.b, p.a)
    print(height, width)
    return MouseClickPos(0, 0)
