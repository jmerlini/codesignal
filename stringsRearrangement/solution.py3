
# stringsRearrangement takes an array of equally sized words and returns true if there is a rearrangement where adjacent pairs differ by exactly one letter
def stringsRearrangement(inputArray):
    
    # convert the array into a graph where edges represent valid adjacent pairs
    a = createGraph(inputArray)
    
    # looks for a maximal path in the graph and returns result
    return findHamPath(a)

# createGraph creates adjacency matrix b where b[i][j] = 1 if a[i] and a[j] differ by exactly 1 letter and is 0 otherwise
def createGraph(a):
    m = len(a)
    b = [[0]*m for i in range(0,m)]
    s = 0
    for i in range(0,m):
        for j in range(0,m):
            for k in range(0,len(a[0])):
                if a[i][k] != a[j][k]:
                    s += 1
            if s == 1:
                b[i][j] = 1
            s = 0
    return b


# Sets starting vertex, returns True if nextVertex finds a path with that starting vertex. Returns False after exhausting all vertices.
def findHamPath(a):
    path = []
    for i in range(0,len(a)):
        path.append(i)
        pathbool = nextVertex(a,path)
        if pathbool == True:
            return True
        else:
            path = []
    return False

# Given a path, looks to complete the path, recursively. Will return True if a maximal Hamiltonian path is found, otherwise returns False
def nextVertex(a,path):
    
    if len(path) == len(a):
        return True
    for j in range(0,len(a)):
        if a[path[-1]][j] == 1 and j not in path:
            path.append(j)
            pathbool = nextVertex(a,path)
            if pathbool == True:
                return True
            path.pop()
    return False
