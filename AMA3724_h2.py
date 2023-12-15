import sympy as sp 

# print("Q1")
# A = sp.Matrix([[2,3,0],[1,4,0],[0,0,5]])

# print(A.eigenvects())
# print(A.det())

# print("Q2")
# A = sp.Matrix([[1,4,-2,6],[0,4,6,2],[0,0,0,6],[0,0,0,2]]);
# print(A.diagonalize());
# print(A.eigenvects())
# print("Q3")

# A = sp.Matrix([[2,3],[1,4]])

# P,D = A.diagonalize()
# print(P)
# print(D)

# print("Q4")
# A = sp.Matrix([[3,-2],[4,-1]])
# P,D = A.diagonalize()
# print(P)
# print(D)
print("Q5")
A = sp.Matrix([[5,2],[-2,1]])

P,J = A.jordan_form()
print(J)
print(P)
print(P@J@(P.inv()))

print("Q6")
A = sp.Matrix([[10,3,-2,1],[3,10,0,9],[-2,0,10,4],[1,9,4,10]])
num_col, num_rows =A.shape
B = abs(A)
print("Matrix A")
for i in range(1,num_col+1):
    print(A[:i,:i])
    print(A[:i,:i].det())
    
print("Matrix |A|")
for i in range(1,num_col+1):
    print(B[:i,:i])
    print(B[:i,:i].det())    


print("Q9")
A = sp.Matrix([[4,11,14],[8,7,-2]])
U,S,V = A.singular_value_decomposition()

print(U)
print(S)
print(V)
print(U@S@(V.transpose()))
print(A.shape)