from w2_graphs.graphIO import writeDOT, loadgraph

g = loadgraph('examplegraph.gr')
writeDOT(g, 'examplegraph.dot')

