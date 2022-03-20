

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
        
        return [f'{str(element)} ({str(element.value)})' for element in enum]


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


    def save(self):
        """ Saves de map in a .pickle file in the maps folder. 
        """

        raise NotImplementedError


    def load(self):
        """ Loads a .pickle file from the maps folder 
            to edit the map it contains. 
        """

        raise NotImplementedError
