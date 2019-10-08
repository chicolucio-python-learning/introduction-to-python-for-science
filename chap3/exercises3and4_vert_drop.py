# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:33:06 2016
@author: Francisco Bustamante

vert_drop.py

Exercício nº 3 e 4 - capítulo 3 - Python for Science

Queda vertical
y = h0 - 1/2 * g * t^2
t = sqrt((2(h0 - y))/g)

g = 9.8 m/s2

script para achar t sendo dado os demais parâmetros

Tentando usar recursos de IO
"""

import numpy as np

np.set_printoptions(threshold=np.inf)

print("Esse programa calcula o tempo a cada 0,5 m de queda vertical. \
Forneça os dados solicitados. \n \
*O programa já considera g = 9,8 m/s2 \n \
*Lembre de entrar os valores com '.' ao invés de ','")

g = 9.8
h0 = float(input("Forneça a altura inicial da queda em metros: "))

print("\nCalculando... \n")

y = np.arange(h0, 0, -0.5)
print("Alturas com decréscimo de 0,5 metro:")
print(y, "\n")

print("Tempo em cada altura anterior:")
t = np.sqrt((2*(h0 - y))/g)
print(t, "\n")

desloc = y[1:] - y[:-1]
t_desloc = t[1:] - t[:-1]

print("Velocidade média a cada 0,5 metro de queda:")
v_med = desloc / t_desloc
print(v_med)
