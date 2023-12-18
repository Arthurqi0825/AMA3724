import sympy as sp
# positive definite check: det>0
def pos_def_check(A):
    if A.rows != A.cols:
        return "not square"
    else:
        # is square
        for i in range(1,A.rows):
            print(A[:i,:i])
            print(A[:i,:i].det())
            if A[:i,:i].det() < 0:
                return "not Positive Definete"
            
    return f"{A} is positive Definite"
        



A = sp.Matrix([[1,2,2],[2,1,2],[3,-3,4]])
P, D = A.diagonalize()
Q,R = P.QRdecomposition()
# print(Q@D@Q.transpose()) 
T = sp.Matrix([[4,-1,3],[0,-1,-4],[0,0,3]])
print(D)
# print(Q@D@Q.transpose()) 
print()
A = sp.Matrix([[3,-2,4],[-2,6,2],[4,2,3]])
#  Attention: A should be symmetric matrix to use QDQ^T to decomposite

P, D = A.diagonalize()
Q,R = P.QRdecomposition()
print(Q@D@Q.transpose())

# SVD:
A = sp.Matrix([[1,2,3],[-1,0,1],[3,2,1]])

U, S, V = A.singular_value_decomposition()

print(A.singular_value_decomposition())

print(U@S@V.transpose())
print(pos_def_check(A))

A = sp.Matrix([[1,1,1,-1],[0,1,1,0],[-1,1,1,1]])
U, S, V = A.singular_value_decomposition()

print(A.singular_value_decomposition())

print(U@S@V.transpose())
