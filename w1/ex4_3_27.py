def getDivisors(n):
    return [x for x in range(1, n + 1) if n % x == 0]

if __name__ == "__main__":
    print(getDivisors(18))
    print(getDivisors(812783))
