from graphObj import Graph
from queue import Queue

def dijkAlg(start:str, end:str, g: Graph) -> list:
    dist = {vertex: float('inf') for vertex in g.vertices()}
    dist[start] = 0
    visited = set()
    shortest = {}

    q = Queue()
    q.put(start)

    while not q.empty():
        current = q.get()
        visited.add(current)

        for neighbour, weight in g.getGraph().get(current, []):
            distance = dist[current] + weight
            if distance < dist[neighbour]:
                dist[neighbour] = distance
                shortest[neighbour] = current
                if neighbour not in visited:
                    q.put(neighbour)

    reconstructedPath = [] ##contains nodes from start to end in correct order
    
    ## this loop will reconstuct path in order starting from the end
    ## and going backwords to verify shortest path
    while end != start:
        reconstructedPath.insert(0, end)
        end = shortest[end]

    reconstructedPath.insert(0, start)
    if dist[end] != float('inf'):
        return reconstructedPath
    else:
        return "No shortest path"
    
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
myGraph.addEdges('A', 'B', 4)
myGraph.addEdges('A', 'D', 1)
myGraph.addEdges('B', 'C', 10)
myGraph.addEdges('B', 'D', 2)
myGraph.addEdges('B', 'F', 2)
myGraph.addEdges('C', 'D', 9)
myGraph.addEdges('C', 'E', 8)
myGraph.addEdges('D', 'E', 3)
myGraph.addEdges('E', 'F', 5)

# Print vertices and edges
print("Vertices:", myGraph.vertices())
print("Edges:", myGraph.edges())


dijkAlg('C','A',myGraph) ## should return: ['C', 'D', 'A']
dijkAlg('A','E',myGraph) ## shoud return: ['A', 'D', 'E']
dijkAlg('A','F',myGraph) ## should return: ['A', 'D', 'B', 'F']