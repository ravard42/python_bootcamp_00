import sys
import string

def text_analyzer(s=""):
    
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    
    if s == "":
        s = input('enter a string to anayze: ')
    tab = [0, 0, 0, 0, 0]
    for c in s:
        tab[0] += 1
        if c.isalpha():
            if c.isupper():
                tab[1] += 1
            elif c.islower():
                tab[2] += 1
        elif c in string.punctuation:
            tab[3] += 1
        elif c.isspace():
            tab[4] += 1
    print("The text contains {} characters:\n- {} upper letters\n- {} lower letters\n- {} punctuation marks\n- {} spaces\n".format(tab[0], tab[1], tab[2], tab[3], tab[4]))


#if __name__ == '__main__':
#    if len(sys.argv) == 1:
#       text_analyzer()
#    elif len(sys.argv) == 2:
#       text_analyzer(sys.argv[1])
#    print(text_analyzer.__doc__)
    
