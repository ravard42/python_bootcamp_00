import datetime

class Book:
    def __init__(self, name, recipes_list, last_update = datetime.datetime.now(), creation_date = datetime.datetime.now()):
        if not isinstance(name, str):
            print("Book __init__ error: name type must be str")
            raise Exception
        elif not name:
            print("Book __init__ error: Book name can't be empty")
            raise Exception
        else:
            self.name = name
        if not isinstance(recipes_list, dict):
            print("Book __init__ error: recipes_list type must be dict")
            raise Exception
        else:
            self.recipes_list = recipes_list
        if not isinstance(last_update, datetime):
            print("Book __init__ error: last_update type must be datetime")
            raise Exception
        else:
            self.creation_date = creation_date
        if not isinstance(creation_date, datetime):
            print("Book __init__ error: creation_date type must be datetime")
            raise Exception
        else:
            self.creation_date = creation_date

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "Book name : {}\n".format(self.name)
        txt += "Book recipes_list : {}\n".format(self.recipes_list)
        txt += "Book last_update : {}\n".format(self.last_update)
        txt += "Book creation_date : {}\n".format(self.creation_date)
        return txt
