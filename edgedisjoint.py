##Name: Bradly Schlenker
##This project solves the unweighted directed-edge edge-disjoint
##paths problem.
##Although, these edges do have the ability to hold weight, it is
##best to give all edges in the graph a capacity of 1.
##As well, if the graphs have cycles then this algorithm fails.
##It only works correctly on graphs with no cycles. (DAG's)
##The test and remake methods far below should give an idea to the
##user on how to test and use this implementation.
##This implementation does not store copies of things and thus
##requires reinitialization every time you find the edge-disjoint
##paths from some place to another. There are ways to avoid this
##by merely storing variables that hold copies, but that is left
##up to the user to decide if they want to do such. There are downsides
##to both methodologies.

##Acknowledgements are made to Wikipedia throughout for base structures.

##This class (Edge) represents an edge that is part of a directed
##graph. This representation is used by the Wikipedia entry
##on the Ford-Fulkerson algorithm. Although, anyone could
##easily redo this in their own version (but it wouldn't
##change anything).


class Edge(object):
    ##This initialization creates a directed edge with a
    ##capacity/weight. Although, for this project, weight = 1 is best.
    ##param u (string) - a source node.
    ##param v (string) - a sink/destination node.
    ##param w (string) - weight of the edge
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
    ##Returns a representation of the edge as a string
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)

##This class (FlowNetwork) represents a directed graph network
##with weighted Edges (But they all should equal 1). This representation is used to analyze
##the maximum edge-disjoint sets and then print out the edge-disjoint sets
##from a path s-t. Uses the Ford-Fulkerson algorithm to do such.
##This code is provided partially from Wikipedia. Edits were made
##to make it print the edge-disjoint sets from s-t and some other
##edits. You can compare and contrast with the Wikipedia page for reference.
class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}

    ##Adds a vertex to the network/graph.
    ##param vertex (string) - a name to represent the vertex
    def add_vertex(self, vertex):
        self.adj[vertex] = []

    ##Gets the edges that are going out of a requested vertex
    ##Operates on self.
    ##param v (string) - The vertex you wish to get the edges of
    ##returns self.adj[v] - a list of edges
    def get_edges(self, v):
        return self.adj[v]

    ##Adds an edge to the graph/network. Use 1 for weight
    ##when analyzing the disjoint-edges problem. Operates on self.
    ##param u (string) - a source node.
    ##param v (string) - a sink/destination node.
    ##param w (string) - weight of the edge (Defaults to 0)
    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        self.adj[u].append(edge)
        self.flow[edge] = 0

    ##Finds a path from the provided source node to
    ##the provided sink node. It will start with the
    ##path provided. Operates on self.
    ##param source (string) - the node to start at
    ##param sink (string) - the final destination
    ##param path - the starting edges to work with (Usually [])
    ##returns list - a path from the source to the sink
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge,residual) in path:
                result = self.find_path( edge.sink, sink, path + [(edge,residual)] ) 
                if result != None:
                    return result
    ##Finds the maximum amount of edge-disjoint sets. It will also
    ##print out all the edge-disjoint sets from the source to
    ##the sink node. Operates on self.
    ##
    ##param source (string) - the node to start at
    ##param sink (string) - the final destination
    ##returns int - the number of edge-disjoint sets
    def find_sets(self, source, sink):
        if(source == sink):
            print("Source == Sink. No solution?")
            return 0
        path = self.find_path(source, sink, [])
        if(path != None):
            thenetwork = path
            result = "Path taken for network: "
            for edge,res in thenetwork:
                result += edge.source + "->" + edge.sink + "  "
            print(result)
        while path != None:
            flow = min(res for edge,res in path)
            for edge,res in path:
                self.flow[edge] += flow
            path = self.find_path(source, sink, [])
            if(path != None):
                thenetwork = path
                result = "Path taken for network: "
                for edge,res in thenetwork:
                    result += edge.source + "->" + edge.sink + "  "
                print(result)
        return sum(self.flow[edge] for edge in self.get_edges(source))

##test data that is self-evident
##All tests below print out ALL possible tests.
def test():
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        for j in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
            g = remake()
            print ("Maximum number of edge-disjoint paths from %s to %s: %d \n\n"  % (i, j, g.find_sets(i,j)) )

