from read import dist

def functionHN(nodeMatrix, current, destination):
    return dist(nodeMatrix, current, destination)

def functionGN(adjacentMatrix, parent, current, curr_cost):
    adj_parent = adjacentMatrix.get(parent)
    for i in range (len(adj_parent)):
        if (adj_parent[i][0] == current):
            return round(adj_parent[i][1]+curr_cost,3)
    return -1

def searchDist (dictionary_adj,node1, node2):
    for key, value in dictionary_adj.items():
        if key == node1: 
            for node in value:
                if node[0] == node2:
                    distance = node[1]
                    break
    return distance

def getIdx(nodeMatrix, node):
    for i in range (len(nodeMatrix)):
        if (node == nodeMatrix[i][0]):
            return i
    return -1

def updateGN(start_node, end_node, visited_Nodes, dictionary_adj, nodeMatrix):
    #path = []
    total_gn = 0
    from_node = start_node
    while (from_node != end_node):
        # Node tujuan sementara adalah previous node dari from_node
        to_node = visited_Nodes.get(from_node)[3]
        #cari jarak dari curr_node ke start_node
        total_gn += searchDist(dictionary_adj, from_node, to_node)
        from_node = to_node
        continue

    return total_gn
        

def functionFN(adjacentMatrix, parent, current, destination, curr_cost, nodeMatrix):
    return round(functionGN(adjacentMatrix, parent, current, curr_cost)+functionHN(nodeMatrix,current, destination),3)

def sortVisitedNodes(visited_Nodes):
    #new_visited_Nodes = dict()
    new_visited_Nodes = dict(sorted(visited_Nodes.items(), key=lambda item: item[1][2]))
    return new_visited_Nodes



def aStar(adjacentMatrix, nodeMatrix, source, destination):
    opened = dict() #berisi node yang diekspan dan akan dibandingkan nilainya
    visited_Nodes = dict()
    closed = []
    # inisialisasi dict visited_Nodes
    # visited_Nodes dictionary
    # KEY    VALUE
    #          0      1      2        3
    # node - g(n) - h(n) - f(n) - prev_node

    current_gn = 0
    current_node = source
    visited_Nodes.setdefault(source,(0,functionHN(nodeMatrix, source, destination),functionHN(nodeMatrix, source, destination),""))
    #jangan lupa tangani kalau ga nemu path
    while (current_node != destination):
        temp_adj = adjacentMatrix.get(current_node) #tetangga yg lg ditinjau
        for i in range(len(temp_adj)):
            temp_gn = functionGN(adjacentMatrix, current_node, temp_adj[i][0], current_gn)
            temp_hn = functionHN(nodeMatrix, temp_adj[i][0], destination)
            temp_fn = temp_gn + temp_hn
            if (temp_adj[i][0] not in visited_Nodes.keys()):
                visited_Nodes.setdefault(temp_adj[i][0], (temp_gn, temp_hn, temp_fn, current_node))
                opened.setdefault(temp_adj[i][0], (temp_gn, temp_hn, temp_fn, current_node))
            else:
                if (temp_fn < visited_Nodes.get(temp_adj[i][0])[2]):
                    update_value = {temp_adj[i][0] : (temp_gn, temp_hn, temp_fn, current_node)}
                    visited_Nodes.update(update_value)
                    opened.update(update_value)
                  
        #sort visited nodes
        visited_Nodes = sortVisitedNodes(visited_Nodes)
        for key, value in visited_Nodes.items():
            if (key in opened.keys()):
                current_node = key
                current_gn = value[0]
                del opened[current_node]
                break

    if (current_node == destination):
        current_backtrack = current_node

        while (current_backtrack != ""):
            closed.insert(0,current_backtrack)
            current_backtrack = visited_Nodes.get(current_backtrack)[3]
    
    return closed, visited_Nodes

def getTotalCost(closed,visited_Nodes):
    return visited_Nodes.get(closed[len(closed)-1])[2]

def getCost(node1, node2, weighted_adj_matrix, nodeMatrix):
    return weighted_adj_matrix[getIdx(nodeMatrix,node1)][getIdx(nodeMatrix,node2)]