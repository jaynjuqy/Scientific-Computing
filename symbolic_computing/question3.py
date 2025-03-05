#In a control system, the Laplace Transform of the system equation is:
#   H(s) = {1}/{s^2 + 3s + 2}

import sympy as sp

s, t = sp.symbols('s t')
H_s = 1 / (s**2 + 3*s +2)

#Task 1: Factor the denominator symbolically
factored_denominator = sp.factor(sp.denom(H_s))
print(f"Factored denominator for the expression {sp.denom(H_s)} is {factored_denominator}")

#Task 2: Compute the Inverse Laplace Transform to find h(t)
h_t = sp.inverse_laplace_transform(H_s, s, t)
print(f"The inverse laplace transform of {H_s} is {h_t}")

#Task 3: Find the poles of the system
poles = sp.solve(sp.denom(H_s), s)
print("The poles of the system are ", poles)
