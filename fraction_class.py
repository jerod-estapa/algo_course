#!usr/local/bin/python

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

     def __mul__(self, otherfraction):
         mulnum = self.num * otherfraction.num
         mulden = self.den * otherfraction.den
         return Fraction(mulnum, mulden)

     def __div__(self, otherfraction):
         divnum = self.num * otherfraction.den
         divden = self.den * otherfraction.num
         return Fraction(divnum, divden)

     def __sub__(self, otherfraction):
         subnum =