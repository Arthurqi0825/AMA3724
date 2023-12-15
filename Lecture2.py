import numpy as np 
import sympy as sp

# A = sp.Matrix([[1,2,3],[-2,5,-4],[-5,6,5],[3,-1,-2],[1,2,3]]);

# x1,x2,x3 = sp.symbols('x1 x2 x3')

# b1 = sp.Matrix([[4,8,-8,9,4]]).T

# b2 = sp.Matrix([[4,8,-8,9,5]]).T

# print(sp.linsolve((A,b1),x1,x2,x3))

# print(sp.linsolve((A,b2),x1,x2,x3))

# A = sp.Matrix([[1,-2,-5,3,1],[2,5,6,-1,2],[3,-4,5,-2,3],[4,8,-8,10,4],[3,8,-8,9,5]]).T
# b2 = sp.Matrix([[4,8,-8,9,5]]).T
# b1 = sp.Matrix([[4,8,-8,9,4]]).T

# x1,x2,x3,x4,x5 = sp.symbols('x1 x2 x3 x4 x5')

# print(A)

# print(f"A rref is \n{A.rref()}")

# print(sp.linsolve((A,b2),x1,x2,x3,x4,x5))
# print(sp.linsolve((A,b1),x1,x2,x3,x4,x5))

# if we ahve v1,v2,... and check whether any one of them can be writen as combination of others =:

A = sp.Matrix([[1,-2,-5,3,1],[2,5,6,-1,2],[3,-4,5,-2,3],[4,8,-8,9,4],[4,8,-8,10,4]]).T; 
print(f"A is \n{A}")
print(f"A rref is \n{A.rref()}")

# [1, 0, 0,  3, 0],
# [0, 1, 0,  2, 0],
# [0, 0, 1, -1, 0],
# [0, 0, 0,  0, 1],
# [0, 0, 0,  0, 0]]), (0, 1, 2, 4))

#  (0, 1, 2, 4)) it means that v4 can be written as combination of v1,v2,v3,v5
#  and thses four cannot be simplifed   
