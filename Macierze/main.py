'''
Szymon Murawski
08.2023
Biblioteka macierzy
'''
import math

class Matrix:
    def __init__(self,matrix =[[]]):
        self.matrix_ = matrix
        self.n_ = len(matrix)

    def __add__(self,other):
        new_matrix = []
        for r in range(0,self.n_):
            row = []
            for c in range(0,self.n_):
                row.append(self.matrix_[r][c]+other.matrix_[r][c])
            new_matrix.append(row)
        return Matrix(new_matrix)
    def __sub__(self,other):
        new_matrix = []
        for r in range(0,self.n_):
            row = []
            for c in range(0,self.n_):
                row.append(self.matrix_[r][c]-other.matrix_[r][c])
            new_matrix.append(row)
        return Matrix(new_matrix)
    def __truediv__(self,other):
        new_matrix = []
        for r in range(self.n_):
            row = []
            for c in range(self.n_):
                row.append(self.matrix_[r][c]/other)
            new_matrix.append(row)
        return Matrix(new_matrix)
    def __mul__(self,other):
        if type(other) == int or type(other) == float:
            new_matrix = []
            for r in range(self.n_):
                row = []
                for c in range(self.n_):
                    row.append(self.matrix_[r][c]*other)
                new_matrix.append(row)
            return Matrix(new_matrix)     
        else:
            new_matrix = []
            for r in range(self.n_):
                row = []
                for c in range(other.n_):
                    element = 0
                    for k in range(self.n_):
                        element += self.matrix_[r][k] * other.matrix_[k][c]
                    row.append(element)
                new_matrix.append(row)
            return Matrix(new_matrix)

    def printMatrix(self):
        for r in range(0,self.n_):
            for c in range(0,self.n_):
                print(str(self.matrix_[r][c])+" ",end="")
            print()
        print()
    
    def deleteRows(self,i,j):
        new_matrix = []
        if i < self.n_ and j < self.n_:
            for r in range(0,self.n_):
                row = []
                for c in range(0,self.n_):
                    if r != i and c !=j:
                        row.append(self.matrix_[r][c])
                if len(row) > 0:
                    new_matrix.append(row)
        return Matrix(new_matrix)
        
    def diag(self,diagonal):
        d = len(diagonal)
        new_matrix = []
        for r in range(0,d):
            row = []
            for c in range(0,d):
                if (r == c):
                    row.append(diagonal[r])
                else:
                    row.append(0)
            if len(row) > 0:
                    new_matrix.append(row)
        return Matrix(new_matrix)
    
    def ones(self,d):
        new_matrix = []
        for r in range(0,d):
            row = []
            for c in range(0,d):
                if (r == c):
                    row.append(1)
                else:
                    row.append(0)
            if len(row) > 0:
                    new_matrix.append(row)
        return Matrix(new_matrix)
    def zeros(self,d):
        new_matrix = []
        for r in range(0,d):
            row = []
            for c in range(0,d):
                row.append(0)
            if len(row) > 0:
                    new_matrix.append(row)
        return Matrix(new_matrix)
    def transposition(self):
        new_matrix = []
        for r in range(0,self.n_):
            row = []
            for c in range(0,self.n_):
                row.append(self.matrix_[c][r])
            new_matrix.append(row)
        return Matrix(new_matrix)
    def complement(self):
        new_matrix = []
        for r in range(0,self.n_):
            row = []
            for c in range(0,self.n_):
                row.append((-1)**(r+c)*self.deleteRows(r,c).determinant())
            new_matrix.append(row)
        return Matrix(new_matrix)


    def determinant(self):
        det = 0
        if self.n_ == 1:
            return self.matrix_[0][0]
        else:
            for i in range (0,self.n_):
                for j in range(0,self.n_):
                    det = det + (-1)**(i+j)*self.matrix_[i][j]*self.deleteRows(i,j).determinant()
                return det
    def inv(self):
        return self.complement().transposition()/self.determinant()


# A = Matrix([[0,1,2,7],[1,2,3,4],[5,6,7,8],[-1,1,-1,1]])
# A.printMatrix()
# print(A.determinant())
# E = Matrix()
# E = E.zeros(7)
# # E.printMatrix()
# A = Matrix([[1,2,1],[3,2,2],[7,7,3]])
# BB = A*2
# BB.printMatrix()
# AA = A.inv()
# A.printMatrix()
# AA.printMatrix()
A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
B = Matrix([[4,5,6],[7,8,9],[1,2,3]])
C = A*B
C.printMatrix()
# B = Matrix([[1,2,3],[4,5,6],[7,8,9]])
# B.printMatrix()
# F = B.transposition()
# F.printMatrix()
# C = Matrix([[1,1],[4,3]])
# D = B-C
# B.printMatrix()
# C.printMatrix()
# D.printMatrix()
