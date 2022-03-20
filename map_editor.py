import pickle
import os
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
    def get_list_of_elements(enum):
        """ Returns the list of all the elements 
            of a given enum and its values.
        """
        
        return [f'{str(element.name)} ({str(element.value)})' for element in enum]


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

        if path:
            with open(path, 'rb') as f:
                return Matrix(pickle.load(f))
        else:
            raise AssertionError('path not found')

    def save(self):
        """ Saves de map in a .pickle file in the maps folder. 
        """

        raise NotImplementedError