"""
Created on Thu Nov 10 09:33:46 2016
@author: chico
vert_throw.py
Modified on Tue Oct 8 7:50 2019

Exercício nº 1 - capítulo 2 - Python for Science

lançamento vertical
h = h0 + v0 * t - 1/2 * g * t^2
v = v0 - g * t

g = 9.8 m/s2

script para achar h sendo dado os demais parâmetros

Tentando usar recursos de IO
"""

print("Esse programa calcula a altura (m) e a velocidade (m/s) de um lançamento \
vertical. Forneça os dados solicitados. \n \
*O programa já considera g = 9,8 m/s2 \n \
*Lembre de entrar os valores com '.' ao invés de ','")

G = 9.8
H0 = float(input("Forneça a altura inicial do lançamento em metros: "))
V0 = float(input("Forneça a velocidade inicial do lançamento em m/s: "))
T = float(input("Forneça o tempo, em segundos, após o qual se deseja os \
valores de h e v: "))

print("\nCalculando... \n")

H = H0 + V0 * T - 1/2 * G * T**2
V = V0 - G * T

print("Altura final: {0:0.2f}".format(H), "metros")
print("Velocidade final: {0:0.2f}".format(V), "m/s")

print("\nDados acima calculados para os seguintes valores de entrada:")
print("Altura inicial: {0:0.2f}".format(H0), "metros")
print("Velocidade inicial: {0:0.2f}".format(V0), "m/s")
print("Tempo: {0:0.2f}".format(T), "segundos")


# Futuras melhorias no programa:

# TODO variáveis com nomes inteligíveis;
# TODO reconhecer quando o resultado der negativo e alertar o usuário;
# TODO reconhecer o número de algarismos significativos de entrada;
# TODO dar resposta condizente com o número de algarismos significativos;
# TODO plotar os gráficos de h e v com base nos dados do usuário;
# TODO no gráfico, destacar os pontos de máxima altura e contato com solo
