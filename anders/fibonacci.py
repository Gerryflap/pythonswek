def getFibonacci(n):
    v = [0, 1, 1]
    p = 1
    pp = 1
    for i in range(n):
        if i <= 2:
            yield v[i]
        else:
            val = p + pp
            pp = p
            p = val
            yield val

n = 10000000
i = 0
for v in getFibonacci(n):
    if i == n-1:
        print(v)
    i += 1
