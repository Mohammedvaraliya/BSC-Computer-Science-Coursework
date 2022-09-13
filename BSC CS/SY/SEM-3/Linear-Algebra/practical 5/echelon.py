# import sympy
import sympy

# find the reduced row echelon form
M=sympy.Matrix([[0,1,2,0,3],
                [2,4,8,2,4],
                [1,2,4,2,2],
                [1,3,6,1,5]]).rref()

print("Matrix : {} ".format(M))
 
# find the rank of matrix
print("Rank of matrix :",sympy.Matrix
      ([[0,1,2,0,3],
        [2,4,8,2,4],
        [1,2,4,2,2],
        [1,3,6,1,5]]).rank())
