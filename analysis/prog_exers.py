#!usr/local/bin/python3

# Analysis Section - Programming Exercises


# 1. Devise an experiment to verify that the list index operator is O(1).

import timeit

l = list(range(1000000))
t = timeit.Timer("l.index(5000)", "from __main__ import l")

print(t.timeit(number=1000)/1000)