# Solução do problem 1.1

import sympy as sp

# definindo as variáveis simbólicas
t, g, m, cd = sp.symbols('t g m cd', real=True, positive=True)

# definindo as constantes A e B
A = sp.sqrt(g * m / cd)
B = sp.sqrt(g * cd / m)

# definindo a função v(t)
v = A * sp.tanh(B * t)

# calculando a derivada primeira da função v(t)
dvdt = sp.diff(v, t)

# verificando se dv/dt - rhs é igual a zero
ehSolucao = (sp.simplify(dvdt - (g - (cd / m) * v**2)) == 0)

# imprimindo os resultados
print("v(t) = ", v)
print("dv/dt = ", dvdt)

if ehSolucao:
    print("v(t) é solução da equação diferencial.")
else:
    print("v(t) é não solução da equação diferencial.")
