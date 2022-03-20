# Map Editor

This is a tool created specifically to create and edit the mazes of our game [GOFM](https://github.com/ArcosJuan/Get-out-of-my-fucking-maze) but I created trying to make it as generic as posible so that is reusable.

## How to use it

### Tile-map editor:

Edit or replace the [tile.py](src/tile.py) file with an intEnum of all the tiles of your map making sure the first element is EMPTY.

To execute the tile-map editor: 
_$ python3 tile_map_editor.py_

When you're done, your tile-map will be saved as a .pickle file that will contain a list of lists that represent it in the maps folder.

### Entity-map editor:

To use the entity-map editor it is necessary to have at least one tile-map in the maps folder.
Similar to the tile-map editor, you should edit or replace the [entity.py](src/entity.py) with an enum of all your entities, but unlike the previous one, this one doesn't need an EMPTY element.

Once we meet these requirements, to run the editor:
_$ python3 entity_map_editor.py_

The entity-map will be stored as a .pickle file that will contain a dictionary with positional indexes as key and the enum entities as value. 


## License

_map-editor as a whole is licensed under the MIT License - Look the [LICENSE](LICENSE) file for details._


