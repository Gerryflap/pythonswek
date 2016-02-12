class Infinity:
    def __cmp__(self, other):
        if type(other) == Infinity:
            return 0
        else:
            return 1

    def __gt__(self, other):
        return self.__cmp__(other) == 1

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return self.__cmp__(other) == 0

    def __ge__(self, other):
        return True

    def __eq__(self, other):
        if other is None:
            return True
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0




a = Infinity()
print(a is None)
print(a > 0)
print(a > Infinity())

