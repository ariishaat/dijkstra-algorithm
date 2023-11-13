class Graph(object):
    def __init__(self,graph=None) -> None:
        if graph == None:
            graph = {}
        self.__graph = graph

    def vertices(self):
        return list(self.__graph.keys())
    
    def edges(self):
        return self.makeEdges()
    
    def addVertex(self, vertex):
        if vertex not in self.__graph:
            self.__graph[vertex] = []
    
    def addEdges(self,edge):
        (v1, v2, weight) = edge
        self.addVertex(v1)
        self.addVertex(v2)
        self.__graph[v1].append((v2, weight))
        self.__graph[v2].append((v1, weight))
    
    def makeEdges(self):
        edges = set()
        for vertex in self.__graph:
            for neighbour, weight in self.__graph[vertex]:
                if (vertex, neighbour,weight) not in edges and (neighbour, vertex, weight) not in edges:
                    edges.add((vertex, neighbour, weight))
        return edges
    
    def __str__(self):
        res = "List of vertices: "
        for k in self.__graph:
            res += str(k) + " "
        res += "\n List of edges: "
        for edge in self.makeEdges():
            res += str(edge) + " "
        return res

    def getGraph(self):
        return self.__graph
    

## Example:

myGraph = Graph()

# Add vertices
myGraph.addVertex('A')
myGraph.addVertex('B')
myGraph.addVertex('C')
myGraph.addVertex('D')
myGraph.addVertex('E')
myGraph.addVertex('F')

# Add weighted edges
myGraph.addEdges(('A', 'B', 4))
myGraph.addEdges(('A', 'D', 1))
myGraph.addEdges(('B', 'C', 10))
myGraph.addEdges(('B', 'D', 2))
myGraph.addEdges(('B', 'F', 2))
myGraph.addEdges(('C', 'D', 9))
myGraph.addEdges(('C', 'E', 8))
myGraph.addEdges(('D', 'E', 3))
myGraph.addEdges(('E', 'F', 5))

# Print vertices and edges
print("Vertices:", myGraph.vertices())
print("Edges:", myGraph.edges())

