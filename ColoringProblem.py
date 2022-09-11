# functions

def isPossible(vIdx, vertexColors, i, graph, nrVertices):
    for j in range(nrVertices):
        if graph[vIdx][j] == 1 and vertexColors[j] == i:
            # graph[vIdx][j] == 1 checks if vertices vIdx and j are linked
            # vertexColors[j] == i checks if vertex j is of color i
            return False

    return True

def colorGraph(m, vertexColors, graph, vIdx):
    nrVertices = len(graph)

    if vIdx == nrVertices:
        return True

    for i in range(1, m+1):
        if isPossible(vIdx, vertexColors, i, graph, nrVertices) == True:
            vertexColors[vIdx] = i

            if colorGraph(m, vertexColors, graph, vIdx+1) == True:
                return True

            vertexColors[vIdx] = 0
    colorGraph(m, vertexColors, graph, vIdx+1)

def graphColoring_BackTracking(graph):
    vertexColors = [0 for i in range(len(graph))]        # initialize array storing colors of Vertices

    m = 2
    while True:
        if colorGraph(m, vertexColors, graph, 0) == True:
            print(vertexColors)
            return m
        else:
            m += 1
            
    


# input variables
# graph = [[0, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
# graph = [[0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0]]

print(graphColoring_BackTracking(graph))