import json
import os
import pickle
from lib.matrix import Matrix


class MapEditor:

    @staticmethod
    def list_to_str(list):
        """ Receives a list and returns a human-readable string of elements.
        """

        string = ''
        for element in list:
            string += str(element) + ', '
        string = string[:-2]
        return string

    
    @staticmethod
    def number_list(list):
        return [f'{list[i]} ({i})' for i in range(len(list))] 


    @staticmethod
    def dict_to_list(dict):
        """ Receives a dict and returns a matrix of elements.
        """

        matrix = Matrix()
        for key in sorted(dict.keys()):
            matrix.append_row([key, dict[key]])

        return matrix


    @staticmethod
    def dict_to_matrix(dict, matrix):
        """ Receives a dict and returns a matrix of elements.
        """

        new_matrix = matrix.copy()
        for element in dict:
            new_matrix.set_element(element, dict[element])

        return new_matrix


    @staticmethod
    def get_list_of_elements(enum):
        """ Returns the list of all the elements 
            of a given enum and its values.
        """
        
        return [f'{str(element.name)} ({str(element.value)})' for element in enum]


    @staticmethod
    def open_json(path):
        with open(path, 'r') as json_file: return json.load(json_file)


    def ask_question(self, question: str):
        """ Receives a question, asks it to the user and returns his answer.
            Also catches the user's exit attempts 
            and redirects them to the save method.
        """

        print(question)
        answ = input()
        print('')

        if answ == 'quit' or answ == 'exit' or answ == 'save': self.save()
        return answ


    def search_tile_map(self):
        """ Asks the user to choose a tile-map
            from the folder and returns its path.
        """

        if os.path.exists('maps'):
            with os.scandir('maps') as files:
                maps = [file for file in files if file.is_file() and file.name.endswith('.tiles.pickle')]
                if not maps: raise AssertionError('no maps created')
                
                print('List of existing maps:')
                for tile_map in maps:
                    print('  -' + tile_map.name[:-13])

                answ = self.ask_question(' \nWich map do you want to edit?') + '.tiles.pickle'
                os.system('cls||clear')
                return next((tile_map.path for tile_map in maps if tile_map.name == answ), None)

        else: raise AssertionError('no tile-maps created')


    def load_tile_map(self, path):
        """ Recieves a tile-map path and 
            returns a Matrix object with its content. 
        """

        return Matrix(self._load_map(path))


    def load_entity_map(self, tile_map_path):
        path = tile_map_path.replace('tiles', 'entities')
        try: return self._load_map(path), path
        except: return dict(), path


    def load_character_map(self, tile_map_path):
        path = tile_map_path.replace('tiles', 'characters')
        try: return self._load_map(path), path
        except: return dict(), path


    def _load_map(self, path):
        if path and os.path.exists(path):
            with open(path, 'rb') as f:
                return pickle.load(f)
        else:
            raise AssertionError('path not found')


    def save(self):
        """ Saves de map in a .pickle file in the maps folder. 
        """

        raise NotImplementedError

    
    def save_map(self, map, path):
        with open(path, 'wb') as file:
            pickle.dump(map, file, protocol=pickle.HIGHEST_PROTOCOL)
        print('Map saved!')
        