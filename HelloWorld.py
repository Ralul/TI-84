import sympy as sy
from sympy import S
sy.init_printing()


x,y = sy.symbols('x,y')
print(sy.solveset(x**2-y**2,x))