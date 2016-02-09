def encode(x):
    if 0 <= x < 10:
        return chr(x + 48)
    elif x < 36:
        return chr(x - 10 + 65)
    else:
        return ''


def decode(x):
    if '0' <= x <= '9':
        return ord(x) - 48
    elif 'A' <= x <= 'Z':
        return ord(x) - 65 + 10
    else:
        raise ValueError


def toK(n, k):
    out = ""
    if n == 0:
        return "0"
    if n < 0:
        raise ArithmeticError
    while n != 0:
        out = encode(n % k) + out
        n //= k
    return out


def fromK(n, k):
    out = 0
    f = 1
    while len(n) != 0:
        out += decode(n[-1]) * f
        f *= k
        n = n[:-1]
    return out


def convert(k, m, s):
    return toK(fromK(s, k), m)


print(toK(35, 2))

print(fromK("1001", 2))
print(fromK("1B", 16))
# Test the encode-decode function
for i in range(35):
    assert decode(encode(i)) == i

# test the toK-fromK function
for n in range(100):
    for k in range(2, 36):
        assert fromK(toK(n, k), k) == n

assert convert(2, 4, "10011010") == "2122"
assert convert(16, 7, "B48C03") == "202400366"
