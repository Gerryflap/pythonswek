import w2_graphs.basicgraphs as bg

def castToGraph(g: bg.graph):
    g.__class__ = Graph
    return g

class Graph(bg.graph):
    def delEdge(self, edge):
        self._E.remove(edge)

    def delVertex(self, vertex):
        for e in vertex.nbs():
            self.delEdge(e)
        self._V.remove(vertex)

if __name__ == "__main__":
    g = bg.graph(10)
    h = castToGraph(g)
    print(h)
    h.delVertex(g[0])
    print(h)