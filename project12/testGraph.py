"""
File: testcourses.py

Laurie Jones, Harry Pinkerton, James Lawson

Builds a graph of the courses in the CS curriculum at W&L
"""

from modules.graph import LinkedDirectedGraph
from modules.linkedStack import LinkedStack
from modules.linkedQueue import LinkedQueue
from modules.grid import Grid
from modules.arrays import Array
##from modules.infinity import addWithInfinity
##from modules.infinity import minWithInfinity
##from modules.infinity import lessThanWithInfinity
from modules.infinity import *
from modules.dijkstraEntry import DijkstraEntry




def makeLabelTable(graph):
    """Returns a table (dictionary) associating vetrex labels with
    index positions."""
    table = {}
    index = 0
    for vertex in graph.vertices():
        table[vertex.getLabel()] = index
        index += 1
    return table

def makeDistanceMatrix(graph, table):
    """Returns a distance matrix for the given graph."""
    matrix = Grid(len(graph), len(graph), INFINITY)
    for vertex in graph.vertices():
        vertexLabel = vertex.getLabel()
        vertexIndex = table[vertexLabel]
        for edge in vertex.incidentEdges():
            neighborLabel = edge.getConnectedTo().getLabel()
            neighborIndex = table[neighborLabel]
            if edge:
               weight = edge.getWeight()
            else:
               weight = INFINITY
            matrix[vertexIndex][neighborIndex] = weight
    return matrix

def printDistanceMatrix(matrix, table):
    labels = Array(len(table))
    position = 0
    for label in table:
        labels[table[label]] = label
        position += 1
    print(" " * 14 + "".join(["{s:^{w}}".format(s=x, w=10)for x in labels]))
    print(" " * 14 + "".join(["{s:^{w}}".format(s=x, w=10) for x in range(len(labels))]))
    
    for row in range(matrix.getHeight()):
        print("%8s %2d   " % (labels[row], row), end ="")
        
        print("".join(["{s:^{w}}".format(s=x, w=10) for x in matrix[row]]))
        

def traverseFromVertex(graph, startVertex, showProcess, collection = LinkedStack()):
    # Exercise
    graph.clearVertexMarks()
    collection.addVertex(startVertex)
    while collection is not collection.isEmpty():
        vertex = collection.pop()
        if not vertex.isMarked():
            vertex.setMark()
            if showProcess:
                print (vertex)
            for newVertex in vertex.neighboringVerticies:
                if not newVertex.isMarked():
                    collection.addVertex(newVertex)
    
    
def depthFirstTraverse(graph, startVertex, showProcess):
    # Exercise
    traverseFromVertex(graph, startVertex, ArrayStack())


def breadthFirstTraverse(graph, startVertex, showProcess):
    # Exercise
    traverseFromVertex(graph, startVertex, LinkedQueue())

    
def topoSort(graph):  
    # Exercise    
    stack = LinkedStack()
    graph.clearVertexMarks()
    for v in graph.neighboringVerticies(v.getLabel()):
        if not w.isMarked():
            dfs(g,w,stack)
    return stack

def dfs(graph, v, stack):
    v.setMark()
    for w in graph.neighboringVerticies(v.getLabel()):
        if not w.isMarked():
            dfs(graph, w, stack)
    stack.push(v)

def allPairsShortestPaths(matrix):
    # Exercise
    for a in range(matrix.getWidth()):
        for b in range(matrix.getWidth()):
            for c in range(matrix.getWidth()):
                matrix[b][c] = minWithInfinity(matrix[b][c], addWithInfinity(matrix[b][a], matrix[a][c]))
                
                                
