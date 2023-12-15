import sympy as sp

T = sp.Matrix([[1,0,0,0],[0,0,-1,2],[0,1,0,0],[0,0,0,1]])

p = sp.Matrix([1,0,0,1])

print(T@p)