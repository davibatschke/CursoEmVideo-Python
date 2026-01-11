# DESAFIO 18 do Curso de Python:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

valor_angulo = float(input('Digite um valor para o Angulo: '))
angulo_radiano = math.radians(valor_angulo)
# math.radians() serve para transformar um numero num valor radiano

print(f'O valor de SENO: {math.sin(angulo_radiano):.2f}')
print(f'O valor do COSSENO: {math.cos(angulo_radiano):.2f}')
print(f'O valor da TANGENTE: {math.tan(angulo_radiano):.2f}')