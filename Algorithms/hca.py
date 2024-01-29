import math
import numpy as np

'''
Użytkownik podaje listę punktów w R2
Wykonywany jest algorytm algomeracyjnego podziału hierarchicznego
Zwracany jest graf przedstawiający podział na poszczególne grupy
'''

'''
Obliczenie metryki Euklidesa między dwoma punktami w R2
'''
def euclidDistance(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
'''
Pierwsza macierz odległości, na podstawie listy punktów
'''
def matrixInitialization(listOfPoints):
    n = len(listOfPoints)
    D = np.zeros([n,n])
    for i in range(0,n):
        for j in range(i,n):
            D[i][j] = euclidDistance(listOfPoints[i],listOfPoints[j])
        for j in range(0,i):
            D[i][j] = D[j][i]
    return D
'''
Znajdowanie minimum w macierzach, zwraca ten wiersz i kolumnę
'''
def findMininMatrix(distanceMatrix):
    [rows,columns] = np.shape(distanceMatrix)
    min = np.array([0,1])
    for i in range(0,rows):
        for j in range(i,columns):
            if distanceMatrix[i][j] != 0:
                if distanceMatrix[i][j]<distanceMatrix[min[0]][min[1]]:
                    min = np.array([i,j])
    return min
'''
Usuwa wybrany wiersz i kolumnę z macierzy, zastępuje elementy maksymalnymi wartościami
'''
def deleteElement(distanceMatrix):
    [r,c] = findMininMatrix(distanceMatrix)
    [rows,columns] = np.shape(distanceMatrix)
    newMatrix = []
    newRow = []
    for i in range(0,rows):
        for j in range(0,columns):
            if i != r and j != c:
                newRow.append(distanceMatrix[i][j])
            else:
                newRow.append()


A =matrixInitialization(np.array([[1,0],[1,0.2],[7,0],[7,0.2],[7,0.5]]))
print(A)
min =findMininMatrix(A)
print(min)
print(A[min[0]][min[1]])