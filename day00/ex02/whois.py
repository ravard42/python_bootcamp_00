import sys

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isalnum():
        x = int(sys.argv[1])
        if x == 0:
            print("I'm Zero.")
        elif x % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
        
