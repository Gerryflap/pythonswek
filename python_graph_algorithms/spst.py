from python_graph_algorithms.graphIO import loadgraph, \
    writeDOT  # graphIO imports basicgraphs.py, so we do not need to import it here.
from python_graph_algorithms.basicgraphs import vertex, graph, edge

# Use these options to change the tests:

TestBellmanFordDirected = True
TestBellmanFordUndirected = False
TestDijkstraDirected = True
TestDijkstraUndirected = False
TestKruskal = False


def relax(e: edge):
    """
    Relaxes the distance d(w) if d(v) + cvw is smaller
    :param e: edge between v and w
    :return: Nothing
    """
    w = e.head()
    v = e.tail()
    if not v.dist is None and (w.dist is None or w.dist > v.dist + e.weight):
        w.dist = v.dist + e.weight
        w.inedge = e


WriteDOTFiles = True

# Use these options to select the graphs to test your algorithms on:
# TestInstances = ["weightedexample.gr"]
# TestInstances=["randomplanar.gr"]
# TestInstances=["negativeweightexample.gr"]
# TestInstances=["negativeweightcycleexample.gr"]
# TestInstances=["WDE100.gr","WDE200.gr","WDE400.gr","WDE800.gr","WDE2000.gr"]; WriteDOTFiles=False
# TestInstances=["bbf2000.gr"]
TestInstances = ["graph%i.gr" % i for i in range(1, 8)]

# If you have implemented a module fastgraphs.py (compatible with basicgraphs.py),
# you can set this option to True:
UseFastGraphs = False


def BellmanFordUndirected(G, start):
    """
	Arguments: <G> is a graph object, where edges have integer <weight> 
		attributes,	and <start> is a vertex of <G>.
	Action: Uses the Bellman-Ford algorithm to compute all vertex distances 
		from <start> in <G>, and assigns these values to the vertex attribute <dist>.
		Optional: assigns the vertex attribute <indedge> to be the incoming
		shortest path edge, for every reachable vertex except <start>.
		<G> is viewed as an undirected graph.
	"""
    # Initialize the vertex attributes:
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0


# Insert your code here.


def BellmanFordDirected(G: graph, start):
    """
	Arguments: <G> is a graph object, where edges have integer <weight> 
		attributes,	and <start> is a vertex of <G>.
	Action: Uses the Bellman-Ford algorithm to compute all vertex distances 
		from <start> in <G>, and assigns these values to the vertex attribute <dist>.
		Optional: assigns the vertex attribute <indedge> to be the incoming
		shortest path edge, for every reachable vertex except <start>.
		<G> is viewed as a directed graph.
	"""
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

    # Insert your code here.
    for i in range(len(G.V()) - 1):
        for e in G.E():
            relax(e)

    for e in G.E():
        if e.tail().dist is not None and e.head().dist > e.tail().dist + e.weight:
            #raise Exception("Negative weight cycle found!")
            print("!!!!!!!!!!!!!!!!!!             Negative weight cycle found                !!!!!!!!!!!!!!!!!!")


def DijkstraUndirected(G, start):
    """
	Arguments: <G> is a graph object, where edges have integer <weight> 
		attributes,	and <start> is a vertex of <G>.
	Action: Uses Dijkstra's algorithm to compute all vertex distances 
		from <start> in <G>, and assigns these values to the vertex attribute <dist>.
		Optional: assigns the vertex attribute <indedge> to be the incoming
		shortest path edge, for every reachable vertex except <start>.
		<G> is viewed as an undirected graph.
	"""
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0


# Insert your code here.



def DijkstraDirected(G, start: vertex):
    """
	Arguments: <G> is a graph object, where edges have integer <weight> 
		attributes,	and <start> is a vertex of <G>.
	Action: Uses Dijkstra's algorithm to compute all vertex distances 
		from <start> in <G>, and assigns these values to the vertex attribute <dist>.
		Optional: assigns the vertex attribute <indedge> to be the incoming
		shortest path edge, for every reachable vertex except <start>.
		<G> is viewed as a directed graph.
	"""
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

    # Insert your code here.
    s = set()
    while len(s) != len(G.V()):
        # pick the next vertex
        minN = None
        for nv in [uv for uv in G.V() if uv not in s]:
            if minN is None or minN.dist is None \
                    or (nv.dist is not None and minN.dist > nv.dist):
                minN = nv

        v = minN
        s.add(v)
        for e in [ne for ne in v.inclist() if ne.tail() == v]:
            relax(e)


