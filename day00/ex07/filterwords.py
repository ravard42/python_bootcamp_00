import sys
import string

if __name__ == '__main__':
    if (not len(sys.argv) == 3
        or not len([c for c in sys.argv[1] if c.isnumeric()]) == 0
        or not sys.argv[2].isnumeric()
    ):
        print("ERROR")
    else:
        newstr = ''.join([c for c in sys.argv[1] if not c in string.punctuation])
        print([x for x in newstr.split() if len(x) > int(sys.argv[2])])
