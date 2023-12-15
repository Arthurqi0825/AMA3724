import sympy as sp
import numpy as np 



 
# Q1   
print("Othogonal Set u1 u2 and u3")
A = sp.Matrix([[3,1,1],[-1,2,1],[-0.5,-2,3.5]])

u1 = A[0, :]
u2 = A[1, :]
u3 = A[2, :]
print(u1.dot(u2))
print(u1.dot(u3))
print(u2.dot(u3))

A = np.array([[3,1,1],[-1,2,1],[-0.5,-2,3.5]]).T
b = np.array([6,1,-8]).T

print(np.linalg.solve(A,b))


# Q2
print("Q2")
y = np.array([1,6]).T
u = np.array([4,2]).T

p = (y.dot(u))/(u.dot(u))*u

print(p)

# Q3
A = np.array([[1,0,0], [1,1,0], [1,1,1], [1,1,1]])

Q, R = np.linalg.qr(A)

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

A_sym = sp.Matrix(A)
b_sym = sp.Matrix(b)

# Define the symbol for the unknown vector x
x = sp.symbols('x0:{}'.format(A.shape[1]))

# Define the normal equations Ax = b
equations = [sp.Eq(A_sym * sp.Matrix(x), b_sym)]

# Solve the normal equations symbolically
solution = sp.solve(equations, x)

# Calculate the error
error = sp.N((A_sym * sp.Matrix(list(solution.values()))) - b_sym).norm()

# Print the solution and error
for i, sol in enumerate(solution):
    print('x{} = {}'.format(i, sol))

print('Error: {}'.format(error))
