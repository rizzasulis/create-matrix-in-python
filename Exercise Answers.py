#Exercise(1)
#Matrix with size 2x3
matriksC = [ [1,2,3],[4,5,6]]

#Show a matrix with the name Matrix C
print(matriksC)

#Exercise(2)
#Matrix using the loop function
m = 3
n = 2
x = [0]*m

#Loop function using for
for i in range(m):
  x[i]=[2]*n

#Show the matrix
print(x)

#Exercise(3)
#Call Library Numpy
from numpy import *

#Specifies the element length as 32
matriks = range(32)

#The order matrix is 4x8
matriks = reshape(matriks,(4,8)) 

#Show the matrix
print(matriks)

#Exercise(4)
#Calls the numpy library and is given the alias np
import numpy as np

#Create a 3x30 matrix with random
matriks=np.random.randint(1,5,(3,30))

#Show the matrix 
print(matriks)

#Exercise(5)
#Sum in Matrix
import numpy as np
matriksA = np.random.randint(1, 5,(7, 9))
matriksB = np.random.randint(1, 4,(7, 9))
print (matriksA)
print () #give line spacing to the printed matrix
print (matriksB)
print ()
#summation of matrix A and matrix B
for x in range(0, len(matriksA)):
    print ('Result of the sum of matrix A and matrix B', 'Row-', x+1)
    print ()
    for y in range(0, len(matriksA[0])):
        print (matriksA[x][y] + matriksB[x][y], end=' '),
    print ()

#Exercise(6)
#Substraction in Matrix
import numpy as np
matriksA = np.random.randint(1, 7,(7, 9))
matriksB = np.random.randint(1, 8,(7, 9))
print (matriksA)
print () #give line spacing to the printed matrix
print (matriksB)
print ()

#Substraction of matrix A and matrix B
for x in range(0, len(matriksA)):
    print ()
    for y in range(0, len(matriksA[0])):
        print (matriksA[x][y] - matriksB[x][y], end=' '),
    print ()
