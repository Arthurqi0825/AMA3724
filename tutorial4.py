import sympy as sp 

A = sp.Matrix([[4,-1,6],[2,1,6],[2,-1,8]])
print(A.eigenvects())

A = sp.Matrix([[1,0,1],[-1,2,1],[0,0,2]])

P,D = A.diagonalize()
print(A.eigenvals())
print("P",P)
print("D",D)


A = sp.Matrix([[2,3,2],[1,8,2],[-2,-14,-3]])
# print(A)
# print(A.eigenvects())
S, J = A.jordan_form()
print(S)
print(J)