def dijkstra(graph, startVertex):
    # Extra Credit
    results = {}
    unincluded = []
    for vertex in graph.vertices():
        if vertex == startVertex:
            results[vertex.getLabel()] = DijkstraEntry(vertex, 0, "UNDEF", True)
        else:
            edge = graph.getEdge(startVertex.getLabel(), vertex.getLabel())
            if edge:
                results[vertex.getLabel()] = DijkstraEntry(vertex, edge.getWeight(), startVertex.getLabel(), False)
            else:
                results[vertex.getLabel()] = DijkstraEntry(vertex, INFINITY, "UNDEF", False)
        
    while len(unincluded) > 0:
        #f is peek item
        #t is other
        unincluded.sort()
        nextItem = unincluded[0]
        unincluded.pop(0)
        peekItem = nextItem.vertex
        results[peekItem.getLabel()].included = True
        others = list(unincluded)
        for other in others:
            otherItem = other.vertex
            edge = peekItem.getEdgeTo(otherItem)
            if edge:
                newDistance = addWithInfinity(nextItem.distance, edge.getWeight())
                if lessThanWithInfinity(newDistance, other.distance):
                    unincluded.remove(other)
                    other.distance = newDistance
                    other.path = peekItem
                    unincluded.append(other)
    return results
            
        
    


#return list or dictionary with dijkstra enties, (0, und, true), edge- distance, path- source vertex as false no edge- infinity, path undd, included, false
        
          
          
def main():
        
    # Create a directed graph using an adjacency list
    graph = LinkedDirectedGraph()
    
    # Add vertices with appropriate labels and print the graph
    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")
    graph.addVertex("E")
    graph.addVertex("F")
    graph.addVertex("G")
    graph.addVertex("H")
    graph.addVertex("I")
    graph.addVertex("J")
    # Insert vertices
##    for ch in "A, B, C, D, E, F, G, H, I, J":
##        graph.addVertex(ch)
    
    print("\nThe graph: \n" + str(graph))
    
    # Insert edges with weights and print the graph
    graph.addEdge("A", "B", 3)
    graph.addEdge("A","J", 1)
    graph.addEdge("A","I", 8)
    graph.addEdge("J","B", 1)
    graph.addEdge("J","H", 6)
    graph.addEdge("H","B", 2)
    graph.addEdge("H","E", 1)
    graph.addEdge("B","C", 2)
    graph.addEdge("C","E", 4)
    graph.addEdge("C","G", 2)
    graph.addEdge("G","F", 1)
    graph.addEdge("G","D", 1)
    graph.addEdge("D","I", 1)


    print("\nThe graph: \n" + str(graph))
    
    # Print the vertices adjacent to vertex A
    print("\nExpect vertices adjacent to A:")
    print(", ".join(list(map(str,graph.getVertex("A").neighboringVertices()))))
    
    # Print the edges incident to A
    print("Expect edges incident to A:")
    print(", ".join(list(map(str,graph.getVertex("A").incidentEdges()))))
    
        
    
    print("\nDepth first traversal:")
    #depthFirstTraverse(graph, graph.getVertex("A"), True)
    
    print("\nBreadth first traversal:")
    #breadthFirstTraverse(graph, graph.getVertex("A"), True)
    
    
        
    print("\nTopological sort:")
    #stack = topoSort(graph)
    #while not stack.isEmpty():
    #    print(stack.pop())
    
    
    print("\nLabel table for graph:")
    labelTable = makeLabelTable(graph)
    print(labelTable)
    
    
    print("\nInitial distance matrix for graph:")
    matrix = makeDistanceMatrix(graph, labelTable)
    printDistanceMatrix(matrix, labelTable)
    
    print("\nDistance matrix after running all pairs shortest paths:")
    allPairsShortestPaths(matrix)
    printDistanceMatrix(matrix, labelTable)
    
    #try:
    print("\nExtra Credit, apply Dijkstra's algorithm from node A:\n")
        
    results = dijkstra(graph, graph.getVertex("A"))
    print("Node Distance Path Included")
    print("\n".join([str(results[x]) for x in results.keys()]))
    
    #except Exception as e:
    #    print("Extra Credit failed, error:", e)
        

if __name__ == '__main__':
    main()
