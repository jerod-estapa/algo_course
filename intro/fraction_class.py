#!usr/local/bin/python


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:


    def __init__(self, top, bottom):
        self.num = int(top / gcd(abs(top), abs(bottom)))
        self.den = int(bottom / gcd(abs(top), abs(bottom)))
        if top != int():
            print("Your first input is not a number!")
        elif bottom != int():
            print("Your second input is not a number!")

# get numerator
    def get_num(self):
        return self.num

# get denominator
    def get_den(self):
        return self.den

# string method
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

# print method
    def show(self):
        print(self.num, "/", self.den)

# add method (adds two fractions)
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

# reverse addition (right-sided addition)
    def __radd__(self, otherfraction):
        return otherfraction.__add__(self)

# set fractions as equal
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

# multiply method
    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

# division method
    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)

# subtraction method
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)
