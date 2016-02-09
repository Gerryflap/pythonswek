import math


def isPalindrome(x):
    s = str(x)
    palindrome = True
    for i in range(math.ceil(len(s)/2)):
        if s[i] != s[-(i + 1)]:
            palindrome = False
            break
    return palindrome

def getLargestPalindrome():
    mp = 0
    (mx, my) = (0, 0)
    for x in range(999, 0, -1):
        for y in range(999, 0, -1):
            if isPalindrome(str(x * y)):
                if x*y > mp:
                    mp = x*y
                    (mx, my) = (x, y)

    return mx, my

print (getLargestPalindrome())