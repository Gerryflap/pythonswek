from random import random
def linsearch(e, k):
    i = 0
    for v in e:
        if v == k:
            return i
        i += 1
    return -1


def getRandomList(n):
    for i in range(n):
        yield round(random(), 6)

x = getRandomList(10000000000)
print(linsearch([0, 1, 2, 3, 5], 3))
print(linsearch(x, 0.5))
