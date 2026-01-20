#sympy (Calculus library in Python)

import sympy as sym 

x = sym.symbols('x')
derivative1 = sym.diff(sym.sin(x), x)
print(derivative1)

x = sym.symbols('x')
derivative1 = sym.diff(sym.sin(x**2), x)
print(derivative1)

x = sym.symbols('x')
func = sym.sin(x)**2 + sym.exp(x**2)
derivative1 = sym.diff(func, x)
print(derivative1)

x = sym.symbols('x')
func = sym.sin(x)**2 + sym.exp(x**2)
derivative1 = sym.diff(func, x, 2)
print(derivative1)
