import sympy as sp

# A1 = sp.Matrix([[5,2],[3,1]])
# A2 = sp.Matrix([[2,3],[1,2]])
# A3 = sp.Matrix([[4,3],[3,3]])
# A4 = sp.Matrix([[5,4],[2,2]])

# A = sp.BlockMatrix([A1,A2,A3,A4]).as_explicit()

# print(A)

b = sp.Matrix([1,-1,2]);
c = sp.Matrix([24/7,-7/5,2/7])

R = b@c.transpose()
print(R@b)