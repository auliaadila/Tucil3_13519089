from AStar_2 import aStar
from read import readinput, makeArrayofWords, makeAdjancentMatrix, makeDictionary, makeNodeMatrix

lines = readinput("itb.txt")
arrayOfWords = makeArrayofWords(lines)
adjacentMatrix = makeAdjancentMatrix(arrayOfWords)
nodeMatrix = makeNodeMatrix(arrayOfWords)
dictionary_adj = makeDictionary(adjacentMatrix,nodeMatrix)

visited_Nodes = dict()
closed = []

print("")
dictionary_adj = makeDictionary(adjacentMatrix,nodeMatrix)
for key, value in dictionary_adj.items():
    print(key, " : ",value)
print("")

source = input("Masukkan source: ")
destination = input("Masukkan destination: ")


closed, visited_Nodes = aStar(dictionary_adj, nodeMatrix, source, destination)

print("")
for key, value in visited_Nodes.items():
    print(key, " : ",value)
print("")
print(closed)