from enum import auto
from enum import IntEnum


class Tile(IntEnum):
    EMPTY = auto()
    TILE1 = auto()
    TILE2 = auto()


    def __str__(self) -> str:
        """ Returns a string which represents the tile.
        """

        return self.name
