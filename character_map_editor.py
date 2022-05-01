#!/usr/bin/env python3

import os
from src.change_mode import ChangeMode
from src.map_editor import MapEditor

# Change the paths if you want.
from src.references import Entity
CHARACTERS_PATH = 'src/references/characters.json'
CHARACTER_ENTITIES = [Entity.ENTITY1]

class CharacterMapEditor(MapEditor):    

    def __init__(self):
        super().__init__()
        self.characters = [name for name in self.open_json(CHARACTERS_PATH)] 
        self.entity_map = dict()
        self.path = str()
        self.tile_map = None
        self.character_map = None
        self.modes = ['Points']
        os.system('cls||clear')
        while 1:
            try:
                tile_map_path = self.select_tile_map()
                self.tile_map = self.load_tile_map(tile_map_path)
                self.entity_map, path = self.load_entity_map(tile_map_path)
                self.character_map, self.path = self.load_character_map(tile_map_path)
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
                entity_matrix = self.dict_to_matrix(self.entity_map, self.tile_map)
                print(self.dict_to_matrix(self.character_map, entity_matrix), ' \n')
                if self.mode == 0: self.edit_by_points()
                else: AssertionError("invalid option")

            except ChangeMode: continue
            except Exception as error:
                print(f"Unexpected {error}. Try again \n")
                continue



    def edit_by_points(self):
        row = int(self.ask_question('In which row is the entity you want to assign?'))
        column = int(self.ask_question('In which column is the entity you want to assign?'))
        self.entity_map[(row,column)]  # Validate the position.
        print(f'Select the character you are going to replace with:')
        
        characters = self.number_list(self.characters)
        characters.append(f"Remove ({len(characters)})")
        character = int(self.ask_question(self.list_to_str(characters)))
        
        if character == len(characters)-1:
            self.character_map.pop((row, column), None)
        else:
            if self.entity_map[(row, column)] in CHARACTER_ENTITIES:
                self.character_map[(row, column)] = self.characters[character]
            else: raise AssertionError('invalid entity for characters')
        
        os.system('cls||clear')

    def save(self):
        if self.character_map: 
            self.save_map(self.entity_map, self.path)
        else: self.delete_file(self.path)
        exit()

      
CharacterMapEditor()  

