#In AI applications, dimensionality reduction is done using eigenvalues of matrices.
#    Given a feature matrix:
#       A = \begin{bmatrix} 2 & 1 \ 1 & 3 \end{bmatrix}

import sympy as sp

A = sp.Matrix([[2,1], [1,3]])

l = sp.symbols('l')

#Task 1: Compute the symbolic determinant of matrix A
A_det = A.det()
print(f"Determinant of matrix A {A} is {A_det}")

#Task 2: Find the eigenvalues of A using symbolic computation
eigenvalues_A = A.eigenvals()
print(f"Eigenvalues of matrix A {A} are {eigenvalues_A}")

#Task 3: Verify that the eigenvalues satisfy the characteristic equation
#NOTE the characteristic equation is det(A - lamdaI) = 0, where I = identity matrix of A, 
#                                                               lambda = eigenvalues, 
#                                                               A-lambdaI = matrix

characteristic_polynomial = A.charpoly(l).as_expr()
eigenvalues = list(eigenvalues_A.keys())
for eigenvalue in eigenvalues:
    result = characteristic_polynomial.subs(l, eigenvalue)

    if result != 0:
        print(f"The eigenvalue {eigenvalue} did not satisfy the characteristic equation")
    else:
        print(f"The eigenvalue {eigenvalue} satisfied the characteristic equation")
