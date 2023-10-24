import sympy as sp 

A = sp.Matrix([[4,-1,6],[2,1,-6],[2,-1,8]])
print(A.eigenvals())

A = sp.Matrix([[1,0,1],[-1,2,1],[0,0,2]])
print("\n")
B = sp.Matrix([[1,1,0],[0,1,0],[1,0,1]]).T
print((B.inv())@A@(B))


A = sp.Matrix([[2,4,3],[-4,-6,-3],[3,3,1]])
# print(A)
print(A.eigenvects())
