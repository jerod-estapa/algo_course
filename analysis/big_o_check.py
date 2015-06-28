import time
from random import randrange

def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin

'''def quad(a, b, c):
    list = [a, b, c]
    for x in list:
        if x > b:
            if c > x:
                return b
        elif x > c:
            if b > x:
                return c
        else:
            return a'''

def findMin(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar

print(findMin([5,4,2,1,0]))
print(findMin([0,2,3,4,5]))



for listSize in range(1000, 10001, 1000):
    aList = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(aList))
    end = time.time()
    print("size: %d time: %f" % (listSize, end-start))



