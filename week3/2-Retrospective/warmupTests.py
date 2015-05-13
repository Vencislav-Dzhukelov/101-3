import unittest
from warmup import *


class TestWarmups(unittest.TestCase):

    def test_char_histogram(self):
        self.assertEqual(char_histogram("Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})

    def test_count_constants(self):
        self.assertEqual(count_constants("Github is the second best thing that happend to programmers, after the keyboard!"), 44)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Theistareykjarbunga"), 8)

    def test_fact_digits(self):
        self.assertEqual(fact_digits(999), 1088640)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_fib_number(self):
        self.assertEqual(fib_number(10), 11235813213455)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_is_decreasing(self):
        self.assertTrue(is_decreasing([100, 50, 20]))
        self.assertEqual(is_decreasing([1, 1, 1, 1]), False)

    def test_is_increasing(self):
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))
        self.assertEqual(is_increasing([1, 1, 1, 1]), False)

    def test_next_hack(self):
        self.assertEqual(next_hack(8031), 8191)

    def test_palindrom(self):
        self.assertTrue(palindrom("kapak"))
        self.assertEqual(palindrom("baba"), False)

    def test_p_score(self):
        self.assertEqual(p_score(198), 6)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(1325132435356), 43)
        self.assertEqual(sum_of_digits(-10), 1)

    def test_to_digits(self):
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_to_number(self):
        self.assertEqual(to_number([1, 2, 3, 0, 2, 3]), 123023)

if __name__ == '__main__':
    unittest.main()
