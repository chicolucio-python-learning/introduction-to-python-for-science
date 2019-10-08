"""
Created on Sat Nov 12 09:14:58 2016
@author: Francisco Bustamante
Modified on Sat Oct 5 14:32 2019
quad_eq.py
Exercício nº 3 - capítulo 2 - Python for Science
"""

import cmath

print("Esse programa calcula as raízes de uma equação de segundo grau.\n \
Formato da equação Ax^2 + Bx + C = 0 \n \
*Lembre de entrar os valores com '.' ao invés de ','")

A = float(input("Forneça A: "))
B = float(input("Forneça B: "))
C = float(input("Forneça C: "))

print("\nCalculando... \n")

DELTA = B**2 - 4 * A * C

X1 = (-B + cmath.sqrt(DELTA)) / (2 * A)
X2 = (-B - cmath.sqrt(DELTA)) / (2 * A)

print("Primeira raiz: ", X1)
print("Segunda raiz: ", X2)


# Futuras melhorias no programa:

# TODO Colocar em formato complexo apenas soluções complexas
# Para isso, basta fazer um condicional, avaliando delta antes.
# TODO Ajustar o número de casas decimais usando formatação de output.
