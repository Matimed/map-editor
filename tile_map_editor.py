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
                if answ == 'y': self.tile_map = self.load_tile_map(self.select_tile_map())
                elif answ == 'n': self.create_new_map()
                else: raise AssertionError('invalid option')
                
                os.system('cls||clear')
                if self.tile_map: break
            except Exception as error:
                print(f'Unexpected {error}. Try again \n')
                continue
        
        self.main()


    def main(self):
        while 1: 
            try:
                mode = self.ask_question('Select an editing mode (1: Lines | 2: Rects)')
                if mode != '1' and mode != '2': AssertionError("invalid option")
                else: break
            except Exception as error:
                print(f'Unexpected {error}. Try again \n')
                continue

        os.system('cls||clear')
        while 1:
            try:
                print("Type 'exit' to save and close the program \n")
                print(self.tile_map , ' \n')
                if mode == '1': self.edit_by_lines()
                elif mode == '2': self.edit_by_rectangules()
                else: AssertionError("invalid option")

            except Exception as error:
                print(f"Unexpected {error}. Try again \n")
                continue


    def edit_by_lines(self):
        axis = self.ask_question('Which axis of the map you want to modify? (x | y)')
        if axis != 'x' and axis != 'y': raise AssertionError("invalid option")
        line = int(self.ask_question('Wich row/column do you want to modify? (starting at 0)'))
        start = int(self.ask_question('From which position do you want to modify? (inclusive)'))
        end = int(self.ask_question('Until which position do you want to modify? (inclusive)'))
        print(f'Select the tile type to replace it with:')
        tile = Tile(int(self.ask_question(self.list_to_str(self.get_list_of_elements(Tile)))))
        if axis == 'x':
            for pos in range(start, end + 1): self.tile_map.set_element((line, pos), tile)

        if axis == 'y':
            for pos in range(start, end + 1): self.tile_map.set_element((pos, line), tile)

    def edit_by_rectangules(self):
        row = int(self.ask_question('In which row is the first position? (starting at 0)'))
        column = int(self.ask_question('In which column is the first position? (starting at 0)'))
        start_point = (row,column)
        self.tile_map.get_element(start_point)  # Validate the position.
        row = int(self.ask_question('In which row is the last position? (starting at 0)'))
        column = int(self.ask_question('In which column is the last position? (starting at 0)'))
        end_point = (row,column)
        self.tile_map.get_element(end_point)  # Validate the position.
        print(f'Select the tile type to replace it with:')
        tile = Tile(int(self.ask_question(self.list_to_str(self.get_list_of_elements(Tile)))))
        
        for row in range(start_point[0], end_point[0]+1):
            for column in range(start_point[1], end_point[1]+1):
                self.tile_map.set_element((row, column), tile)
    
    def create_new_map(self):
        rows = int(self.ask_question('Define the quantity of rows of your map:'))
        column = int(self.ask_question('Define the quantity of columns of your map:'))
        self.tile_map = Matrix([[Tile.EMPTY for x in range(column)] for i in range(rows)])
        os.system('cls||clear')
    
    def save(self):
        if self.tile_map:
            try:
                self.search_tile_map()
            except:
                pass
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

