class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description=""):
        if not isinstance(name, str):
            print("Recipe __init__ error: name type must be str")
            raise Exception
        elif not name:
            print("Recipe __init__ error: Recipe name can't be empty")
            raise Exception
        else:
            self.name = name

        if not isinstance(cooking_lvl, int):
            print("Recipe __init__ error:"
                  "cooking_lvl type must be int")
            raise Exception
        elif int(cooking_lvl) not in range(1, 6):
            print("Recipe __init__ error:"
                  "cooking_lvl must be an int in range 1 to 5")
            raise Exception
        else:
            self.cooking_lvl = cooking_lvl
        if not isinstance(cooking_time, int):
            print("Recipe __init__ error: cooking_time type must be int")
            raise Exception
        elif int(cooking_time) < 0:
            print("Recipe __init__ error: cooking_time must be positive")
            raise Exception
        else:
            self.cooking_time = cooking_time
        if not isinstance(ingredients, list):
            print("Recipe __init__ error: ingredients type must be list")
            raise Exception
        elif not ingredients:
            print("Recipe __init__ error: ingredients is empty")
            raise Exception
        elif len([ing for ing in ingredients if isinstance(ing, str)])\
                != len(ingredients):
            print("Recipe __init__ error:"
                  "elem in ingredients list must be str")
            raise Exception
        else:
            self.ingredients = ingredients
        if not isinstance(recipe_type, str):
            print("Recipe __init__ error: recipe_type type must be str")
            raise Exception
        elif recipe_type != "starter" and\
                recipe_type != "lunch" and\
                recipe_type != "dessert":
            print("Recipe __init__ error:"
                  "recipe type must be one of 'starter', 'lunch' or 'dessert'")
            raise Exception
        else:
            self.recipe_type = recipe_type
        if not isinstance(description, str):
            print("Recipe __init__ error: description type must be str")
            raise Exception
        else:
            self.description = description
        print("Recipe initialiation OK!")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "Recipe name : {}\n".format(self.name)
        txt += "Recipe cooking_lvl : {}\n".format(self.cooking_lvl)
        txt += "Recipe cooking_time : {}\n".format(self.cooking_time)
        txt += "Recipe ingredients : {}\n".format(self.ingredients)
        txt += "Recipe recipe_type : {}\n".format(self.recipe_type)
        txt += "Recipe description : {}\n".format(self.description)
        return txt
