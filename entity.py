from enum import auto
from enum import IntEnum


class Entity(IntEnum):
    ENTITY1 = auto()
    ENTITY2 = auto()


    def __str__(self) -> str:
        """ Returns a string which represents the tile.
        """

        return self.name