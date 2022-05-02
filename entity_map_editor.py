#!/usr/bin/env python3

import os
from src.change_mode import ChangeMode
from src.map_editor import MapEditor
from src.references_file import Entity
from src.references_file import Tile

class EntityMapEditor(MapEditor):

    def __init__(self):
        super().__init__()
        self.entity_map = dict()
        self.path = str()
        self.tile_map = None
        self.modes = ['Points', 'Lines', 'Fill']
        os.system('cls||clear')
        while 1:
            try:
                tile_map_path = self.select_tile_map()
                self.tile_map = self.load_tile_map(tile_map_path)
                self.entity_map, self.path = self.load_entity_map(tile_map_path)
                os.system('cls||clear')
                if self.tile_map: break
            except ChangeMode: continue
            except AssertionError as error:
                print(f'Unexpected {error}.')
                exit()
            except Exception as error:
                print(f'Unexpected {error}. Try again \n')
                continue
        
        self.main()


    def main(self):
        os.system('cls||clear')
        while 1:
            try:
                print("Type 'exit' to save and close the program \n")
                print(self.dict_to_matrix(self.entity_map, self.tile_map), ' \n')
                if self.mode == 0: self.edit_by_points()
                elif self.mode == 1: self.edit_by_lines()
                elif self.mode == 2: self.edit_by_fill()
                else: AssertionError("invalid option")

            except ChangeMode: continue
            except Exception as error:
                print(f"Unexpected {error}. Try again \n")
                continue


    def edit_by_lines(self):
        axis = self.ask_question('Which axis of the map you want to modify? (x | y)')
        if axis != 'x' and axis != 'y': raise AssertionError("invalid option")
        line = int(self.ask_question('Wich row/column do you want to modify? (starting at 0)'))
        start = int(self.ask_question('From which position do you want to modify? (inclusive)'))
        end = int(self.ask_question('Until which position do you want to modify? (inclusive)'))
        print(f'Select the entity type to replace it with:')
        entities = self.get_list_of_elements(Entity)
        entities.append(f"Remove ({len(entities)+1})")
        entity = int(self.ask_question(self.list_to_str(entities)))
        
        if entity == len(entities):
            for pos in range(start, end + 1): 
                if axis == 'x': self.entity_map.pop((line, pos), None)
                elif axis == 'y': self.entity_map.pop((pos, line), None)
            
        else:
            if axis == 'x':
                for pos in range(start, end + 1): 
                    self.tile_map.get_element((line, pos))  # Validate the position.
                    self.entity_map[(line, pos)] = Entity(entity)

            elif axis == 'y':
                for pos in range(start, end + 1): 
                    self.tile_map.get_element((pos, line))  # Validate the position.
                    self.entity_map[(pos, line)] = Entity(entity)

        os.system('cls||clear')


    def edit_by_points(self):
        row = int(self.ask_question('In which row do you want to add an entity?'))
        column = int(self.ask_question('In which column do you want to add an entity?'))
        self.tile_map.get_element((row,column))  # Validate the position.
        print(f'Select the entity type to replace it with:')
        entities = self.get_list_of_elements(Entity)
        entities.append(f"Remove ({len(entities)+1})")
        entity = int(self.ask_question(self.list_to_str(entities)))
        
        if entity == len(entities): self.entity_map.pop((row, column), None)
        else: self.entity_map[(row, column)] = Entity(entity)
        os.system('cls||clear')

    def edit_by_fill(self):
        print(f'Select the tile type to fill:')
        tile = Tile(int(self.ask_question(self.list_to_str(self.get_list_of_elements(Tile)))))
        print(f'Select the entity type to replace it with:')
        entities = self.get_list_of_elements(Entity)
        entities.append(f"Remove ({len(entities)+1})")
        entity = int(self.ask_question(self.list_to_str(entities)))
        for row in range(self.tile_map.length()[0]):
            for column in range (self.tile_map.length()[1]):
                element = self.tile_map.get_element((row,column))
                if element == tile:
                    if entity == len(entities):
                        self.entity_map.pop((row,column), None)
                    else:
                        self.entity_map[(row,column)] = Entity(entity)


    def save(self):
        if self.entity_map: 
            self.save_map(self.entity_map, self.path)
        else: 
            self.delete_file(self.path)
        exit()


EntityMapEditor()  

