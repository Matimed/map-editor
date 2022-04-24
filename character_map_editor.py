#!/usr/bin/env python3

import os
from src.map_editor import MapEditor


class CharacterMapEditor(MapEditor):

    def __init__(self):
        self.characters = [name for name in self.open_json('src/references/characters.json')] 
        self.entity_map = dict()
        self.path = str()
        self.tile_map = None
        self.character_map = None
        os.system('cls||clear')
        while 1:
            try:
                tile_map_path = self.search_tile_map()
                self.tile_map = self.load_tile_map(tile_map_path)
                self.entity_map, path = self.load_entity_map(tile_map_path)
                self.character_map, self.path = self.load_character_map(tile_map_path)
                for key in self.character_map:
                    self.entity_map[key] = self.character_map[key]
                os.system('cls||clear')
                if self.tile_map: break
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

                print(self.tile_map , ' \n')
                print(self.dict_to_list(self.entity_map), ' \n')
                row = int(self.ask_question('In which row is the entity you want to assign? (starting at 0)'))
                column = int(self.ask_question('In which column is the entity you want to assign? (starting at 0)'))
                self.entity_map[(row,column)]  # Validate the position.
                print(f'Select the character you are going to replace with:')
                character = int(self.ask_question(self.list_to_str(self.number_list(self.characters))))
                self.entity_map[(row, column)] = self.characters[character]
                self.character_map[(row, column)] = self.characters[character]
                os.system('cls||clear')

            except Exception as error:
                print(f"Unexpected {error}. Try again \n")
                continue


    def save(self):
        if self.character_map: self.save_map(self.character_map, self.path)
        exit()
        
    


      
CharacterMapEditor()  

