# functions
def graphColoring_BackTracking(m, graph):
    VertexColors = [0,0,0,0]        # initialize array storing colors of Vertices

    if graphColoring(m, VertexColors, graph) == False:
        '''returns false if there is no possible solution'''
        return False


# input variables
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m     = 3           # number of colors
