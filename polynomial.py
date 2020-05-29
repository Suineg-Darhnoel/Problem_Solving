#!/usr/bin/python3
from collections.abc import Iterable

class Polynomial:
    def __init__(self, coeffs=[]):
        self.__coeffs = coeffs
        self.__degree = len(coeffs)

    def compute(self, x):
        total = 0
        for n in range(self.degree):
            total += self.coeffs[n] * (x**n)
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
        return len(self.coeffs);

    def __repr__(self):
        degree = self.degree
        coeffs_info = self.coeffs

        bar = "*"*50
        name = "\n{}-degree Polynomial with coefficients : {}\n".\
                format(degree, coeffs_info)
        return (bar + name + bar)


x = Polynomial([3, 4, 5])
z = Polynomial([3, 4, 5])
y = Polynomial([4, 2, -1])
y.compute(-10)
print(x+y)
print(x-y)
print(x == y)
print(x == z)
