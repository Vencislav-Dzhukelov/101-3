import sys


def read_file():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        text_file = open(filename, "r")
        text = text_file.read()
        text_file.close()
        return text
    else:
        print ("Enter file name:")


if __name__ == '__main__':
    print (read_file())
