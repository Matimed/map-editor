# Map Editor

This is a tool created specifically to create and edit the mazes of our game [GOFM](https://github.com/ArcosJuan/Get-out-of-my-fucking-maze) but I created trying to make it as generic as posible so that is reusable.

## How to use it

Edit or replace the _tile.py_ file with an intEnum of all the tiles of your map making sure the first element is EMPTY.

To execute the tile-map editor: 
_$ python3 map-editor.py_

When you're done, your map will be saved as a .pickle file that will contain a list of lists that represent it in the maps folder.

## License

_map-editor as a whole is licensed under the MIT License - Look the [LICENSE](LICENSE) file for details._


