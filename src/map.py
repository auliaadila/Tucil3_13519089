# JUPITER 1
# import folium package
import folium
from AStar_2 import aStar, getIdx, getTotalCost
from read import readinput, makeArrayofWords, makeAdjancentMatrix, makeDictionary, makeNodeMatrix

lines = readinput("alun2.txt")
arrayOfWords = makeArrayofWords(lines)
adjacentMatrix = makeAdjancentMatrix(arrayOfWords)
nodeMatrix = makeNodeMatrix(arrayOfWords)
dictionary_adj = makeDictionary(adjacentMatrix,nodeMatrix)

listofNodes = []
for nodes in nodeMatrix:
    listofNodes.append(nodes[0])

print("============================")    
print("|List of Available Nodes : |")
for node in listofNodes:
    print("|- ",node, "                     |")
print("============================") 

source = input("Input source: ")
while (source not in listofNodes):
    print("Not Available Node")
    source = input("Input source: ")

destination = input("Input destination: ")
while (destination not in listofNodes):
    print("Not Available Node")
    destination = input("Input destination: ")

visited_Nodes = aStar(dictionary_adj, nodeMatrix, source, destination)[1]
closed = aStar(dictionary_adj, nodeMatrix, source, destination)[0]

# JUPITER 2
def Pusat(nodeMatrix):
    # Ambil rerataan koordinat
    
    sum_lat = 0
    sum_long = 0
    for i in range(len(nodeMatrix)):
        sum_lat += float(nodeMatrix[i][1])
        sum_long += float(nodeMatrix[i][2])
    sum_lat = sum_lat/len(nodeMatrix)
    sum_long = sum_long/len(nodeMatrix)

    pusat = [sum_lat,sum_long]
    return pusat


pusat = Pusat(nodeMatrix)   
my_map1 = folium.Map(location = pusat, zoom_start = 12 )

def initializedMap(dictionary_adj, nodeMatrix, my_map1):
    for key,value in dictionary_adj.items():
        #node1
        m_long1 = float(nodeMatrix[getIdx(nodeMatrix,key)][1])
        m_lat1 = float(nodeMatrix[getIdx(nodeMatrix,key)][2])
        name1 = key

        #menandai letak node
        folium.Marker([m_long1,m_lat1], popup = name1).add_to(my_map1)

        for v in value:
            #node2
            m_long2 = float(nodeMatrix[getIdx(nodeMatrix,v[0])][1])
            m_lat2 = float(nodeMatrix[getIdx(nodeMatrix,v[0])][2])

            #warnain jalur antara node 1 dan node 2
            folium.PolyLine(locations = [(m_long1,m_lat1), (m_long2,m_lat2)],
            line_opacity = 0.2).add_to(my_map1)
    
    return my_map1


def updateMap(closed, dictionary_adj, my_map1, nodeMatrix):
    for i in range(len(closed)-1):
        #node1
        m_long1 = float(nodeMatrix[getIdx(nodeMatrix,closed[i])][1])
        m_lat1 = float(nodeMatrix[getIdx(nodeMatrix,closed[i])][2])

        #node2
        m_long2 = float(nodeMatrix[getIdx(nodeMatrix,closed[i+1])][1])
        m_lat2 = float(nodeMatrix[getIdx(nodeMatrix,closed[i+1])][2])

        #warnain jalur antara node 1 dan node 2
        folium.PolyLine(locations = [(m_long1,m_lat1), (m_long2,m_lat2)], color = 'red',
        line_opacity = 0.5).add_to(my_map1)
    
    return my_map1

#JUPITER 3
my_map1 = initializedMap(dictionary_adj, nodeMatrix, my_map1)
my_map1 = updateMap(closed, dictionary_adj, my_map1, nodeMatrix)
my_map1

#INFORMASI TAMBAHAN
print("Shortest Path  : ", end="")
for i in range(len(closed)):
    if i < len(closed)-1:
        print(closed[i], end= " -> ")
    else:
        print(closed[i])

print("Total Distance :  m", getTotalCost(closed,visited_Nodes))