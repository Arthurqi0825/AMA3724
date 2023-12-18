import sympy as sp 

# Q1
A = sp.Matrix([[2,1,1],[1,-1,3]]).T
print(A)
v=sp.Matrix([1,5,-7]).T

x1,x2 = sp.symbols("x1 x2 ")

print(sp.linsolve((A,v),x1,x2))
# Q2
A = sp.Matrix([[2,1,0],[2,2,0],[0,0,1]])

B = sp.eye(3)
I = sp.eye(3)
B[1,1] = -1
B[2,2] = 2
# print(B)

C = (2*A-I)*B*((2*A-I).inv())

print(pow(C,5))

# A  = sp.Matrix([[1,0,2],[4,1,5],[3,2,0]]).T
# print(A)
# print(A.rref())

# Q4
print("Q4")
A  = sp.Matrix([[0,-3,-2],[-5,9,1]])

u = sp.Matrix([5,3,-2])

print(A@u)

# # Q5

print("Q5")
A = sp.Matrix([[-3,6,-1,1,-7],[1,-2,2,3,-1],[2,-4,5,8,-4]])

x1,x2,x3,x4,x5 = sp.symbols('x1 x2 x3 x4 x5')

print(sp.linsolve((A,sp.zeros(5,1)),x1,x2,x3,x4,x5))
print(A.rref())
print(A.nullspace())
# # Q7

A = sp.Matrix([[1,0,2],[4,1,5],[3,2,0]]).T

print(A.rref())

A = sp.Matrix([[1,1,2,3],[3,4,-1,2],[-1,-2,5,4]])
x1, x2, x3, x4 = sp.symbols('x1,x2,x3,x4');
print(A)
print(sp.linsolve((A, sp.zeros(4, 1)), x1, x2, x3, x4))
print(A.nullspace())

