import sympy as sp
import numpy as np
x = sp.symbols('x')
y = sp.Function('y')(x)
DE = sp.Eq(y.diff(),-2*y/(3*x-y))
A = sp.dsolve(DE,y,simplify = True)
print(A)

# A = sp.Matrix([[5,2,4,5],[2,3,3,4],[3,1,3,2],[1,2,3,2]])
A = sp.Matrix([[5,2],[3,1],[2,3],[1,2],[4,3],[3,3],[5,4],[2,2]])
# A = np.array([[5,2],[3,1],[2,3],[1,2],[4,3],[3,3],[5,4],[2,2]])
# B = sp.Matrix([[1,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,1]]).T
B = np.array([[1,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,1]]).T
# print(np.linalg.solve(A,B))
print(A@(A.transpose()))
