from recipe import Recipe
from book import Book

if __name__ == '__main__':

    ## Recipe tests

    try:
        r = Recipe(-42, 1, 20, ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], 'lunch', "full fromage")
    except:
        pass
    try:
        r = Recipe("", 1, 20, ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], 'lunch', "full fromage")
    except:
        pass
    try:
        r = Recipe("Croc monsieur", "str", 20, ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], 'lunch', "full fromage")
    except:
        pass
    try:
        r = Recipe("Croc monsieur", 42, 20, ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], 'lunch', "full fromage")
    except:
        pass
    try:
        r = Recipe("Croc monsieur", 1, "str", ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], 'lunch', "full fromage")
    except:
        pass
    try:
        r = Recipe("Croc monsieur", 1, -42, ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], 'lunch', "full fromage")
    except:
        pass
    try:
        r = Recipe("Croc monsieur", 1, 20, 0, 'lunch', "full fromage")
    except:
        pass
    try:
        r = Recipe("Croc monsieur", 1, 20, ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], -42, "full fromage")
    except:
        pass
    try:
        r = Recipe("Croc monsieur", 1, 20, ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], 'petit dejeuner', "full fromage")
    except:
        pass

    print()
    try:
        r_l = Recipe("Croc monsieur", 1, 20, ['pain de mie', 'creme fraiche', 'gruyere', 'jambon'], 'lunch', "full fromage")
        print(r_l)
    except:
        pass
    try:
        r_s = Recipe("Saumon citronnee", 1, 5, ['saumon', 'citron'], 'starter', 'pour noel')
        print(r_s)
    except:
        pass
    try:
        r_d = Recipe("bananne flambee vannille choco", 2, 10, ['banane', 'rhum', 'glace vanille', 'neskwik'], 'dessert', "")
        print(r_d)
    except:
        pass
   
    

    ## Book tests

    try:
        b = Book(42, {'starter' : [r_s], 'lunch' : [r_l], 'dessert' : [r_d]})
    except:
        pass
    try:
        b = Book("", {'starter' : [r_s], 'lunch' : [r_l], 'dessert' : [r_d]})
    except:
        pass
    try:
        b = Book("food tips", 42)
    except:
        pass
    try:
        b = Book("food tips", {'BAD' : [], 'lunch' : [r_l], 'dessert' : [r_d]})
    except:
        pass
    try:
        b = Book("food tips", {'starter' : 42, 'lunch' : [r_l], 'dessert' : [r_d]})
    except:
        pass
    try:
        b = Book("food tips", {'starter' : [42], 'lunch' : [r_l], 'dessert' : [r_d]})
    except:
        pass

    print()

    try:
        b = Book("food tips", {'starter' : [r_s], 'lunch' : [r_l], 'dessert' : [r_d]})
        print(b)
    except:
        pass
