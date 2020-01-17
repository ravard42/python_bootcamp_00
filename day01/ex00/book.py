import datetime
from recipe import Recipe


class Book:

    def __init__(self, name, recipes_list={
            "starter": [], "lunch": [], "dessert": []}):
        if not isinstance(name, str):
            print("Book __init__ error: name type must be str")
            raise Exception
        elif not name:
            print("Book __init__ error: you have to named your new book")
            raise Exception
        else:
            self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        if not isinstance(recipes_list, dict):
            print("Book __init__ error: recipes_list type must be dict")
            raise Exception
        if sorted([key for key in recipes_list.keys()]) != sorted(
                ["starter", "lunch", "dessert"]):
            print("Book __init__ error: recipes_list dict bad keys")
            raise Exception
        err_l = [val for val in recipes_list.values()
                 if not isinstance(val, list)]
        if len(err_l):
            print("Book __init__ error:"
                  "recipes_list dict values must be a list")
            raise Exception
        self.all = []
        for key in recipes_list:
            self.all += recipes_list[key]
        for r in self.all:
            if not isinstance(r, Recipe):
                print("Book __init__ error:"
                      "recipes_list dict values must be a list of Recipe type")
                raise Exception
        self.recipes_list = recipes_list
        print("Book initialiation OK!")

    def __str__(self):
        """Return the string to print with the book info"""
        txt = ""
        txt += "Book name : {}\n".format(self.name)
        txt += "Book creation_date : {}\n".format(self.creation_date)
        txt += "Book last_update : {}\n".format(self.last_update)
        for v in self.recipes_list.values():
            for r in v:
                txt += str(r)
        return txt

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for r in self.all:
            if r.name == name:
                print(r)
                return r
            else:
                print("the recipe " + name + " doesn't exist in your book")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in ['lunch', 'dessert', 'starter']:
            print("bad recype_type")
        else:
            for r in self.recipes_list[recipe_type]:
                print(r.name)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("error: you only can add Recipe type ...")
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            last_update = datetime.datetime.now()
