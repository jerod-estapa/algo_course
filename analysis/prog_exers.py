#!usr/local/bin/python3

# Analysis Section - Programming Exercises


# 1. Devise an experiment to verify that the list index operator is O(1).

import timeit
import random

print("Exercise 1")
print("----------")

t = timeit.Timer("l.index(5000)", "from __main__ import l")

print("l.index()")

for i in range(100000, 10000001, 1000000):
    l = list(range(i))
    lt = t.timeit(number=1000)
    print("%15.5f" % lt)

print("-----------------------------------")

# 2. Devise an experiment to verify that the 'get' method is O(1) for dictionaries
print("Exercise 2")
print("----------")

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x.get(random.randrange(%d))" % i, "from __main__ import random, x")

    x = {j: None for j in range(i)}
    get_time = t.timeit(number=1000)
    print("%d, %10.3f" % (i, get_time))


print("-----------------------------------")

# 3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.


print("-----------------------------------")

# 4. Given a list of numbers in random order, write an algorithm that
#    works in O(nlog(n)) to find the kth smallest number in the list.


print("-----------------------------------")

# 5. Can you improve the previous problem to be linear?
