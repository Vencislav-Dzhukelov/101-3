import sys


def sum_int():
    filename = sys.argv[1]
    result = 0
    numbers = []
    file = open(filename, "r")
    numbers = file.read()
    numbers = numbers.split(' ')
    for i in range(len(numbers)-1):
        result = result + int(numbers[i])
    return result


if __name__ == '__main__':
    print (sum_int())
