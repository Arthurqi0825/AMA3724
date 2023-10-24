import numpy as np
import sympy as sp

# Linear Combination
'''
    It's matrix with[v1,v2,...] in Matrix A
    Code is to check whether b is a linear combination of vectors
    from v1 to vn.

    Solve the Matrix equation Ax=b to find the combination

'''
A = sp.Matrix([[2,4,2],[1,0,-1]]).T
b = sp.Matrix([[2,6,4]]).T
x1,x2= sp.symbols('x1 x2')
print(A)
print(b)
sol = sp.linsolve((A,b),x1,x2)
print(sol)


'''
    Linear dependence:
    Ax = 0 for {v1,v2,...}
    and using A.rref() to check whether its linearly dependent
'''

A = sp.Matrix([[1,-2,-5,3,1],
               [2,5,6,-1,2],
               [3,-4,5,-2,3],
               [4,8,-8,9,4],
               [4,8,-8,10,4]]).T

print(A.rref())



print("Inner product")
x = sp.Matrix([[1,2,3,4,5]]).T
y = sp.Matrix([[3,-1,2,1,-1]]).T
print(y.T*x)