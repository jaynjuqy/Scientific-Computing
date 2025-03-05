#A startup incubator at JKUAT is optimizing the cost function:
#   C(x) = 5x^3 - 10x^2 + 4x + 3 where x is the number of AI startups funded.

import sympy as sp

x = sp.symbols('x')
C = 5*x**3 - 10*x**2 + 4*x + 3

#Task 1: Find the symbolic derivative of C(x).
first_derivative = sp.diff(C, x)
print(f"Symbolic derivative(first) of C(x) is {first_derivative}")

#Task 2: Solve for x when the cost is minimized
x_critical_points = sp.solve(first_derivative, x)
second_derivative = sp.diff(first_derivative, x)

for point in x_critical_points:
    concavity = second_derivative.subs(x, point)

    if isinstance(concavity, sp.Basic):
        concavity = float(concavity)

    if concavity > 0:
        print(f"Cost is minimized when x={point}")
    else:
 
