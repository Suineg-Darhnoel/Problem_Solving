#!/usr/bin/python3
from collections.abc import Iterable

class Polynomial:
    """
    Polynomial in the form of a_nX^n + a_(n-1)X^(n-1) + ... + a_0

    """
    def __init__(self, coeffs=[]):
        self.__coeffs = coeffs
        self.__degree = len(coeffs)-1

    # compute polynomial using bruteforce
    def compute(self, x):
        assert(self.degree >= 0)
        total = 0
        for n, coeff in enumerate(self.coeffs):
            total += coeff * (x**(self.degree-n))
        print("p({}) = {}".format(x, total))
        return total

    # compute polynomial using horner's rule
    def horner(self, x):
        assert(self.degree >= 0)
        total = 0
        for coeff in self.coeffs[:-1]:
            total = x * (coeff + total)
        total += self.coeffs[-1]
        print("p({}) = {}".format(x, total))
        return total

    def __add__(self, other):
        assert(isinstance(other, Polynomial))
        new_coeffs = []
        for c_p1, c_p2 in zip(self.coeffs, other.coeffs):
            new_coeffs.append(c_p1 + c_p2)
        return Polynomial(new_coeffs)

    def __sub__(self, other):
        assert(isinstance(other, Polynomial))
        new_coeffs = []
        for c_p1, c_p2 in zip(self.coeffs, other.coeffs):
            new_coeffs.append(c_p1 - c_p2)
        return Polynomial(new_coeffs)

    def __eq__(self, other):
        return True if self.coeffs == other.coeffs else False

    @property
    def coeffs(self):
        return self.__coeffs;

    @coeffs.setter
    def coeffs(self, coeffs):
        assert(isinstance(coeffs, Iterable)),\
            "coeffiecent must be iterable"
        self.__coeffs = coeffs

    @property
    def degree(self):
        return len(self.coeffs)-1;

    def __repr__(self):
        degree = self.degree
        coeffs_info = self.coeffs

        bar = "*"*50
        name = "\n{}-degree Polynomial with coefficients : {}\n".\
                format(degree, coeffs_info)
        return (bar + name + bar)


x = Polynomial([3, 4, 5])
y = Polynomial([4, 2, -1])
z = Polynomial([3, 4, 5])

print(y)
y.compute(-100)
y.horner(-100)
print(x+y)
print(x-y)
print(x == y)
print(x == z)
