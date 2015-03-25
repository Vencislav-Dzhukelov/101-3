import sys
from random import randint


def gen_num():
    filename = sys.argv[1]
    file = open(filename, "w+")
    for i in range(int(sys.argv[2])):
        number = randint(1, 1000)
        file.write(str(number) + " ")


if __name__ == '__main__':
    print (gen_num())
