#Matrix A with a size/order of 2x2
matriksA = [ [1,0],[0,1] ]

#Show the Matrix A
print (matriksA)

#Matrix A with a size/order of 3x3
matriksB = [ [1,0,1],[0,1,0],[1,0,1] ]

#Show the Matrix B
print (matriksB)

#Matrix using the loop function
m = 2
n = 3 
x = [0]*m

#Loop function using for
for i in range(m): 
    x[i] = [1]*n 
    
#Show the Matrix
print (x)

#Call Library Numpy
from numpy import * 

#Specifies the length of the element as 12
matriks = range(12) 

#The order matrix is 4x3
matriks = reshape(matriks,(4,3)) 

#Show the Matrix
print (matriks)

#Calls the numpy library and is given the alias np
import numpy as np

#Create a 3x4 matrix with random
matriks = np.random.randint(1,4,(3,4))

#Show the Matrix
print (matriks)

#Sum in Matrix
#Example 1
mat1 = [
    [5, 0],
    [2, 6],
]

mat2 = [
    [1, 0],
    [4, 2],
]


for x in range(0, len(mat1)):
    for y in range(0, len(mat1[0])):
        print (mat1[x][y] + mat2[x][y], end=' '),
    print

#Sum in Matrix
#Example 2
import numpy as np
matriksA = np.random.randint(1, 4,(3, 4))
matriksB = np.random.randint(1, 3,(3, 4))
print (matriksA)
print () #give line spacing to the printed matrix
print (matriksB)
print ()

#summation of matrix A and matrix B
for x in range(0, len(matriksA)):
    print ('Result of the sum of matrix and matrix B', 'Row-', x+1)
    print ()
    for y in range(0, len(matriksA[0])):
        print (matriksA[x][y] + matriksB[x][y], end=' '),
    print ()

#Sum in Matrix
#Example 3
import numpy as np
matriksA = np.random.randint(1, 4,(6, 10))
matriksB = np.random.randint(1, 3,(6, 10))
print (matriksA)
print () #give line spacing to the printed matrix
print (matriksB)
print ()

#summation of matrix A and matrix B
for x in range(0, len(matriksA)):
    print ()
    for y in range(0, len(matriksA[0])):
        print (matriksA[x][y] + matriksB[x][y], end=' '),
    print ()

#Subtraction in Matrix
#Example 1
mat1 = [
    [5, 0],
    [2, 6],
]

mat2 = [
    [1, 0],
    [4, 2],
]


for x in range(0, len(mat1)):
    for y in range(0, len(mat1[0])):
        print (mat1[x][y] - mat2[x][y], end=' '),
    print

#Subtraction in Matrix
#Example 2
mat1 = [
    [5, 0],
    [2, 6],
]

mat2 = [
    [1, 0],
    [4, 2],
]


for x in range(0, len(mat1)):
    for y in range(0, len(mat1[0])):
        print (mat1[x][y] - mat2[x][y], end=' '),
    print ()

#Subtraction in Matrix
#Example 3
import numpy as np
matriksA = np.random.randint(1, 4,(3, 4))
matriksB = np.random.randint(1, 3,(3, 4))
print (matriksA)
print () #give line spacing to the printed matrix
print (matriksB)
print ()

#subtraction matrix A with matrix B
for x in range(0, len(matriksA)):
    print ('Result of Subtraction matrix A and matrix B', 'Row-', x+1)
    print ()
    for y in range(0, len(matriksA[0])):
        print (matriksA[x][y] - matriksB[x][y], end=' '),
    print ()

#Subtraction in Matrix
#Example 4
import numpy as np
matriksA = np.random.randint(1, 4,(6, 10))
matriksB = np.random.randint(1, 3,(6, 10))
print (matriksA)
print () #give line spacing to the printed matrix
print (matriksB)
print ()

#subtraction matrix A with matrix B
for x in range(0, len(matriksA)):
    print ()
    for y in range(0, len(matriksA[0])):
        print (matriksA[x][y] - matriksB[x][y], end=' '),
    print ()
