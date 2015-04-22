from fractions import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        g_c_devisor = gcd(numerator, denominator)
        self.numerator = numerator / g_c_devisor
        self.denominator = denominator / g_c_devisor

    def __str__(self):
        if self.denominator == 1 or self.numerator == 0:
            return str(self.numerator)
        else:
            return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def reducer(self, a, b):
        for i in range(a, 0, -1):
            if b % i == 0 and a % i == 0:
                a /= i
                b /= i
        return int(a), int(b)

    def __add__(self, other):
        down = self.denominator * other.denominator
        up = self.numerator * other.denominator + \
            other.numerator * self.denominator
        return Fraction(up, down)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        up = self.numerator * other.denominator - \
            other.numerator * self.denominator
        down = self.denominator * other.denominator
        return Fraction(up, down)

    def __eq__(self, other):
        return self.numerator == other.numerator and \
                self.denominator == other.denominator

a = Fraction(1, 2)
b = Fraction(2, 4)
print ("Fraction test:")
print (a + b)
print (a * b)
print (a - b)
print (a == b)
