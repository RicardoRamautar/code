import timeit

def isPossible(vIdx, vertexColors, i, graph, nrVertices):
    neighbours = graph[vIdx]
    for j in neighbours:
        if vertexColors[j-1] == i:
            return False
    return True

def checkPossible(m, vertexColors, graph, vIdx):
    global stop
    neighbours = graph[vIdx]

    neighbourColors = dict.fromkeys([vertexColors[i-1] for i in neighbours])

    if len(neighbourColors) >= m:
        raise Exception("No possible answer")


def colorGraph(m, vertexColors, graph, vIdx):
    nrVertices = len(graph)

    if vIdx == nrVertices:
        return True
    
    if len(graph[vIdx]) >= m:
        checkPossible(m, vertexColors, graph, vIdx)

    for i in range(1, m+1):
        if isPossible(vIdx, vertexColors, i, graph, nrVertices) == True:
            vertexColors[vIdx] = i

            if colorGraph(m, vertexColors, graph, vIdx+1) == True:
                return True

            vertexColors[vIdx] = 0

def graphColoring_BackTracking(graph):
    vertexColors = [0 for i in range(len(graph))]

    m = 2
    while True:
        try: 
            if colorGraph(m, vertexColors, graph, 0) == True:
                return vertexColors
            else:
                m += 1
        except:
            m += 1
        # if colorGraph(m, vertexColors, graph, 0) == True:
        #     return vertexColors
        # else:
        #     m += 1

start = timeit.default_timer()
res1 = graphColoring_BackTracking([(2,3,4),(1,3,4),(1,2),(1,2)])
res2 = graphColoring_BackTracking([(2,4),(1,3),(2,4),(1,3)])
res3 = graphColoring_BackTracking([(4,5),(3,4),(2,4),(1,2,3),(1,4)])
res4 = graphColoring_BackTracking([(2,3,4),(1,3,5),(1,2,5),(1,5),(2,3,4)])
res5 = graphColoring_BackTracking([(2,3,4,6),(1,3,5),(1,2,5),(1,6),(2,3,6),(1,4,5)])
res6 = graphColoring_BackTracking([(2,3,4,6),(1,3,4,5),(1,2,5),(1,2,6),(2,3,6),(1,4,5)])
stop = timeit.default_timer()

if res1 == [1,2,3,3]:
    print("Test 1: Correct")
else:
    print("Test 1: FALSE!!!")

if res2 == [1,2,1,2]:
    print("Test 2: Correct")
else:
    print("Test 2: FALSE!!!")

if res3 == [1,1,2,3,2]:
    print("Test 3: Correct")
else:
    print("Test 3: FALSE!!!")

if res4 == [1,2,3,2,1]:
    print("Test 4: Correct")
else:
    print("Test 4: FALSE!!!")

if res5 == [1,2,3,2,1,3]:
    print("Test 5: Correct")
else:
    print("Test 5: FALSE!!!")

if res6 == [1,2,3,3,1,2]:
    print("Test 6: Correct")
else:
    print("Test 6: FALSE!!!")

print("Time: ", stop-start)