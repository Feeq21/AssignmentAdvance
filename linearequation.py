#Question
#2x + y + z =2
#x+y =2
#y - 3z =1
import numpy as np

A = np.array([[2, 1, 1], [1, 1, 0], [0, 1, -3]])
B = np.array([2, 2, 1])
X1 = np.linalg.solve(A,B)

print(X1)