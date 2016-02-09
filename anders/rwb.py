import random

import time

import math


def roodWitBlauw(array):
    cv = 0
    sortedI = 0
    while sortedI != len(array):
        if array[sortedI] == cv:
            sortedI += 1
        else:
            found = False
            for i in range(sortedI + 1, len(array)):
                if array[i] == cv:
                    array[sortedI], array[i] = array[i], array[sortedI]
                    found = True
                    break
            if not found:
                cv += 1
    return array

if __name__ == "__main__":
    print(roodWitBlauw([0,2,1,2,0,2,2,1,1,0]))
    for e in range(2, 10):
        n = int(10 ** (e/2))
        l = [int(3*random.random()) for i in range(n)]
        ts = time.time()
        roodWitBlauw(l)
        print((time.time() - ts))


