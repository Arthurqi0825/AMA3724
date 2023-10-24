import sympy as sp

# A = sp.Matrix([[3,-2,4], [-2,6,2], [4,2,3]])
# A = sp.Matrix([[3,2,2,2], [2,3,2,2],[2,2,3,2], [2,2,2,3]])
A = sp.Matrix([[1,2,2],[2,1,2],[3,-3,4]])
P,D = A.diagonalize()
Q,R = P.QRdecomposition()
print(Q)
print(R)
print(A.eigenvects())
print((Q)@D@(Q.inv()))