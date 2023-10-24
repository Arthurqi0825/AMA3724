import numpy as np
import sympy as sp

# Q1 
A1 = np.array([[2,6,4]]).T
A2 = np.array([[2,4,2]]).T
A3 = np.array([[1,0,-1]]).T
print("linear combination is\n")
print(-2*A1 + 3*A2-2*A3)

A = sp.Matrix([[2,4,2],[1,0,-1]]).T
A1 = sp.Matrix([[2,6,4]]).T
x1,x2= sp.symbols('x1 x2')
sol = sp.linsolve((A,A1),x1,x2)

print(f"solution is {sol}")

# Q2b
A = sp.Matrix([[2,4,5],[3,0,0],[1,4,3]])
B = sp.Matrix([[1,3,6],[4,5,0],[2,7,5]])

print(f"det(AB) is {sp.det(A@B)}")
print(f"det(3A) is {sp.det(3*A)}")

# Q3
print("Q3a")
A = np.array([[2,4,5],[3,0,0],[1,4,3]])
B = np.array([[1,3,6],[4,5,0],[2,7,5]])

print(f"A*B = {A@B}" )
print(f"B*A = {B@A}")

print("\n Q3b")
A = np.array([[1, 0],[0, 0]])
B = np.array([[0, 0],[0, 1]])

print(f"A*B = {A@B}")
print(f"B*A = {B@A}")

print("Q3c")

A = np.array([[2,4,5],[3,0,0],[1,4,3]])
B = np.array([[1,3,6],[4,5,0],[2,7,5]])

M = np.linalg.det(A+B)
N = np.linalg.det(A)+np.linalg.det(B)
print(f"det(A+B) = {M} and det(A)+det(B) = {N}")
# print("NOT Equal")

# Q4
print("Q4")
A = np.array([[1,0,-1,2],[0,3,1,-1],[2,4,0,3],[-3,1,-1,2]])
B = np.array([[1,3,0,4],[2,-1,-2,1]]).T
C = np.array([[3,-2,0,5],[1,0,-3,4]])

print(3*pow(A,3)-5*pow((B@C),2))

A = sp.Matrix([[1,0,-1,2],[0,3,1,-1],[2,4,0,3],[-3,1,-1,2]])
B = sp.Matrix([[1,3,0,4],[2,-1,-2,1]]).T
C = sp.Matrix([[3,-2,0,5],[1,0,-3,4]])
print(3*pow(A,3)-5*pow((B@C),2))
# Q5

print("Q5")

A = np.array([[1,2,-1],[1,4,-2],[2,3,1]])
B = np.array([-4,-6,3])
# print(B)
print(np.linalg.solve(A,B))

# Q6

# Q8
print("Q8")
A = sp.Matrix([[1,1,2,3],[3,4,-1,2],[-1,-2,5,4]])

print(A.rref())