##test data that is self-evident. This one has a cycle because of an edge from d to g.
def test2():
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        for j in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
            g = remake2()
            print ("Maximum number of edge-disjoint paths from %s to %s: %d \n\n"  % (i, j, g.find_sets(i,j)) )

##test data that is self-evident. This one has a cycle because of an edge from d to g.
##Only difference is how the edges are added to the graph.
def test21():
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        for j in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
            g = remake21()
            print ("Maximum number of edge-disjoint paths from %s to %s: %d \n\n"  % (i, j, g.find_sets(i,j)) )

##This one uses a completely different graph!
def test3():
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        for j in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
            g = remake3()
            print ("Maximum number of edge-disjoint paths from %s to %s: %d \n\n"  % (i, j, g.find_sets(i,j)) )

##This one uses a COMPLETELY CONNECTED (Self-loop even!)!
def test4():
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        for j in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
            g = remake4()
            print ("Maximum number of edge-disjoint paths from %s to %s: %d \n\n"  % (i, j, g.find_sets(i,j)) )

    

##remakes the FlowNetwork object. This goes for all of them.
##This is basically setting up the graph and then returning it.
def remake():
    g = FlowNetwork()
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        g.add_vertex(i)
    g.add_edge('a','b',1)
    g.add_edge('a','h',1)
    g.add_edge('a','e',1)
    g.add_edge('h','i',1)
    g.add_edge('b','c',1)
    g.add_edge('e','f',1)
    g.add_edge('i','b',1)
    g.add_edge('i','c',1)
    g.add_edge('i','j',1)
    g.add_edge('c','j',1)
    g.add_edge('c','d',1)
    g.add_edge('f','b',1)
    g.add_edge('f','g',1)
    g.add_edge('j','d',1)
    g.add_edge('j','z',1)
    ##Removing cycle
    ##g.add_edge('d','g',1)
    g.add_edge('d','z',1)
    g.add_edge('g','z',1)
    return g

def remake2():
    g = FlowNetwork()
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        g.add_vertex(i)
    g.add_edge('a','b',1)
    g.add_edge('a','h',1)
    g.add_edge('a','e',1)
    g.add_edge('h','i',1)
    g.add_edge('b','c',1)
    g.add_edge('e','f',1)
    g.add_edge('i','b',1)
    g.add_edge('i','c',1)
    g.add_edge('i','j',1)
    g.add_edge('c','j',1)
    g.add_edge('c','d',1)
    g.add_edge('f','b',1)
    g.add_edge('f','g',1)
    g.add_edge('j','d',1)
    g.add_edge('j','z',1)
    ##Adding cycle below
    g.add_edge('d','g',1)
    g.add_edge('d','z',1)
    g.add_edge('g','z',1)
    return g

def remake21():
    g = FlowNetwork()
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        g.add_vertex(i)
    g.add_edge('i','c',1)
    g.add_edge('a','b',1)
    g.add_edge('j','d',1)
    g.add_edge('j','z',1)
    g.add_edge('d','g',1)
    g.add_edge('a','h',1)
    g.add_edge('c','j',1)
    g.add_edge('c','d',1)
    g.add_edge('f','b',1)
    g.add_edge('f','g',1)
    g.add_edge('d','z',1)
    g.add_edge('g','z',1)
    g.add_edge('b','c',1)
    g.add_edge('e','f',1)
    g.add_edge('i','b',1)
    g.add_edge('a','e',1)
    g.add_edge('h','i',1)
    g.add_edge('i','j',1)
    return g

def remake3():
    g = FlowNetwork()
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        g.add_vertex(i)
    g.add_edge('a','b',1)
    g.add_edge('a','e',1)
    g.add_edge('a','h',1)
    g.add_edge('b','h',1)
    g.add_edge('c','g',1)
    g.add_edge('c','f',1)
    g.add_edge('d','f',1)
    g.add_edge('d','z',1)
    g.add_edge('e','b',1)
    g.add_edge('e','d',1)
    g.add_edge('f','e',1)
    g.add_edge('g','z',1)
    g.add_edge('h','c',1)
    g.add_edge('i','d',1)
    g.add_edge('j','c',1)
    g.add_edge('j','d',1)
    return g
	
	
def remake4():
    g = FlowNetwork()
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        g.add_vertex(i)
    for i in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
        for j in ['a','b','c','d','e','f', 'g', 'h', 'i', 'j', 'z']:
            if(i != j):
                g.add_edge(i, j, 1)
    return g
