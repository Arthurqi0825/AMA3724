import sympy as sp
import numpy as np 



 
# Q1   
print("Othogonal Set u1 u2 and u3")
A = sp.Matrix([[3,1,1],[-1,2,1],[-0.5,-2,3.5]]).T

u1 = A[:, 0]
u2 = A[:, 1]
u3 = A[:, 2]
print(u1.dot(u2))
print(u1.dot(u3))
print(u2.dot(u3))

# A = np.array([[3,1,1],[-1,2,1],[-0.5,-2,3.5]]).T
b = sp.Matrix([6,1,-8]).T
x1,x2,x3 = sp.symbols('x1 x2 x3')
print(sp.linsolve((A,b),x1,x2,x3))
# print(np.linalg.solve(A,b))


# Q2
print("Q2")
y = np.array([1,6]).T
u = np.array([4,2]).T

p = (y.dot(u))/(u.dot(u))*u

print(p)

# Q3
A = sp.Matrix([[1,0,0], [1,1,0], [1,1,1], [1,1,1]])

Q, R = A.QRdecomposition()

print(f"Q is:\n{Q}\nR is:\n{R}")


A = np.array([[1, 1, 1, 1, 1, 1],
              [1, 0, 1, 0, 0, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 0, 1, 1]]).T

b = np.array([1, 1, 1, 1, 1, 1])

x, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)

print("Least-squares solution:")

print(f"x is {x}")
print(f"residuals is {residuals}")
# print(rank)
# print(singular_values)

A = sp.Matrix([[3,2,-1],[1,-4,3],[1,10,-7]])
b = sp.Matrix([2,-2,1])
ata = A.transpose()@A
atb = A.transpose()@b

AB = sp.Matrix([[ata,atb]])
print(AB.rref())