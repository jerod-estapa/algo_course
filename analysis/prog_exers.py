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

# 2. Devise an experiment to verify that the 'get' method is O(1) for dictionaries.

print("Exercise 2")
print("----------")
print("dictionary get method speed")

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("x.get(random.randrange(%d))" % i, "from __main__ import random, x")

    x = {j: None for j in range(i)}
    get_time = t.timeit(number=1000)
    print("%d, %10.3f" % (i, get_time))


print("-----------------------------------")

# 3. Devise an experiment that compares the performance of the del operator on lists and dictionaries.

print("Exercise 3")

print("-----------------------------------")

# 4. Given a list of numbers in random order, write an algorithm that
#    works in O(nlog(n)) to find the kth smallest number in the list.

print("Exercise 4")

print("-----------------------------------")

# 5. Can you improve the previous problem to be linear?

print("Exercise 5\n")

def select(items, k):
    items = list(items)
    if not 0 <= k < len(items):
        raise ValueError("Not enough elements for the given rank.")
    while True:
        pivot = random.choice(items)
        pcount = 0
        under, over = [], []
        uappend, oappend = under.append, over.append
        for elem in items:
            if elem < pivot:
                uappend(elem)
            elif elem > pivot:
                oappend(elem)
            else:
                pcount += 1
        if k < len(under):
            items = under
        elif k < len(under) + pcount:
            return pivot
        else:
            items = over
            k -= len(under) + pcount


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

rand_list = [random.randint(100, 1000) for p in range(1000)]

wrapped = wrapper(select, rand_list, 500)

t = timeit.timeit(wrapped, number=1000)

print(t)