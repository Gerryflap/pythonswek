class Sorter(object):
    """
    Base class for sorters. Defines the `sort` method.
    """

    def sort(self, elements):
        """
        Sorts the elements in the list.

        :param elements: The list of elements which has to be sorted
        :type elements: list
        :return: The sorted list of elements
        :rtype: list
        """
        raise NotImplementedError()


class InsertionSorter(Sorter):
    """
    Sorter implementation using the insertion sort strategy.
    """

    def sort(self, elements):
        for j in range(1, len(elements)):
            v = elements[j]
            i = j - 1
            while i >= 0 and elements[i] > v:
                elements[i + 1] = elements[i]
                i -= 1
            elements[i + 1] = v
        return elements


class QuickSorter(Sorter):
    """
    Sorter implementation using the quick sort strategy.
    """

    def sort(self, elements):
        self.quickSort(elements, 0, len(elements) - 1)
        return elements

    def quickSort(self, elements, left, right):
        if right > left:
            i = self.partition(elements, left, right)
            self.quickSort(elements, left, i - 1)
            self.quickSort(elements, i + 1, right)

    def partition(self, elements, left, right):
        i, j = left, right
        pivot = elements[right]
        while i < j:
            while elements[i] < pivot and i < j:
                i += 1
            while elements[j-1] >= pivot and i < j:
                j -= 1
            if i < j:
                elements[i], elements[j - 1] = elements[j - 1], elements[i]
                i += 1
                j -= 1
        if pivot < elements[i]:
            elements[i], elements[right] = elements[right], elements[i]
        return i