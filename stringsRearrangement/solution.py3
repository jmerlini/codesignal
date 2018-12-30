# stringsRearrangement takes an array of equally sized words and returns true if there is a rearrangement where adjacent pairs differ by exactly one letter
def stringsRearrangement(inputArray):

    # convert the array into a graph where edges represent valid adjacent pairs
    matrix = createGraph(inputArray)

    # looks for a maximal path in the graph and returns result
    return findHamPath(matrix)

# createGraph creates adjacency matrix where matrix[i][j] = 1 if the words array[i] and array[j] differ by exactly 1 letter and is 0 otherwise
def createGraph(array):
    length = len(array)
    matrix = [[0]*length for word in range(0, length)]
    diff = 0
    for word1_idx in range(0, length):
        for word2_idx in range(0,length):
            for letter_idx in range(0, len(array[0])):
                if array[word1_idx][letter_idx] != array[word2_idx][letter_idx]:
                    diff += 1
            if diff == 1:
                matrix[word1_idx][word2_idx] = 1
            diff = 0
    return matrix


# Sets starting vertex, returns True if nextVertex finds a path with that starting vertex. Returns False after exhausting all vertices.
def findHamPath(matrix):
    path = []
    for i in range(0, len(matrix)):
        path.append(i)
        pathbool = nextVertex(matrix, path)
        if pathbool == True:
            return True
        else:
            path = []
    return False

# Given a path, looks to complete the path, recursively. Will return True if a maximal Hamiltonian path is found, otherwise returns False
def nextVertex(matrix, path):

    if len(path) == len(matrix):
        return True
    for j in range(0, len(matrix)):
        if matrix[path[-1]][j] == 1 and j not in path:
            path.append(j)
            pathbool = nextVertex(matrix, path)
            if pathbool == True:
                return True
            path.pop()
    return False
