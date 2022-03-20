import pickle
import os

# Change the Tile path if you want.
from tile import Tile as Tile
from lib.matrix import Matrix


class MapEditor:

    def __init__(self):
        self.matrix = None
        os.system('cls||clear')
        while 1:
            try:
                answ = self.ask_question('Do you want to load an existing map? (y | n)')
                if answ == 'y': self.load()
                elif answ == 'n': self.create_new_map()
                else: raise AssertionError('invalid option')
                
                os.system('cls||clear')
                if self.matrix: break
            except Exception as error:
                print(f'Unexpected {error}. Try again \n')
                continue
        
        self.main()


    def main(self):
        while True:
            try:
                os.system('cls||clear')
                print("Type 'exit' to save and close the program \n")
                print(self.matrix , ' \n')
                axis = self.ask_question('Which axis of the map you want to modify? (x | y)')
                if axis != 'x' and axis != 'y': raise AssertionError("invalid option")
                line = int(self.ask_question('Wich row/column do you want to modify? (starting at 0)'))
                start = int(self.ask_question('From which position do you want to modify? (inclusive)'))
                end = int(self.ask_question('Until which position do you want to modify? (inclusive)'))
                print(f'Select the tile type to replace it with')
                tile = Tile(int(self.ask_question(self.list_to_str(self.get_list_of_tiles()))))
                self.modify_matrix(axis, line, start, end, tile)

            except Exception as error:
                print(f"Unexpected {error}. Try again \n")
                continue

    
    def create_new_map(self):
        rows = int(self.ask_question('Define the quantity of rows of your map:'))
        column = int(self.ask_question('Define the quantity of columns of your map:'))
        self.matrix = Matrix([[Tile.EMPTY for x in range(column)] for i in range(rows)])
        os.system('cls||clear')

    
    def ask_question(self, question):
        print(question)
        answ = input()
        print('')

        if answ == 'quit' or answ == 'exit' or answ == 'save': self.save()
        return answ


    def list_to_str(self, list):
        string = ''
        for element in list:
            string += str(element) + ', '
        string = string[:-2]
        return string


    def get_list_of_tiles(self):
        """ Returns the list of all the posible tiles and its numbers
        """
        
        return [f'{str(tile)} ({str(tile.value)})' for tile in Tile]

    
    def modify_matrix(self, axis, line, start, end, tile):
        if axis == 'x':
            for pos in range(start, end + 1): self.matrix.set_element((line, pos), tile)

        if axis == 'y':
            for pos in range(start, end + 1): self.matrix.set_element((pos, line), tile)


    def save(self):
        if self.matrix:
            name = self.ask_question('How do you want your map to be called?')
            if not os.path.exists('maps'):
                os.makedirs('maps')
            self.matrix.save_as_pickle(f'maps/{name}.pickle')
            print('Map saved!')
        
        exit()
        
    
    def load(self):
        if os.path.exists('maps'):
            with os.scandir('maps') as files:
                maps = [file for file in files if file.is_file() and file.name.endswith('.pickle')]
                if not maps: raise AssertionError('no maps created')
                
                print('List of existing maps:')
                for level in maps:
                    print('  -' + level.name[:-7])

                answ = self.ask_question(' \nWich map do you want to edit?') + '.pickle'
                path = next((level.path for level in maps if level.name == answ), None)
                if path:
                    with open(path, 'rb') as f:
                        self.matrix = Matrix(pickle.load(f))
                else:
                    raise AssertionError('path not found')

            os.system('cls||clear')
        else: raise AssertionError('no maps created')

      
MapEditor()  

