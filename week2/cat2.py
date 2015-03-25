import sys


def read_files():
    result = ""
    if len(sys.argv[1]) > 1:
        for i in range(1, len(sys.argv)):
            filename = sys.argv[i]
            text_file = open(filename, "r")
            text = text_file.read()
            text_file.close()
            result = result + text + "\n"
        return result
    else:
        print ("Enter file name:")


if __name__ == '__main__':
    print (read_files())
