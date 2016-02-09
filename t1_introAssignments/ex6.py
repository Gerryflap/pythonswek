def fact(x):
    out = 1
    for i in range(1, x+1):
        out *= i
    return out


def binomial(n, k):
    if n < 1 or n < k or k < 1:
        return ArithmeticError
    return fact(n)/(fact(n-k) * fact(k))

assert binomial(12, 8) == 495
assert binomial(40, 2) == 780
