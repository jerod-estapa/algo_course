#!usr/local/bin/python3

# Analysis Section - Programming Exercises


# 1. Devise an experiment to verify that the list index operator is O(1).

import timeit

t = timeit.Timer("l.index(5000)", "from __main__ import l")

print("list.index()")

for i in range(100000, 10000001, 1000000):
    l = list(range(i))
    lt = t.timeit(number=1000)
    print("%15.5f" % lt)

print("-----------------------------------------------------")

# 2. Devise an experiment to verify that get_item and set_item are O(1) for dictionaries

