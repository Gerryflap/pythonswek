from w2_graphs.basicgraphs import *
from w2_graphs.ex1 import createCycleGraph, createPathGraph
from w2_graphs.meerGraphs import getNeighbourDict
from w2_graphs.graphIO import writeDOT


def graphSearch(s: vertex, bf: bool):
    labels = dict()
    labels[s] = 1
    pred = dict()
    pred[s] = None
    l = [s]
    k = 1
    nbDict = getNeighbourDict(s._graph)
    while len(l) != 0:
        if bf:
            v = l[0]
        else:
            v = l[-1]
        unexploredNeighbours = [w for w in nbDict[v] if not w in labels]
        if len(unexploredNeighbours):
            w = unexploredNeighbours[0]
            k = k + 1
            labels[w] = k
            pred[w] = v
            l = l + [w]
        else:
            l.remove(v)
    return labels, pred

def addVisitingOrder(s: vertex, bf: bool):
    (labels, preds) = graphSearch(s, bf)
    for v in labels:
        v.label = labels[v]
    return s._graph


if __name__ == "__main__":
    print(graphSearch(graph(4)[1], True))
    print(graphSearch(createPathGraph(5)[1], True))
    print(graphSearch(graph(4)[1], False))
    print(graphSearch(createPathGraph(5)[1], False))
    g = createPathGraph(8)
    addVisitingOrder(g[7], True)
    writeDOT(g, 'BFvisitingOrder.dot')

    g = createPathGraph(8)
    addVisitingOrder(g[7], False)
    writeDOT(g, 'DFvisitingOrder.dot')