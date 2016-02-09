#with a function
def getMultipleList3and5(n):
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


print(getMultipleList3and5(1000))

#with list comprehension
print(
    sum(
        [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
    )
)
