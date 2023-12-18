import sympy as sp
import numpy as np

A = sp.Matrix([[3,17],[19,1]])
print("det",A.det())
print("invA ",A.inv())
print("A2", A**2)
print("Q2")
A = sp.Matrix([[10,5,0],[1,19,0]])
B = sp.Matrix([[1,1],[1,0]])
print("AT", A.transpose())
print((A.transpose())@B,B.transpose()@A)   
print("Q4")
A = sp.Matrix([[1,3,5,0],[0,1,0,10],[0,0,1,3],[0,0,0,1]])
A = 5*A
print(A.transpose().det())
print("A eigenvals",A.eigenvals())

print("Q5")
A1 = sp.Matrix([[1,5],[7,9]])
A2 =sp.Matrix([[2,3],[4,7]])
A22 = sp.eye(2)
A12 = sp.zeros(2,2)
print(A22)
A = sp.Matrix([[A1,A2],[A12,A22]])

print(A)
print("A inv",A.inv())

print("Q6")
A = sp.Matrix([[2,2,1],[3,1,5],[3,2,3]])
B = sp.Matrix([1,2,3])

x1,x2,x3 = sp.symbols('x1 x2 x3')
print(sp.linsolve((A,B),x1,x2,x3))

print("Q8")
A =sp.Matrix([[2,2,1,0,0],[3,1,0,0,0],[0,0,0,1,1]])

b = sp.Matrix([0,0,1])

x1,x2,x3,x4,x5 = sp.symbols('x1 x2 x3 x4 x5')

print(sp.linsolve((A,b),x1,x2,x3,x4,x5))