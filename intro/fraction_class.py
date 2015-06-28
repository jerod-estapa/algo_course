#!usr/local/bin/python


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:


    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

# string method
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

# print method
    def show(self):
        print(self.num, "/", self.den)

# add method (adds fractions)
    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den *otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

# sets fractions as equal
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

# multiply method
    def __mul__(self, otherfraction):
        mulnum = self.num * otherfraction.num
        mulden = self.den * otherfraction.den
        return Fraction(mulnum, mulden)

# division method
    def __div__(self, otherfraction):
        divnum = self.num * otherfraction.den
        divden = self.den * otherfraction.num
        return Fraction(divnum, divden)

# subtraction method
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(self.newnum // common, self.newden // common)