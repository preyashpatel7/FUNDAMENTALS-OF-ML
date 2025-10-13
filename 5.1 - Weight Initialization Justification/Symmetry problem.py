import numpy as np

x = np.array([[1,2,3],[4,5,6]])
w = np.ones((3,2))

result = np.matmul(x,w)
print(result)
print("\n see the resulting matrix have same row values. Meaning all those hidden nodes will get same output!")