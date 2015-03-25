def factorial(x):
    product = 1
    for i in range(x):
        product = product * (i + 1)
    return product

print ("factorial test:")
print (factorial(0))
print (factorial(1))
print (factorial(5))


def fibHelp(n):
    result = 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        result = fibHelp(n - 1) + fibHelp(n - 2)
    return result

print ("fibHelp test:")
print (fibHelp(10))


def fibonacci(n):
    result = []
    if n == 1:
        result = [1]
        return result
    elif n == 2:
        result = [1, 1]
        return result
    else:
        for i in range(n):
            result.append(fibHelp(i + 1))
        return result

print ("fibonacci test:")
print (fibonacci(1))
print (fibonacci(2))
print (fibonacci(10))

"""if __name__ == "__main__":
    n = int(input("Enter number:"))
    print (fibonacci(n))
"""


def sum_of_digits(n):
    n = abs(n)
    digits = list(map(int, str(n)))  # moje i bez List;
    sum = 0
    for i in digits:
        sum = sum + i
    return sum

print ("sum_of_digits test:")
print (sum_of_digits(1325132435356))
print (sum_of_digits(-15))


def fact_digits(n):
    n = abs(n)
    sum = 0
    digits = list(map(int, str(n)))
    for i in digits:
        sum = sum + factorial(i)
    return sum

print ("fact_digits test:")
print (fact_digits(999))


def palindrom(obj):
    obj = str(obj)
    if (len(obj) % 2 == 0):
        return False
    elif obj == obj[::-1]:
        return True

print ("palindrom test:")
print (palindrom("kapak"))
print (palindrom(121))
print (palindrom("baba"))


def to_digits(n):
    digits = list(map(int, str(n)))
    return digits

print ("to_digits test:")
print (to_digits(123))


def to_number(digits):
    result = ""
    for i in digits:
        result = result + str(i)
    int(result)
    return result

print ("to_number test:")
print (to_number([1, 2, 3]))


def fib_number(n):
    result = fibonacci(n)
    result = to_number(result)
    return result

print ("fib_number test:")
print (fib_number(3))


def count_vowels(str):
    sum = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    str = str.lower()
    for i in str:
        if i in vowels:
            sum = sum + 1
    return sum

print ("count_vowels test:")
print (count_vowels("Python"))


def count_constants(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    sum = 0
    str = str.lower()
    for i in str:
        if i not in vowels:
            sum = sum + 1
    return sum

print ("count_constants test:")
print (count_constants("Python"))


def char_histogram(string):
    dictionary = {}
    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u', 'y']:
            dictionary[i] = count_vowels(i)
        else:
            dictionary[i] = count_constants(i)
    return dictionary

print ("char_histogram test:")
print (char_histogram("Python!"))


def p_score(n):
    sum1 = 0
    if palindrom(n):
        return 1
    else:
        reverse = str(n)
        reverse = reverse[::-1]
        reverse = int(reverse)
        new_n = n + int(reverse)
        sum1 = 1 + p_score(new_n)

        return sum1

print ("p_score test:")
print (p_score(48))
print (p_score(198))


def is_increasing(seq):
    flag = True
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            flag = False
    return flag

print ("is_increasing test:")
print (is_increasing([1, 2, 3, 4, 5]))
print (is_increasing([5, 6, -10]))
print (is_increasing([1, 1, 1, 1]))
print (is_increasing([1]))


def is_decreasing(seq):
    flag = True
    for i in range(len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            flag = False
    return flag
print("is_decreasing test:")
print (is_decreasing([5, 4, 3, 2, 1]))
print (is_decreasing([1, 2, 3]))
print (is_decreasing([1, 1, 1, 1]))


def next_hack(n):
    binNumber = bin(n + 1)[2:]
    if palindrom(binNumber):
        return n + 1
    else:
        return next_hack(n + 1)

print ("next_hack test:")
print (next_hack(0))
print (next_hack(10))
# print bin(17)[2:]
print (next_hack(8031))
