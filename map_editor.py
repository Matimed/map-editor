import os

# Change the Tile path if you want.
from tile import Tile as Tile
from lib.matrix import Matrix


class MapEditor:

    def __init__(self):
        self.matrix = None
        os.system('cls||clear')

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

        return answ


    def list_to_str(self, list):
        string = ''
        for element in list:
            string += str(element) + ', '
        string = string[:-2]
        return string


    def modify_matrix(self, axis, line, start, end, tile):
        if axis == 'x':
            for pos in range(start, end + 1): self.matrix.set_element((line, pos), tile)

        if axis == 'y':
            for pos in range(start, end + 1): self.matrix.set_element((pos, line), tile)


      
MapEditor()  

