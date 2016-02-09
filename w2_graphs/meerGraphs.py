import w2_graphs.basicgraphs as bg

def getNeighbourDict(g: bg.graph):
    d = dict()
    for v in g.V():
        d[v] = []
    for e in g.E():
        d[e.tail()].append(e.head())
        d[e.head()].append(e.tail())
    return d
