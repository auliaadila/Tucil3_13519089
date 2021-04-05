

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


lines = readinput("itb.txt")
arrayOfWords = makeArrayofWords(lines)
for i in range (len(arrayOfWords)):
    print(arrayOfWords[i])

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

print("")
adjacentMatrix = makeAdjancentMatrix(arrayOfWords)
for i in range (len(adjacentMatrix)):
    print(adjacentMatrix[i])

print("")
nodeMatrix = makeNodeMatrix(arrayOfWords)
for i in range (len(nodeMatrix)):
    print(nodeMatrix[i])

#Membuat dictionary dari matrix dan tetangganya
def makeDictionary(adjacentMatrix,nodeMatrix):
    dictionary_adj = dict()
    for i in range(len(adjacentMatrix)):
        tempAdj = []
        for j in range (len(adjacentMatrix)):
            if (adjacentMatrix[i][j] != '0'):
                tempAdj.append(nodeMatrix[j][0])
        dictionary_adj.setdefault(nodeMatrix[i][0], tempAdj)
    return dictionary_adj

print("")
dictionary_adj = makeDictionary(adjacentMatrix,nodeMatrix)
for key, value in dictionary_adj.items():
    print(key, " : ",value)


