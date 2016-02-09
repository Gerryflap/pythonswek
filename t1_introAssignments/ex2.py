def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# gcd test
assert gcd(3141, 156) == 3

print(
    "The squares would have a size of %i" % (gcd(123456789, 987654321) ** 2)
)


def frac(a, b):
    if a == 0:
        return 0, 1
    if b == 0:
        raise ArithmeticError
    div = gcd(a, b)
    return a / div, b / div

assert frac(0, 4) == (0, 1)
assert frac(2, 4) == (1, 2)

error = False
try:
    frac(4, 0)
except ArithmeticError:
    error = True
assert error


print("All done!")
