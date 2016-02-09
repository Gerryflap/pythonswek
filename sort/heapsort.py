import math
import random

import time


def heapify(array, i, length=-1):
    if length == -1:
        length = len(array)
    left = 2 * i + 1
    right = 2 * i + 2
    max = i

    if left < length and array[max] < array[left]:
        max = left
    if right < length and array[max] < array[right]:
        max = right
    if max != i:
        array[max], array[i] = array[i], array[max]
        heapify(array, max, length)


def makeHeap(array):
    for i in range(
            int(2 ** int(math.log(len(array) - 1, 2))),
            -1, -1):
        heapify(array, i)

    return array


def heapSort(array):
    sortedStart = len(array) - 1
    makeHeap(array)
    for i in range(len(array)):
        array[0], array[sortedStart] = array[sortedStart], array[0]
        heapify(array, 0, sortedStart)
        sortedStart -= 1
    return array




if __name__ == "__main__":
    print("Making list")
    for e in range(2, 12):
        n = int(10 ** (e / 2))
        t = 0
        for j in range(10):
            l = [random.randint(0, n) for i in range(n)]
            ts = time.time()
            heapSort(l)
            t += (time.time() - ts) / (n * math.log(n))
        print(t)
