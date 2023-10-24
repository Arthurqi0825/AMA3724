import sympy as sp

A = sp.Matrix([[2,3],[3,-6]])
print(A)

print(A.charpoly())
print(A.eigenvals())
B = A.eigenvects()



