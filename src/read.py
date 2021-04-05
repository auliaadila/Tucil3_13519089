import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

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


def makeAdjancentMatrix(arrayOfWords):
    adjacentMatrix = []
    N = int(arrayOfWords[0][0])
    for i in range (N+1,(len(arrayOfWords))):
        adjacentMatrix.append(arrayOfWords[i])
    return adjacentMatrix

print("")
adjacentMatrix = makeAdjancentMatrix(arrayOfWords)
for i in range (len(adjacentMatrix)):
    print(adjacentMatrix[i])

