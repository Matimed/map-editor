import pickle
import os
from src.map_editor import MapEditor

# Change the Entity path if you want.
from src.references import Entity


class EntityMapEditor(MapEditor):

    def __init__(self):
        self.entity_map = dict()
        self.path = str()
        self.tile_map = None
        os.system('cls||clear')
        while 1:
            try:
                tile_map_path = self.search_tile_map()
                self.tile_map = self.load_tile_map(tile_map_path)
                self.load_entity_map(tile_map_path)
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
        while True:
            try:
                print("Type 'exit' to save and close the program \n")
                print(self.tile_map , ' \n')
                print(self.list_to_str(self.dict_to_list(self.entity_map)), ' \n')

                row = int(self.ask_question('In which row do you want to add an entity? (starting at 0)'))
                column = int(self.ask_question('In which column do you want to add an entity? (starting at 0)'))
                self.tile_map.get_element((row,column))  # Validate the position.
                print(f'Select the entity type to replace it with:')
                entity = Entity(int(self.ask_question(self.list_to_str(self.get_list_of_elements(Entity)))))
                self.entity_map[(row, column)] = entity
                os.system('cls||clear')

            except Exception as error:
                print(f"Unexpected {error}. Try again \n")
                continue


    def save(self):
        if self.entity_map:

            with open(self.path, 'wb') as file:
                pickle.dump(self.entity_map, file, protocol=pickle.HIGHEST_PROTOCOL)
            print('Map saved!')
        
        exit()
        
    
    def load_entity_map(self, tile_map_path):
        self.path = tile_map_path.replace('tiles', 'entities')
        if os.path.exists(self.path):
            with open(self.path, 'rb') as f:
                self.entity_map = pickle.load(f)

      
EntityMapEditor()  

