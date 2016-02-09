from w1.ex4_3_27 import getDivisors
from anders.prime1 import getPrimes

def getPrimeFactors(n):
    return [x for x in getPrimes(n) if x in getDivisors(n)]

#WERKT NIET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def getPrimeFactorisation(n):
    factorisation = dict()
    total = 1
    pf = getPrimeFactors(n)
    for p in pf:
        factorisation[p] = 0
    for p in pf[::-1]:
        f = 0
        while total * p**(f + 1) <= n:
            f += 1
        total *= p**f
        factorisation[p] = f
    return factorisation
if __name__ == "__main__":
    print(getPrimeFactors(2132))
    print(getPrimeFactorisation(2132))


