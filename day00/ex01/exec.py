import sys

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        tot = ''
        for i in sys.argv[1::]:
            tot += i + ' '
        tot = tot[:-1]
        ret = ''
        for c in tot:
            if c.isalpha() and c.isupper():
                ret += c.lower()
            elif c.isalpha() and c.islower():
                ret += c.upper()
            else:
                ret += c
        print(ret[::-1])
