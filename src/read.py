from math import radians, cos, sin, asin, sqrt

# Membaca masukan dari file txt dan mengembalikannya 
# dalam bentuk array
def readinput(filename):
    file = open(filename)
    lines = file.read().splitlines()
    return lines

# Mengubah array of strings menjadi array of words
def makeArrayofWords(lines):
    arrayOfWords = []
    for line in lines:
        line = line.split(' ')
        arrayOfWords.append(line)
    return arrayOfWords


""" lines = readinput("itb.txt")
arrayOfWords = makeArrayofWords(lines)
for i in range (len(arrayOfWords)):
    print(arrayOfWords[i]) """

# Memisahkan matriks ketetanggaan dari input file
def makeAdjancentMatrix(arrayOfWords):
    adjacentMatrix = []
    N = int(arrayOfWords[0][0])
    for i in range (N+1,(len(arrayOfWords))):
        adjacentMatrix.append(arrayOfWords[i])
    return adjacentMatrix

# Memisahkan matriks node dari input file
def makeNodeMatrix(arrayOfWords):
    nodeMatrix = []
    N = int(arrayOfWords[0][0])
    for i in range (1,N+1):
        nodeMatrix.append(arrayOfWords[i])
    return nodeMatrix

""" print("")
adjacentMatrix = makeAdjancentMatrix(arrayOfWords)
for i in range (len(adjacentMatrix)):
    print(adjacentMatrix[i])

print("")
nodeMatrix = makeNodeMatrix(arrayOfWords)
for i in range (len(nodeMatrix)):
    print(nodeMatrix[i]) """

def dist(nodeMatrix, source, destination):
    #Penyederhanaan : longitude (x), latitude(y)
    
    for i in range (len(nodeMatrix)):
        if (source == nodeMatrix[i][0]):
            node1 = nodeMatrix[i]
        if (destination == nodeMatrix[i][0]):
            node2 = nodeMatrix[i]
            
    x1 = radians(float(node1[1]))
    x2 = radians(float(node2[1]))
    y1 = radians(float(node1[2]))
    y2 = radians(float(node2[2]))
    
    # Haversine formula 
    dx = x2 - x1 #longitude
    dy = y2 - y1 #latitude
    a = sin(dy / 2)**2 + cos(y1) * cos(y2) * sin(dx / 2)**2
    c = 2 * asin(sqrt(a)) 
     
    r = 6371
    return(c * r)

def changeMatrix(adjacentMatrix, nodeMatrix):
    newadjacentMatrix = [ [ 0 for i in range(len(adjacentMatrix)) ] for j in range(len(adjacentMatrix)) ]

    for i in range(len(adjacentMatrix)):
        for j in range(i):
            if(adjacentMatrix[i][j] != "0"):
                newadjacentMatrix[i][j] = dist(nodeMatrix, nodeMatrix[i][0],nodeMatrix[j][0])*1000
                newadjacentMatrix[j][i] = newadjacentMatrix[i][j]
            #print(adjacentMatrix[i][j], end=' ')
        #print('\n')
    return newadjacentMatrix

#Membuat dictionary dari matrix dan tetangganya
def makeDictionary(adjacentMatrix,nodeMatrix):
    dictionary_adj = dict()
    weighted_adj_matrix = changeMatrix(adjacentMatrix, nodeMatrix)
    for i in range(len(adjacentMatrix)):
        tempAdj = []
        for j in range (len(adjacentMatrix)):
            if (adjacentMatrix[i][j] != '0'):
                tempAdj.append((nodeMatrix[j][0], weighted_adj_matrix[i][j]))
        dictionary_adj.setdefault(nodeMatrix[i][0], tempAdj)
    return dictionary_adj


""" print("")
dictionary_adj = makeDictionary(adjacentMatrix,nodeMatrix)
for key, value in dictionary_adj.items():
    print(key, " : ",value)

new = changeMatrix(adjacentMatrix, nodeMatrix)
for i in range(len(new)):
    for j in range(len(new)):
        print(new[i][j], end =' ')
    print('\n')


visited_Nodes = dict()

for i in range(len(adjacentMatrix)):
    visited_Nodes.setdefault(nodeMatrix[i][0],(0,0,0,"A"))
    #print(visited_Nodes.get(nodeMatrix[i][0])[3],"\n")
    if (i%2 > 0):
        update_value = {nodeMatrix[i][0] : (3,-1,i-2,"A")}
        visited_Nodes.update(update_value)

new_visited_Nodes = dict(sorted(visited_Nodes.items(), key=lambda item: item[1][2]))
    
for key, value in new_visited_Nodes.items():
    print(key, " : ",value)

print(list(new_visited_Nodes.keys())[0])
 """