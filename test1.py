import numpy as np
import sympy as sp
# # print("hello world")


# # 2CA-2AB = C-B
# # 2CA-C = 2AB-B
# # 2C(A-I) = 2B(A-I)

# A = sp.Matrix([[2,8,6,0,-6,8,0],[-1,8,-2,1,1,-9,5],[-5,7,3,-1,7,2,7],[3,-5,-1,-6,7,3,-4],[-5,2,2,6,-9,-7,3],[-8,-8,-5,8,-5,8,-7],[8,-9,-7,8,6,1,2]]); 
# print(A.rref())

# from numpy import array
# from scipy.linalg import lu

# a = array([[1,4,3],[0,1,2],[2,5,0]])
# print(np.linalg.(A))

A = sp.Matrix([[1,2,-1,3],[-2,-3,1,-5],[1,-1,2,0]]).T

b = sp.Matrix([1,0,1,0])

AtA = A.transpose()@A
Atb = A.transpose()@b

x1,x2,x3 = sp.symbols('x1 x2 x3')

print(sp.linsolve((AtA,Atb),x1,x2,x3))


A = sp.Matrix([[1,1,0,0],[1,0,1,0],[0,1,1,1]]).T
Q,R = A.QRdecomposition()

print("Q:\n",Q)
print("R:\n",R)

A =sp.Matrix([[0,0,3],[1,0,-1],[0,1,3]])
print(A.eigenvects())
print(A.diagonalize())


A = np.array([[6,3,6],[3,6,1],[6,1,6]])
print(np.linalg.eig(A))