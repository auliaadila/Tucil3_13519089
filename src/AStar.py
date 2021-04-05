from read import dist

def functionHN(node1, node2):
    return dist(node1, node2)

def functionGN(adjacentMatrix, node1, node2, curr_cost):
    adj_node1 = adjacentMatrix.get(node1)
    for i in range (len(adj_node1)):
        if (adj_node1[i][0] == node2):
            return adj_node1[i][1]+curr_cost
    return -1

def functionFN(adjacentMatrix, node1, node2, curr_cost):
    return functionGN(adjacentMatrix, node1, node2, curr_cost)+functionHN(node1, node2)

""" def minFinAdj (adjacentMatrix_, destination, curr_cost):
    if (len(adjacentMatrix_ > 0)):
        temp_min = adjacentMatrix_[0]
    for i in range (len(adjacentMatrix_)):
        if (functionFN(adjacentMatrix, adjacentMatrix_[i], destination, curr_cost) < 
        functionFN(adjacentMatrix, temp_min, destination, curr_cost)) """

def aStar(adjacentMatrix, nodeMatrix, source, destination):
    path = []
    visited_Nodes = dict()

    path.append(source)
    #visited_Nodes.setdefault((source, functionFN(0,Heuristik(source,destination))))
    current_gn = 0

    while (destination not in visited_Nodes.keys()):
        temp_adjMatrix = adjacentMatrix.get(source) #
        for i in range (len(temp_adjMatrix)):


""" A  :  ['B']

B  :  ['A', 'C', 'E', 'G']

C  :  ['B', 'D']
pathFIX : C
visited : (akan dibandingkan)

visited : BD

pathFIX : CDEHIKB
visited : B F E J --> dipilih anak dengan f(n) terkecil

temp_adj : 
path : CD

D  :  ['C', 'E', 'I']

E  :  ['B', 'D', 'F', 'H']
F  :  ['E', 'G', 'J']
G  :  ['B', 'F']
H  :  ['E', 'I', 'J', 'L']
I  :  ['D', 'H', 'K']
J  :  ['F', 'H', 'M']
K  :  ['I', 'L']
L  :  ['H', 'K', 'M']
M  :  ['J', 'L'] """