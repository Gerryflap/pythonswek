from w2_graphs.graphIO import loadgraph, savegraph
from w2_graphs.basicgraphs import *
from w2_graphs.ex1 import createCycleGraph

def complement(g: graph):
    h = graph(len(g.V()))
    for i in range(len(g.V())):
        for j in range(i+1, len(g.V())):
            if g.findedge(g[i], g[j]) is None:
                h.addedge(h[i], h[j])
    return h


if __name__ == "__main__":
    print(complement(createCycleGraph(10)))
    print(complement(graph(4)))

    g = loadgraph('examplegraph.gr')
    savegraph(complement(g), 'complementexamplegraph.gr')
