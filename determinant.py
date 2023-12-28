import numpy as np
from scipy.linalg import det

def determinant():
    A=np.array([[0,2,3],[3,2,9],[7,1,4]])
    val=det(A)
    print(val)


determinant()
