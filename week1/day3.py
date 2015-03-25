def count_words(arr):
    dictionary = {}
    for i in arr:
        count = arr.count(i)
        dictionary[i] = count
    return dictionary

print ("count_words test:")
print (count_words(["apple", "banana", "apple", "pie"]))
print (count_words(["python", "python", "python", "ruby"]))


def unique_words_count(arr):
    return len(set(arr))

print ("unique_words_count test:")
print (unique_words_count(["apple", "banana", "apple", "pie"]))
print (unique_words_count(["python", "python", "python", "ruby"]))
print (unique_words_count(["HELLO!"] * 10))


def nan_expand(times):
    if times != 0:
        return ("Not a " * times) + "NaN"
    else:
        return " "

print ("nan_expand test:")
print (nan_expand(0))
print (nan_expand(1))
print (nan_expand(2))
print (nan_expand(3))


def iterations_of_nan_expand(expanded):
    result = expanded.count("Not a")
    if "Not a NaN" not in expanded or result < 1:
        return False
    else:
        return result

print ("iterations_of_nan_expand test:")
print (iterations_of_nan_expand(""))
print (iterations_of_nan_expand("Show these people!"))
print (iterations_of_nan_expand("Not a NaN"))
print (iterations_of_nan_expand(
    'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))


def group_help(lst):
    first_item = lst[0]
    result = [first_item]
    for i in range(1, len(lst)):
        if lst[i] == first_item:
            result.append(lst[i])
        else:
            break
    return result

print ("group_help test:")
print (group_help([1, 1, 1, 2, 1, 1, 3]))


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


def next_prime(n):
    n = n + 1

    while not is_prime(n):
        n = n + 1
    return n


def divide_count(n, k):
    times = 0

    while n != 1 and n % k == 0:
        times += 1
        n = n // k

    return times


def prime_factorization(n):
    result = []

    current_prime = 2

    while n != 1:
        times = divide_count(n, current_prime)

        if times != 0:
            result.append((current_prime, times))
            n = n // current_prime ** times

        current_prime = next_prime(current_prime)

    return result


print ("prime_factorization test:")
print (prime_factorization(10))
print (prime_factorization(14))
print (prime_factorization(356))
print (prime_factorization(89))
print (prime_factorization(1000))


def group(lst):
    result = []
    while len(lst) is not 0:
        sub_list = group_help(lst)
        result.append(sub_list)
        lst = lst[len(sub_list):]
    return result

print ("group test:")
print (group([1, 1, 1, 2, 3, 1, 1]))


def max_consecutive(items):
    items = group(items)
    return max([len(item) for item in items])

print ("max_consecutive test:")
print (max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print (max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def groupby(func, seq):
    dictionary = {}

    for item in seq:
        if func(item) not in dictionary:
            dictionary[func(item)] = [item]
        else:
            dictionary[func(item)].append(item)
    return dictionary


print ("groupby test:")
print (groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
print (groupby(lambda x: 'odd' if x %
               2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
print (groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))


def spam_help_by3(number):
    result = 0
    for i in range(1, number):
        if number % 3**i == 0 and i > result:
            result = i
    return result


def spam_help_by5(number):
    result = 0
    for i in range(1, number):
        if number % 5**i == 0 and i > result:
            result = i
    return result


def prepare_meal(number):
    if spam_help_by5(number) > 0 and spam_help_by3(number) > 0:
        return ['spam ' * spam_help_by3(number) + 'and eggs']
    elif spam_help_by3(number) > 0 and spam_help_by5(number) == 0:
        return ['spam ' * spam_help_by3(number)]
    elif spam_help_by3(number) == 0 and spam_help_by5(number) > 0:
        return ['eggs']
    else:
        return ""

print ("prepare_meal test:")
print (prepare_meal(3))
print (prepare_meal(5))
print (prepare_meal(7))
print (prepare_meal(15))
print (prepare_meal(27))
print (prepare_meal(45))


def reduce_path_slash_help(path):
    while "//" in path:
        path = path.replace("//", "/")
    return path


def reduce_file_path(path):
    if path[len(path) - 1] == "/" and len(path) > 1:
        path = path[0:len(path) - 1]

    path = reduce_path_slash_help(path)
    path = path.split("/", len(path))

    while '.' in path or ".." in path:
        if '.' in path:
            path.remove('.')
        elif ".." in path:
            pop_index = path.index("..")
            path.remove("..")
            path.remove(path[pop_index - 1])
    path = "/".join(path)
    if len(path) == 0:
        path = "/"
    return path

print ("reduce_file_path test:")
print (reduce_file_path("/"))
print (reduce_file_path("/srv/../"))
print (reduce_file_path("/srv/www/htdocs/wtf/"))
print (reduce_file_path("/srv/www/htdocs/wtf"))
print (reduce_file_path("/srv/./././././"))
print (reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print (reduce_file_path("//////////////"))
print (reduce_file_path("/../"))


def is_an_bn(word):
    if len(word) == 0:
        return True
    if len(word) % 2 != 0:
        return False

    first = word[0]
    last = word[len(word) - 1]
    flag = True
    if not (first == 'a' and word.count('a') == word[0:len(word) / 2].count('a')):
        flag = False
    if not (last == 'b'):
        flag = False
    return flag

print ("is_an_bn test:")
print (is_an_bn(""))
print (is_an_bn("rado"))
print (is_an_bn("aaabb"))
print (is_an_bn("aaabbb"))
print (is_an_bn("aabbaabb"))
print (is_an_bn("bbbaaa"))
print (is_an_bn("aaaaabbbbb"))


def is_credit_card_valid(number):
    number = list(map(int, str(number)))
    for i in range(len(number)):
        if i % 2 != 0:
            number[i] = number[i] * 2
    digits_sum = 0
    for item in number:
        if item > 9:
            digits_sum += item // 10 + item % 10
        else:
            digits_sum += item

    if digits_sum % 10 == 0:
        return True
    else:
        return False

print ("is_credit_card_valid test:")
print (is_credit_card_valid(79927398713))
print (is_credit_card_valid(79927398715))


def sum_of_divisors(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0:
            result += i
    return result
"""print (sum_of_divisors(8))
print (sum_of_divisors(7))
print (sum_of_divisors(1))
print (sum_of_divisors(1000))"""


def is_prime(n):
    n = abs(n)
    return sum_of_divisors(n) - 1 == n


def goldbach(n):
    current = 2
    result = []
    while current < n:
        if is_prime(current) and is_prime(n - current):
            if (n - current, current) not in result:
                result = result + [(current, n - current)]
        current = current + 1
    return result

print ("goldbach test:")
print (goldbach(4))
print (goldbach(6))
print (goldbach(8))
print (goldbach(10))
print (goldbach(100))


def magic_square(matrix):
    result1 = []
    for i in range(len(matrix)):
        result1.append(0)
        for j in range(len(matrix)):
            result1[i] = result1[i] + matrix[j][i]

    result2 = []
    for item in matrix:
        i = 0
        result2.append(sum(item))
        i += 1

    result3 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                result3.append(matrix[i][j])
    matrix.reverse()

    result4 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                result4.append(matrix[i][j])

    if sum(result4) == sum(result3) and result1.count(sum(result3)) == len(matrix) and result2.count(sum(result3)) == len(matrix):
        return True
    else:
        return False

print ("magic_square test:")
print (magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print (magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print (magic_square([[7, 12, 1, 14], [2, 13, 8, 11],
                                     [16, 3, 10, 5], [9, 6, 15, 4]]))
print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
