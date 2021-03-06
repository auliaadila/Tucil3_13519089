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

def dist(nodeMatrix, source, destination):
    #Penyederhanaan : lat (x), long(y)
    for i in range (len(nodeMatrix)):
        if (source == nodeMatrix[i][0]):
            node1 = nodeMatrix[i]
        if (destination == nodeMatrix[i][0]):
            node2 = nodeMatrix[i]
            
    x1 = radians(float(node1[2]))
    x2 = radians(float(node2[2]))
    y1 = radians(float(node1[1]))
    y2 = radians(float(node2[1]))    
    # Haversine formula 
    dx = x2 - x1 #longitude
    dy = y2 - y1 #latitude
    a = sin(dy / 2)**2 + cos(y1) * cos(y2) * sin(dx / 2)**2
    c = 2 * asin(sqrt(a)) 
     
    r = 6371
    result = (c * r)*1000
    return round(result,3)

def changeMatrix(adjacentMatrix, nodeMatrix):
    newadjacentMatrix = [ [ 0 for i in range(len(adjacentMatrix)) ] for j in range(len(adjacentMatrix)) ]

    for i in range(len(adjacentMatrix)):
        for j in range(i):
            if(adjacentMatrix[i][j] == "1"):
                newadjacentMatrix[i][j] = dist(nodeMatrix, nodeMatrix[i][0],nodeMatrix[j][0])
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