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



# 3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.



# 4. Given a list of numbers in random order, write an algorithm that
#    works in O(nlog(n)) to find the kth smallest number in the list.


# 5. Can you improve the previous problem to be linear?
