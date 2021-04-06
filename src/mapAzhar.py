# IMPORT MODULE
from astar import eystar, get_key

# IMPORT LIBRARY
import folium

# Menghasilkan pusat koordinat peta
def centerCoordinate(nodePos):
    # Ambil rerataan koordinat
    n_Node = len(nodePos) # banyaknya node
    
    m_lat = 0
    m_long = 0
    for val in nodePos.values():
        m_lat += val[0]
        m_long += val[1]
    m_lat = m_lat/n_Node
    m_long = m_long/n_Node

    centerCoor = [m_lat,m_long]
    return centerCoor


# Menampilkan daftar node yang tersedia
def availableNode(nodeId):
    print("\nDaftar simpul yang tersedia")
    print("| ",end="")
    for node in nodeId:
        print(node, end=" | ")
    print()


# Menghasilkan peta umum yang mengvisualisasi graph
def generateGeneralMap(adjacentMatrix, nodeId, nodePos):

    # Ambil rerataan koordinat
    centerCoor = centerCoordinate(nodePos)
    
    # Buat Peta
    generalMap = folium.Map(location = centerCoor, zoom_start = 15)

    # Tambah Simpul
    for node in nodePos.keys():
        folium.Marker([nodePos.get(node)[0], nodePos.get(node)[1]], tooltip=('{}\n'.format(node))).add_to(generalMap)

    # Tambah Sisi
    for i in range(len(nodeId)):
        for j in range(i):
            if (adjacentMatrix[i][j] > 0):
                nodeA = get_key(list(nodeId.values()).index(i), nodeId)
                nodeB = get_key(list(nodeId.values()).index(j), nodeId)    
                path = [nodePos.get(nodeA), nodePos.get(nodeB)]     # buat jalur dari nodeA ke nodeB
                folium.PolyLine(path, color='cyan').add_to(generalMap)   # tambahkan jalur ke peta
                
    return generalMap


# Menghasilkan peta yang mengvisualisasi rute
def generatePathMap(adjacentMatrix, nodeId, nodePos, startNode, finalNode):
    if not (startNode in nodeId.keys() and finalNode in nodeId.keys()):
        return print("Masukan simpul tidak sesuai")
    
    # Ambil rerataan koordinat
    centerCoor = centerCoordinate(nodePos)
    
    # Buat Peta
    pathMap = folium.Map(location = centerCoor, zoom_start = 15)
    
    # Rute yang dapat ditempuh
    try:
        result = eystar(startNode, finalNode, nodePos, nodeId, adjacentMatrix)
        path = result[0]
        jarak = result[1]

        # Buat peta baru
        pathMap = folium.Map(location = centerCoor, zoom_start = 15)

        # Tambah Simpul di peta baru
        for node in path:
            folium.Marker([nodePos.get(node)[0], nodePos.get(node)[1]], tooltip=('{}\n'.format(node))).add_to(pathMap)

        # Tambah rute di peta baru
        pastNode = path[0]
        i = 1

        while (i < len(path)):
            curNode = path[i]
            curPath = [nodePos.get(pastNode), nodePos.get(curNode)]
            folium.PolyLine(curPath, color='red').add_to(pathMap)   # tambahkan jalur ke peta

            pastNode = curNode
            i += 1
            
        return pathMap
    except Exception as e:
        return print(str(e))
    

# Menampilkan rute dari startNode ke finalNode
def generatePath(adjacentMatrix, nodeId, nodePos, startNode, finalNode):
    if not (startNode in nodeId.keys() and finalNode in nodeId.keys()):
        return print("Masukan simpul tidak sesuai") 
    
    try:
        result = eystar(startNode, finalNode, nodePos, nodeId, adjacentMatrix)
        path = result[0]
        jarak = result[1]
        
        # Hasil pencarian
        print("Hasil pencarian rute:")
        for i in range(len(path)):
            if i < len(path)-1:
                print(path[i],end=" -> ")
            else:
                print(path[i])
        print("Panjang rute: %.2f m" %(jarak))
        
    except Exception as e:
        return print(str(e))
        