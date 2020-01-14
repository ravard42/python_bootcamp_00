import sys
import string

atom = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    ' ' : '/'
}

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("usage: python sos.py [alphanum str to morse translate]")
        sys.exit(0)
    newstr = " ".join([arg for arg in sys.argv[1:]])
    if not ''.join([c for c in newstr if not c.isspace()]).isalnum():
        print("only alphanumeric pls")
    else:
        print(' '.join([atom[c.upper()] for c in newstr]))


