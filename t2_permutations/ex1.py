from t2_permutations.perm import *

def gcd(x, y):
    a, b = abs(x), abs(y)
    while b != 0:
        a, b = b, a % b
    return a

def composition(p, q):
    out = p[:]
    for i in range(len(p)):
        out[i] = q[p[i]]
    return out


def inverse(p):
    out = p[:]
    for i in range(len(p)):
        out[p[i]] = i
    return out

def power(p, i):
    out = p[:]
    cycleList = cycles(p)
    for k in range(len(p)):
        e = p[k]
        for cycle in cycleList:
            if e in cycle:
                j = cycle.index(e)
                j = (j + i - 1) % len(cycle)
                out[k] = cycle[j]
    return out


def period(p):
    cycs = cycles(p)
    gcm = len(cycs[0])
    cycs = cycs[1:]
    for cycle in cycs:
        e = len(cycle)
        g = gcd(gcm, e)
        if g != e:
            gcm = (gcm * e)//g
    return gcm

print(composition([1, 0, 2, 3], [2, 1, 3, 0]))
p = [2, 0, 1, 4, 3, 6, 5]
print(cycles(p))
print(period(p))
print(composition(p, inverse(p)))
print(inverse(p))
print(power(p, 0))
print(power(p, -1))
print(power(p, 2141422))
q = [1, 2, 3, 0, 5, 6, 4, 8, 7]
print(power(q, 0))



P = testPermutation(100)
print(period(P))

"""
printPermutation(power(P, period(P)))
for offset in range(period(p)):
    for i in range(-4, 4):
        assert power(P, offset) == power(P, i * period(p) + offset)

"""