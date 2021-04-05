from read import dist

def Heuristik(source, destination):
    return dist(source, destination)

def functionF(G,H):
    return G+H

def minFinAdj (adjacentMatrix_, destination):
    if (len(adjacentMatrix_ > 0)):
        temp_min = adjacentMatrix_[0]
    for i in range (len(adjacentMatrix_)):
        if ()

def findDistance(adjacentMatrix, node1, node2):
    adj_node1 = adjacentMatrix.get(node1)
    for i in range (len(adj_node1)):

def aStar(adjacentMatrix, nodeMatrix, source, destination):
    path = []
    visited_Nodes = dict()
    backtrack = []

    path.append(source)
    visited_Nodes.setdefault((source, functionF(0,Heuristik(source,destination))))
    current_gn = 0

    temp_adjMatrix = adjacentMatrix.get(source)
    for i in range len(temp_adjMatrix):
        visited_Nodes.append((source, functionF(,Heuristik(source,destination))))


    