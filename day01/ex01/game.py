class GotCharacter:

    def __init__(self, first_name=None, is_alive=True):
        if not isinstance(first_name, str):
            print("GotCharacter __init__ error: name type must be str")
            raise Exception
        elif not first_name:
            print("Book __init__ error: you have to named your new character")
            raise Exception
        else:
            self.first_name = first_name
        self.is_alive = True
        print("GotCharacter __init__ succeed")
    
    def __repr__(self):
        return "first_name : {}, is_alive : {}, ".format(self.first_name, self.is_alive)


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good
people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
        print("Stark __init__ succeed")

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
    
    def __repr__(self):
        return super().__repr__() + "family_name : {}, house_words : {} ".format(self.family_name, self.house_words)
