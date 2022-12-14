# Create Matrices in Python
A matrix in the world of mathematics is a number, symbol, or expression arranged in rows and columns that form a square/rectangular field. The matrix has size/order. In Python, matrices can be created as needed by specifying the size/order of the matrix. The general form of the size/order of a matrix is mxn, m is the number of rows and n is the number of columns.

## Creating a 2x2 Order Matrix
A matrix of order 2x2 is a matrix that has values in 2 rows and 2 columns. In the example: matrixA has: Row 1 Column 1, value = 1 Row 1 Column 2, value = 0 Row 2 Column 1, value = 0 Row 2 Column 2, value = 1.

Here is the syntax to create a matrix named matrix A with a size/order of 2x2.
```python
#Matrix A with a size/order of 2x2
matriksA = [ [1,0],[0,1] ]

#Show the Matrix A
print (matriksA)
```
And here is the output of the program
```python
[[1, 0], [0, 1]]
```

## Creating a 3x3 Order Matrix
A matrix of order 3x3 is a matrix that has values in 3 rows and 3 columns. In the example: matrix B has: Row 1 Column 1, value = 1 Row 1 Column 2, value = 0 Row 1 Column 3, value = 1 Row 2 Column 1, value = 0 Row 2 Column 2, value = 1 Row 2 Column 3 , value = 0 Row 3 Column 1, value = 1 Row 3 Column 2, value = 0 Row 3 Column 3, value = 1.

Here is the syntax to create a matrix named matrix B with a size/order of 3x3.
```python
#Matrix A with a size/order of 3x3
matriksB = [ [1,0,1],[0,1,0],[1,0,1] ]

#Show the Matrix B
print (matriksB)
```
And here is the output of the program
```python
[[1, 0, 1], [0, 1, 0], [1, 0, 1]]
```
## Creating a Matrix with a Loop
Matrices can also be created using the loop function. The looping function or commonly called looping or iteration requires a condition test. If the test result is True, the code block is executed again. But if False, then exit the loop. In python, looping can be done in two ways or methods, namely: using For or using While.
### Creating a Matrix with a Loop
The following is a matrix using the for a loop. The matrix has order mxn, namely: order 2x3, and the values given are: Row 1 Column 1, value = 1 Row 1 Column 2, value = 1 Row 1 Column 3, value = 1 Row 2 Column 1, value = 1 Row 2 Column 2, value = 1 Row 2 Column 3, value = 1
```python
#Matrix using the loop function
m = 2
n = 3 
x = [0]*m

#Loop function using for
for i in range(m): 
    x[i] = [1]*n 
 
#Show the Matrix
print (x)
```
And here is the output of the program
```python
[[1, 1, 1], [1, 1, 1]]
```
## Creating a Matrix Using the Numpy Library
Library in Python is a term for additional program code that is used for certain needs. Python has more than 140,000 libraries developed through open-source projects.

The Numpy library is useful for vector and matrix operations. Its features are almost the same as MATLAB in managing multidimensional arrays and arrays. Numpy is one of the libraries used by other libraries such as Scikit-Learn for data analysis purposes.

In the following example, a matrix with a length of 12 elements is created with element values starting from index 0 to 11, with the size/order of the matrix is 4x3.
```python
#Call Library Numpy
from numpy import * 

#Specifies the length of the element as 12
matriks = range(12)

#The order matrix is 4x3
matriks = reshape(matriks,(4,3)) 

#Show the Matrix
print (matriks)
```
And here is the output of the program
```python
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
```
### Creating a Matrix with Random Values
If you want elements in the matrix to be random, you can use the random function available in numpy.

In the following example, a matrix of size/order 3x4 is created with element values starting from index 1 to 4 at random.
```python
#Calls the numpy library and is given the alias np
import numpy as np

#Create a 3x4 matrix with random
matriks = np.random.randint(1,4,(3,4))

#Show the Matrix
print (matriks)
```
And here is the output of the program
```python
[[3 1 3 1]
 [1 1 2 3]
 [1 1 3 3]]
```
## Sum in Matrix
Matrix addition is done by adding up each element, using the plus sign (+). The result of the sum will be a new element. Each matrix is accessed by each element at the same coordinates and then added together to get a new element. Matrix addition is done on two matrices that have the same order.

