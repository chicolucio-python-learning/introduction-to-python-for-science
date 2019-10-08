"""
Created on Sat Nov 12 08:41:15 2016

@author: Francisco Bustamante

some_calc.py

Exercício nº 2 - capítulo 1 - Python for Science
"""

import math

A = (2 + math.exp(2.8)) / (math.sqrt(13) - 2)
print(A)

A = (2 + math.e**(2.8)) / (math.sqrt(13) - 2)
print(A)

B = (1 - math.pow((1 + math.log(2)), (-3.5))) / (1 + math.sqrt(5))
print(B)

C = math.sin((2 - math.sqrt(2)) / (2 + math.sqrt(2)))
print(C)
