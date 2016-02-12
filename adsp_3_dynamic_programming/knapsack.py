from functools import total_ordering

# This total ordening defines comparison functions in terms of other functions
# for example if you know when two objects are equal, you also know when they are not
import sys


@total_ordering
class Item:
    def __init__(self, weight, value):
        """
        Creates a new Item for the KnapSack problem
        :param weight: The weight of this item,
                       the total weight of all elements in the KnapSack cannot exceed a certain maximum.
        :param value: The value that is stored in this Item
        """
        self._weight = weight
        self._value = value

    @property
    def weight(self):
        return self._weight

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "Item (weight: {}, value {})".format(self.weight, self.value)

    def __eq__(self, other):
        return self.weight == other.weight and self.value == other.value

    def __lt__(self, other):
        return self.value < other.value or self.weight < other.weight


@total_ordering
class KnapSack:
    def __init__(self, max_weight):
        self._max_weight = max_weight
        self.items = []  # fill this with items for this KnapSack

    @property
    def max_weight(self):
        return self._max_weight

    def solve(self, items: list):
        """
        Fills this KnapSack with items, does not exceed self.max_weight in weight
        Should set items in this KnapSack instance
        :param items: Array of candidate items
        """

        items = [Item(0, 0)] +items
        n = len(items)
        s = [[0 for i in range(n)] for i in range(self._max_weight + 1)]

        for i in range(items[0].weight, self._max_weight + 1):
            s[i][0] = items[0].value

        for weight in range(self._max_weight+1):
            print("")
            for i in range(1, n):
                sys.stdout.write("\t")
                ninclude = s[weight][i-1]
                if weight < items[i].weight:
                    s[weight][i] = ninclude
                    sys.stdout.write(str(s[weight][i]) + ":%i:%i"% (weight, weight - items[i].weight))
                    continue
                include = items[i].value + s[weight - items[i].weight][i - 1]
                if ninclude >= include:
                    s[weight][i] = ninclude
                else:
                    s[weight][i] = include
                # s[weight][i] = max(ninclude, include)
                sys.stdout.write(str(s[weight][i]) + ":%i:%i"% (weight, weight - items[i].weight))
        print("")
        print(s)
        weight = self._max_weight
        for i in range(n-1, 0, -1):
            if (i == 1 and s[weight][i] > 0) or s[weight][i] != s[weight][i-1]:
                self.items.append(items[i])
                weight -= items[i].weight
        for item in self.items:
            print(item.value, item.weight)
        return s[self._max_weight][n-1]

    @property
    def value(self):
        """
        Calculates the total of values in this KnapSack
        :return: the total of values
        """
        total = 0
        for item in self.items:
            total = total + item.value

        return total

    @property
    def weight(self):
        """
        Calculates the total of weigths in this KnapSack
        :return: the total of weights
        """
        total = 0
        for item in self.items:
            total = total + item.weight

        return total

    def __str__(self):
        """
        :return: String representation of this KnapSack
        """
        return "Knapsack (weight: {}, value {}, items [{}])".format(self.weight, self.value, ", ".join(map(str, self.items)))

    def __eq__(self, other):
        return self.max_weight == other.max_weight and sorted(self.items) == sorted(other.items)

    def __lt__(self, other):
        return self.value < other.value or self.weight < other.weight

