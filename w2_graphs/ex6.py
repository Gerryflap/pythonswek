import time

from w2_graphs.graphIO import loadgraph, savegraph
from w2_graphs.ex4 import graphSearch

g = loadgraph('graph8000.gr')
i = 0
times = []
for n in [1000, 2000, 4000, 8000]:
    g = loadgraph('graph%i.gr'%n)
    times.append(0)
    for j in range(5):
        ts = time.time()
        graphSearch(g[0], False)
        t = time.time() - ts
        times[i] += t
    times[i] /= 10
    i += 1

print(times)
