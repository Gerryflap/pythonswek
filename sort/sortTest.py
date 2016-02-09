import random

import time
from sort.heapsort import heapSort
from adsp_1_sorting.sorting import QuickSorter, InsertionSorter


def testSort(function, maxPower, label="algorithm", worstCase = False):
    for e in range(1, maxPower + 1):
        if worstCase:
            l = list(range(10**e))
        else:
            l = [random.randint(0, 10**5) for i in range(10**e)]
        ts = time.time()
        function(l)
        t = time.time() - ts
        print("%s: n = 10**%i; \tt=%f"%(label, e, t))

if __name__ == "__main__":
    print(heapSort([random.randint(-i, -i + 1) for i in range(10**2)]))
    testSort(heapSort, 6, "Heapsort")
    quickSorter = QuickSorter()
    insertionSorter = InsertionSorter()
    testSort(quickSorter.sort, 6, "Quicksort")
    testSort(insertionSorter.sort, 4, "InsertionSort", True)