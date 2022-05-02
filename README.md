# Map Editor

This is a tool created specifically to create and edit the mazes of our game [GOFM](https://github.com/ArcosJuan/Get-out-of-my-fucking-maze) but I created trying to make it as generic as posible so that is reusable.

## How to use it
To create a map it is important to first create the tile_map, then the entity_map and finally the character_map in that order. Also keep in mind that if you delete or change an entity with the entity_map_editor without removing it in the character_map it can cause problems.


### Saving:
To start the saving process of the map being edited, type __save__ at any time. Once you decide on a map name it will be stored in the [maps folder](maps/) as a .pickle file. 

The tile-map will contain a list of lists (in the form of a matrix) with the enum of tiles in each position, the entity-map will contain a dictionary with positional indexes as key and the enum entities as value, and the character-map will contain a dictionary with positional indexes as key and the name of the characters as value.

### Modes:
Some editors have different editing modes that can be more useful for certain tasks, such as the fill mode of the entity map editor. To switch between these modes type __mode__ in any time.

## First time configuration
By changing the imports made in [references.py](src/references.py), you can modify the location of any of the assets needed to run the program and the file extension of your maps. 

To run the tile-map editor, [Tile](example_assets/tile.py) must be an Enum with all the tiles of your map, making sure the first element is EMPTY.

To run the entity-map editor you also need [Entity](example_assets/entity.py), this sould be an Enum similar to Tile but unlike the previous one, this one doesn't need an EMPTY element.

Finally to run the character-map editor in addition to the previous two you will also need a [Characters](example_assets/characters.json) file, this is a .json with the name of your character as a key and anything else as value.


### IMPORTANT ADVICE:
For the correct operation of the maps when importing them from an external program, the reference structure that was used when creating them with the editor must be maintained. This implies that the references of the tiles and entities are in src/references. This location can be modified by the user without major complications.


## License

_map-editor as a whole is licensed under the MIT License - Look the [LICENSE](LICENSE) file for details._


