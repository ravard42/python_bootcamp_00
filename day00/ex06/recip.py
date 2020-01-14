cookbook = {'sandwich' : {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'], 'meal' : 'lunch', 'prep_time' : 10},
               'cake' : {'ingredients' : ['lour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : 60},
               'salad' : {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal' : 'lunch', 'prep_time' : 15}
               }

def add_recipe(name):
    ing = []
    buff = ""
    while not buff == 'ok':
        buff = input("add ingredient ('ok' when the ingredient list is complete)\n")
        ing.append(buff)
    ing.pop()
    meal = input('type of meal?\n')
    prep_time = ""
    while not prep_time.isnumeric():
        print("you must enter a number\n")
        prep_time = input('prep_time?\n')
    prep_time = int(prep_time)
    cookbook[name] = {'ingredients' : ing, 'meal' : meal, 'prep_time' : prep_time}


def del_recipe(name):
    if name in cookbook.keys():
        del cookbook[name]
    else:
        print('unknown recipe name {}\n'.format(name))

def print_recipe(name):
    
    if name in cookbook.keys():
        print('Recipe for {}:'.format(name))
        print("Ingredients list: {}".format(cookbook[name]['ingredients']))
        print('To be eaten for {}'.format(cookbook[name]['meal']))
        print('Takes {} minutes of cooking\n'.format(cookbook[name]['prep_time']))
    else:
        print('unknown recipe name {}\n'.format(name))

def print_all(cookbook):
    print("coobook content:\n")
    for key in cookbook.keys():
        print_recipe(key)
    

if __name__ == '__main__':


    i = -1
    while not i == 5:
        
        i = input('\nPlease select an option by typing the corresponding number:\n'
            + '1: Add a recipe\n'
            + '2: Delete a recipe\n'
            + '3: Print a recipe\n'
            + '4: Print the cookbook\n'
            + '5: Quit\n')
        if not i.isnumeric():
            print("you must enter a number\n")
            continue
        i = int(i)
        print("")
        if i == 1:
            add_recipe(input("Please enter the recipe's name you want to add:\n\n"))
        elif i == 2:
            del_recipe(input("Please enter the recipe's name you want to delete:\n\n"))
        elif i == 3:
            print_recipe(input("Please enter the recipe's name to get its details:\n\n"))
        elif i == 4:
            print_all(cookbook)
        elif i == 5:
            print('Cookbook closed.\n')
        else:
            print('This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n')

    