def Kruskal(G):
    """
	Arguments: <G> is a graph object, where edges have integer <weight> attributes.
	Action: Uses Kruskal's algorithm to compute all a minimum weight spanning tree
		of <G> (or a minimum weight maximal spanning forest if <G> is not connected).
		Returns a list <ST> of all edges that are in the minimum weight spanning
		tree (forest).
	"""
    ST = []  # will be the spanning tree. Append edge objects to this list.

    # Insert your code here.

    return ST


##############################################################################
#
# Below is test code that does not need to be changed.
#
##############################################################################

def printmaxdist(G):
    unreachable = False
    numreachable = 0
    unreachablev = []
    remote = G[0]
    for v in G:
        if v.dist == None:
            unreachable = True
            unreachablev.append(v)
        # print("Vertex",v,"is unreachable")
        else:
            numreachable += 1
            if remote.dist == None or v.dist > remote.dist:
                remote = v
    print("Number of reachable vertices:", numreachable, "out of", len(G.V()))
    if (len(G.V()) - numreachable > 0):
        print("Vertices that are unreachabe:", *unreachablev)
    print("Largest distance:", remote.dist, "For vertex", remote)


def preparedrawing(G):
    for e in G.E():
        e.colornum = 0
    for v in G.V():
        if hasattr(v, "inedge") and v.inedge != None:
            v.inedge.colornum = 1
    for v in G:
        if v.dist != None:
            v.label = v.dist
        else:
            v.label = "inf"


if __name__ == "__main__":
    from time import time

    if UseFastGraphs:
        import fastgraphs
    for FileName in TestInstances:
        if UseFastGraphs:
            print("\n\nLoading graph", FileName, "(Fast graph)")
            # G=loadgraph("graphs/"+FileName,graph)
            G = loadgraph(FileName, fastgraphs.graph)
        else:
            print("\n\nLoading graph", FileName)
            # G=loadgraph("graphs/"+FileName)
            G = loadgraph(FileName)

        for i in range(len(G.V())):
            G[i].colornum = i

        # Tuple arguments below:
        # First: printable string
        # Second: Boolean variable: should test be done?
        # Third: Function
        # Fourth: Filename
        # Fifth: Whether output should be directed
        for testalg in [("Bellman-Ford, undirected", TestBellmanFordUndirected, BellmanFordUndirected,
                         "BellmanFordUndirected", False),
                        ("Bellman-Ford, directed", TestBellmanFordDirected, BellmanFordDirected, "BellmanFordDirected",
                         True),
                        ("Dijkstra, undirected", TestDijkstraUndirected, DijkstraUndirected, "DijkstraUndirected",
                         False),
                        ("Dijkstra, directed", TestDijkstraDirected, DijkstraDirected, "DijkstraDirected", True),
                        ("Kruskal", TestKruskal, Kruskal, "Kruskal", False)]:
            if testalg[1]:
                print("\n\nTesting", testalg[0])
                startt = time()
                if testalg[0] == "Kruskal":
                    ST = testalg[2](G)
                    totalweight = 0
                    for e in ST:
                        totalweight += e.weight
                else:
                    testalg[2](G, G[0])
                endt = time()
                print("Elapsed time in seconds:", endt - startt)

                if testalg[0] != "Kruskal":
                    printmaxdist(G)
                    preparedrawing(G)
                else:
                    if len(ST) < len(G.V()) - 1:
                        print("Total weight of maximal spanning forest:", totalweight)
                    else:
                        print("Total weight of spanning tree:", totalweight)
                    for e in G.E():
                        e.colornum = 0
                    for e in ST:
                        e.colornum = 1
                    for v in G.V():
                        v.label = v._label

                if WriteDOTFiles:
                    # writeDOT(G,'graphs/'+testalg[3]+'.dot',directed=testalg[4])
                    writeDOT(G, testalg[3] + '.dot', directed=testalg[4])
