'''
import numpy as np
#Read file
def readMatrix():
    file = input("Insert your filename in filename.txt format : ")
    print("\n")

    f = open("../test/"+file, "r")

    #matrix = []
    #for line in f:
    
    with f:
        matrix = [[int(num) for num in line.split()]for line in f]
    print(matrix)
        


#Make dictionary of adjacent node

#Remake weighted matrix
#def weightedMatrix(matrix):

A = np.array([[0,67.0,0,0,0,0,0,0],
            [67.0,0,174.0,0,178.0,0,140.0],
            [0,174.0,0,175.0,0,0,0,0],
            [0,0,175.0,0,192.0,0,0,0],
            [0,178.0,0,192.0,0,142.0,0,120.0],
            [0,0,0,0,142.0,0,175.0,0],
            [0,140.0,0,0,0,175.0,0,0],
            [0,0,0,0,120.0,0,0,0]])

print(A)



import numpy as np

A = np.array([[0,67.0,0,0,0,0,0,0],
            [67.0,0,174.0,0,178.0,0,140.0,0],
            [0,174.0,0,175.0,0,0,0,0],
            [0,0,175.0,0,192.0,0,0,0],
            [0,178.0,0,192.0,0,142.0,0,120.0],
            [0,0,0,0,142.0,0,175.0,0],
            [0,140.0,0,0,0,175.0,0,0],
            [0,0,0,0,120.0,0,0,0]])
#print(A) 
#print(len(A))
for i in range(len(A)):
    for j in range(i):
        if(A[i][j] == "1"):
            #euclidean
        print(A[i][j], end=' ')
    print('\n')
'''
'''
import numpy as np
  
# intializing points in
# numpy arrays
point1 = np.array((-6.893220,107.610454))
point2 = np.array((-6.892613,107.610428))
  
# calculating Euclidean distance
# using linalg.norm()
dist = np.linalg.norm(point1 - point2)
  
# printing Euclidean distance
print(dist)
'''
pA=[-6.893220,107.610454]
pB=[-6.892613,107.610428]

def euc(pA,pB):
    x = pA[0] - pB[0]
    y = pA[1] - pB[1]
    return ((x**2 + y**2)**0.5)
#0.0006075565817278666
#print(euc(pA,pB))