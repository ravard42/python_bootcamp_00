import sys
import string

def op(a, b):
    """This function compute the five basic operations (+, -, x, :, %) on its 2 int input args"""
    tab = [0, 0, 0, 0, 0]
    tab[0] = a + b
    tab[1] = a - b
    tab[2] = a * b
    if b == 0:
        tab[3] = "ERROR (div by zero)"
    else:
        tab[3] = a / b
    if b == 0:
        tab[4] = "ERROR (modulo by zero)"
    else:
        tab[4] = a % b
    print("Sum: {}\nDiff: {}\nProduct: {}\nQuotient: {}\nReminder: {}".format(tab[0], tab[1], tab[2], tab[3], tab[4]))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: python operations.py [operands]\nexample:\n\tpython operations.py 10 3")
    elif not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
        print("InputError: only number")
    else:
        op(int(sys.argv[1]), int(sys.argv[2]))
    
