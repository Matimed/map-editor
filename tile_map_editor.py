#!/usr/bin/env python3

import pickle
import os
from lib.matrix import Matrix
from src.map_editor import MapEditor

# Change the Tile path if you want.
from src.references import Tile


class TileMapEditor(MapEditor):

    def __init__(self):
        self.tile_map = None
        os.system('cls||clear')
        while 1:
            try:
                answ = self.ask_question('Do you want to load an existing tile map? (y | n)')
                if answ == 'y': self.tile_map = self.load_tile_map(self.search_tile_map())
                elif answ == 'n': self.create_new_map()
                else: raise AssertionError('invalid option')
                
                os.system('cls||clear')
                if self.tile_map: break
            except Exception as error:
                print(f'Unexpected {error}. Try again \n')
                continue
        
        self.main()


    def main(self):
        while True:
            try:
                print("Type 'exit' to save and close the program \n")
                print(self.tile_map , ' \n')
                axis = self.ask_question('Which axis of the map you want to modify? (x | y)')
                if axis != 'x' and axis != 'y': raise AssertionError("invalid option")
                line = int(self.ask_question('Wich row/column do you want to modify? (starting at 0)'))
                start = int(self.ask_question('From which position do you want to modify? (inclusive)'))
                end = int(self.ask_question('Until which position do you want to modify? (inclusive)'))
                print(f'Select the tile type to replace it with:')
                tile = Tile(int(self.ask_question(self.list_to_str(self.get_list_of_elements(Tile)))))
                self.modify_tile_map(axis, line, start, end, tile)
                os.system('cls||clear')

            except Exception as error:
                print(f"Unexpected {error}. Try again \n")
                continue

    
    def create_new_map(self):
        rows = int(self.ask_question('Define the quantity of rows of your map:'))
        column = int(self.ask_question('Define the quantity of columns of your map:'))
        self.tile_map = Matrix([[Tile.EMPTY for x in range(column)] for i in range(rows)])
        os.system('cls||clear')
    
    
    def modify_tile_map(self, axis, line, start, end, tile):
        if axis == 'x':
            for pos in range(start, end + 1): self.tile_map.set_element((line, pos), tile)

        if axis == 'y':
            for pos in range(start, end + 1): self.tile_map.set_element((pos, line), tile)


    def save(self):
        if self.tile_map:
            name = self.ask_question('How do you want your map to be called?')
            if not os.path.exists('maps'):
                os.makedirs('maps')

            if os.path.exists(f'maps/{name}.tiles.pickle'):
                answ = self.ask_question('The map already exists, do you want to replace it? (y | n)')
                if answ != 'y': return
            self.tile_map.save_as_pickle(f'maps/{name}.tiles.pickle')
            print('Map saved!')
        
        exit()

      
TileMapEditor()  

