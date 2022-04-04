from enum import auto
from enum import Enum

class Tile(Enum):
    EMPTY = auto()
    TILE1 = auto()
    TILE2 = auto()


    def __str__(self) -> str:
        """ Returns a string which represents the tile.
        """

        return self.name
