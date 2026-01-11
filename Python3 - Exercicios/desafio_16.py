# DESAFIO 16 do Curso de Python:
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

num_real = float(input('Digite um Numero Real: '))
conversao = math.trunc(num_real)
# math.trunc() serve para "truncar" um numero com virgula

print(f'O numero {num_real} em sua porcao inteira fica: {conversao}')