
 
class ChangeMode(Exception):
    def __init__(self, msg = "The mode change."):
        super().__init__(msg)