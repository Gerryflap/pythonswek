def getFibonacci():
    v = [0, 1, 1]
    p = 1
    pp = 1
    i = 0
    while True:
        if i <= 2:
            yield v[i]
            i += 1
        else:
            val = p + pp
            pp = p
            p = val
            yield val


def sumFibonacci(n):
    s = 0
    f = 0
    series = getFibonacci()
    while f < n:
        f = series.__next__()
        if f % 2 == 0:
            s += f
    return s


print(sumFibonacci(4 * 10 ** 6))