The following are some examples of addition in a matrix.
```python
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
```
And here is the output of the program in example 1
```python
6 0 6 8 
```
```python
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
```
And here is the output of the program in example 2
```python
[[2 3 1 2]
 [2 1 2 3]
 [1 1 1 3]]

[[2 1 1 1]
 [2 2 2 2]
 [1 2 2 2]]

Result of the sum of matrix and matrix B Row- 1

4 4 2 3 
Result of the sum of matrix and matrix B Row- 2

4 3 4 5 
Result of the sum of matrix and matrix B Row- 3

2 3 3 5 
```
```python
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
```
And here is the output of the program in example 3
```python
[[1 3 3 2 2 3 2 2 1 2]
 [1 1 1 1 3 2 1 1 2 3]
 [3 1 2 2 2 2 3 2 2 2]
 [3 3 1 3 1 3 1 1 3 2]
 [2 3 1 2 1 3 3 1 1 2]
 [1 1 3 3 3 3 1 2 1 1]]

[[1 1 2 1 2 2 2 1 1 1]
 [2 1 1 1 2 2 1 2 1 1]
 [2 2 2 2 1 2 2 1 1 2]
 [2 1 2 1 2 1 1 1 2 2]
 [1 2 2 1 2 2 2 2 1 1]
 [2 2 1 2 1 1 2 1 2 2]]


2 4 5 3 4 5 4 3 2 3 

3 2 2 2 5 4 2 3 3 4 

5 3 4 4 3 4 5 3 3 4 

5 4 3 4 3 4 2 2 5 4 

3 5 3 3 3 5 5 3 2 3 

3 3 4 5 4 4 3 3 3 3  
```
## Subtraction in Matrix
Matrix subtraction uses the operator with a minus sign (-). A new matrix will be formed as a result of subtracting each of the two matrix elements. Matrix subtraction is performed on two matrices that have the same order.

The following are some examples of addition in a matrix.
```python
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
```
And here is the output of the program in example 1
```python
4 0 -2 4
```
```python
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
```
And here is the output of the program in example 2
```python
4 0 
-2 4 
```
```python
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
```
And here is the output of the program in example 3
```python
[[2 2 2 2]
 [3 2 1 1]
 [2 2 3 1]]

[[1 2 1 2]
 [1 2 1 1]
 [2 1 2 1]]

Result of Subtraction matrix A and matrix B Row- 1

1 0 1 0 
Result of Subtraction matrix A and matrix B Row- 2

2 0 0 0 
Result of Subtraction matrix A and matrix B Row- 3

0 1 1 0  
```
```python
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
```
And here is the output of the program in example 4
```python
[[2 3 1 3 1 2 2 3 1 3]
 [2 1 3 2 2 2 3 1 2 1]
 [2 2 1 2 3 2 3 3 1 2]
 [3 3 1 1 1 1 3 2 2 1]
 [3 2 2 2 1 1 1 1 1 2]
 [3 1 3 2 3 3 1 3 1 3]]

[[2 1 2 1 2 1 2 2 2 1]
 [2 2 2 2 2 1 1 1 1 2]
 [1 2 2 1 1 1 2 1 1 2]
 [2 1 1 2 1 2 1 2 2 1]
 [2 1 2 1 1 1 1 1 2 1]
 [2 1 1 2 1 1 2 2 2 2]]


0 2 -1 2 -1 1 0 1 -1 2 

0 -1 1 0 0 1 2 0 1 -1 

1 0 -1 1 2 1 1 2 0 0 

1 2 0 -1 0 -1 2 0 0 0 

1 1 0 1 0 0 0 0 -1 1 

1 0 2 0 2 2 -1 1 -1 1
```

## EXERCISES 
1. Create a matrix C with order 2x3, and the values given to matrix C are as follows: Row 1 Column 1, value = 1 Row 1 Column 2, value = 2 Row 1 Column 3, value = 3 Row 2 Column 1, value = 4 Row 2 Column 2, value = 5 Row 2 Column 3, value = 6.
2. Create a matrix with order 3x2, with values are: Row 1 Column 1, value = 2 Row 1 Column 2, value = 2 Row 2 Column 1, value = 2 Row 2 Column 2, value = 2 Row 3 Column 1, value = 2 Row 3 Column 2, value = 2.
3. Create a matrix using the Numpy Library with an element length is 32 and the matrix has order of 4x8.
4. Create a matrix using the Numpy Library with the order of 3x30, and the element values start from index 1 to 5 randomly.
5. Create a sum of two matrices using the Numpy library, with a 7x9 matrix whose values are obtained randomly.
6. Create a subtraction of two matrices using the Numpy library, with a 7x9 matrix whose values are obtained randomly.
