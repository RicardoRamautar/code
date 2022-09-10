# functions

def colorGraph(m, vertexColors, graph, vIdx):
    nrVertices = len(graph)

    if vIdx == nrVertices:
        return True

    for i in range(1, m+1):
        if isPossible(vIdx, vertexColors, i, graph) == True:
            vertexColors[vIdx] = i

            if colorGraph(m, vertexColors, graph, vIdx+1) == True:
                return True

            vertexColors[vIdx] = 0

def graphColoring_BackTracking(m, graph):
    vertexColors = [0 for i in range(len(graph))]        # initialize array storing colors of Vertices

    solution = False
    m = 1
    while solution == False:
        if colorGraph(m, vertexColors, graph, 0) == True:
            solution = True
        else:
            m += 1
            
    


# input variables
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m     = 3           # number of colors
