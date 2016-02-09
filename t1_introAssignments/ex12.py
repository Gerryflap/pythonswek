import random

import math


def isProbabilyPrime(n, k):
    if n%2 == 0:
        return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    d = n - 1
    for a in [random.randrange(2, n - 2 + 1) for i in range(k)]:
        x = pow(a, d, n)
        if x != 1:
            i = 0
            while x != (n-1):
                if i == r - 1:
                    return False
                else:
                    i += 1
                    x = pow(x, 2, n)
    return True


def getNextPrime(n):
    i = 0
    while not isProbabilyPrime(n + i, 100):
        if (n + i) % 2 == 0:
            i += 1
        i += 2
    return n + i


print(isProbabilyPrime(669483106578092405936560831017556154622901950048903016651289, 10))
print(isProbabilyPrime(669483106578092405936560831017556154622901950048903016651287, 10))
print(isProbabilyPrime(7595009151080016652449223792726748985452052945413160073645842090827711, 10))
print(isProbabilyPrime(123456789987654321123456789987654321, 10))
print(getNextPrime(123456789123456789123456789123456789))
