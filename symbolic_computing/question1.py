#A machine learning model at JKUAT is trained using the loss function:
#   L(x) = 3x^2 + 2x - 5

import sympy as sp

x = sp.symbols('x')

L = 3*x**2 + 2*x - 5

#Task 1: Compute the symbolic derivative of L(x) to find the gradient
first_derivative = sp.diff(L, x)
print(f"Gradient, L'(x) = {first_derivative}")

#Task 2: Solve for x when the gradient is zero(optimal solution)
x_critical_points= sp.solve(L, x)
print(f"X when gradient is zero is {x_critical_points}")

#Task 3: Use the second derivative to check if it is a maximum or a minimum
second_derivative = sp.diff(first_derivative, x)
for point in x_critical_points:
    concavity = second_derivative.subs(x, point)

    if isinstance(concavity, sp.Basic):
        concavity = float(concavity)

    if concavity > 0:
        print(f"x={point} is a minimum")
    elif concavity < 0:
        print(f"x={point} is a maximum")
    else:
        print(f"x={point} is an inflection point")
