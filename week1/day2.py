import copy
import pprint


def sum_of_divisors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum = sum + i
    return sum

print ("sum_of_divisors test:")
print (sum_of_divisors(8))
print (sum_of_divisors(7))
print (sum_of_divisors(1000))


def is_prime(n):
    n = abs(n)
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True

print ("is_prime test:")
print (is_prime(1))
print (is_prime(2))
print (is_prime(8))
print (is_prime(11))
print (is_prime(-10))


def prime_number_of_divisors(n):
    number = 0
    for i in range(1, n + 1):
        if n % i == 0:
            number = number + 1
    if is_prime(number):
        return True
    else:
        return False

print ("prime_number_of_divisors test:")
print (prime_number_of_divisors(7))
print (prime_number_of_divisors(8))
print (prime_number_of_divisors(9))


def contains_digit(number, digit):
    digits = map(int, str(number))
    result = False
    for i in digits:
        if i == digit:
            result = True
            return result
    return result

print ("contains_digit test:")
print (contains_digit(123, 4))
print (contains_digit(42, 2))
print (contains_digit(1000, 0))
print (contains_digit(12346789, 5))


def contains_digits(number, digits):
    result = True
    for i in digits:
        if not contains_digit(number, i):
            result = False
    return result

print ("contain_digits test:")
print (contains_digits(402123, [0, 3, 4]))
print (contains_digits(666, [6, 4]))
print (contains_digits(123456789, [1, 2, 3, 0]))
print (contains_digits(456, []))


def is_number_balanced(n):
    lenght = len(str(n))
    # print lenght
    numbers = list(map(int, str(n)))
    if lenght == 1:
        return True
    elif lenght % 2 == 0:
        sum1 = 0
        sum2 = 0
        for i in range(0, (lenght // 2)):
            sum1 = sum1 + numbers[i]
        for i in range((lenght // 2), lenght):
            sum2 = sum2 + numbers[i]
        if sum1 == sum2:
            return True
        else:
            return False
    else:
        sum1 = 0
        sum2 = 0
        for i in range(0, (lenght // 2)):
            sum1 = sum1 + numbers[i]
        for i in range((lenght // 2) + 1, lenght):
            sum2 = sum2 + numbers[i]
        if sum1 == sum2:
            return True
        else:
            return False

print ("is_number_balanced test:")
print (is_number_balanced(9))
print (is_number_balanced(11))
print (is_number_balanced(13))
print (is_number_balanced(121))
print (is_number_balanced(4518))
print (is_number_balanced(28471))
print (is_number_balanced(1238033))


def count_substrings(heystack, needle):
    sum = heystack.count(needle)
    return sum

print("count_substrings test:")
print (count_substrings("This is a test string", "is"))
print (count_substrings("babababa", "baba"))
print (count_substrings("Python is an awesome language to program in!", "o"))


def zero_insert(n):
    numbers = list(map(int, str(n)))
    result = []
    result2 = []

    if (len(numbers) == 1):
        return numbers

    # same digits one after another check
    for i in range(0, len(numbers) - 1):
        result.append(numbers[i])
        if (numbers[i] == numbers[i + 1]):
            result.append(0)

        if (i == len(numbers) - 2):
            result.append(numbers[len(numbers) - 1])

    if len(result) > 0:
        numbers = result

    for i in range(0, len(numbers) - 1):
        result2.append(numbers[i])
        if ((numbers[i] + numbers[i + 1]) % 10) == 0:
            result2.append(0)

        if (i == len(numbers) - 2):
            result2.append(numbers[len(numbers) - 1])

    return result2

print ("zero_insert test:")
print (zero_insert(116457))
print (zero_insert(55555))
print (zero_insert(11223344))
print (zero_insert(6446))
print (zero_insert(1))


def sum_matrix(m):
    sum = 0
    for i in m:
        for j in i:
            sum = sum + j
    return sum

print ("sum_matrix test:")
print (sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print (sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print (sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))


NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
    (-1, 0), (1, 0),  # Get to 8 and 7
    (-1, 1), (0, 1), (1, 1)]  # Get to 9, 5 and 6


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result

print ("matrix_bombing_plan test:")
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = matrix_bombing_plan(m)

pp = pprint.PrettyPrinter()
pp.pprint(result)
