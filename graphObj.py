
class Graph(object):

    def __init__(self,graph=None) -> None:
        if graph == None:
            graph = {}
        self.__graph = graph

    def vertices(self):
        return list(self.__graph.keys())
    
    def addVertex(self, vertex):
        if vertex not in self.__graph:
            self.__graph[vertex] = []
    
    def addEdges(self, v1, v2, weight):
        edge = (v1, v2, weight)
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
    
    def edges(self):
        return self.makeEdges()

    def __str__(self):
        res = "List of vertices: "
        for k in self.__graph:
            res += str(k) + " "
        res += "\nList of edges: "
        for edge in self.edges():
            res += str(edge) + " "
        return res

    def getGraph(self):
        return self.__graph