def gcd(x, y):
    a, b = abs(x), abs(y)
    while b != 0:
        a, b = b, a % b
    return a


def getPrimes(n):
    primes = []
    for v in range(2, n+1):
        prime = True
        for p in primes:
            if gcd(v, p) != 1:
                prime = False
                break
        if prime:
            primes.append(v)
            yield v

if __name__ == "__main__":
    print(gcd(160, 120))
    print(list(getPrimes(100000)))
