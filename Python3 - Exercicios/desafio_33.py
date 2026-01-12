# DESAFIO 33 do Curso de Python:
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um Numero: '))
num2 = int(input('Digite outro Numero: '))
num3 = int(input('Digite mais um Numero: '))

num_menor = num1
num_maior = num1

print('\nAnalisando estes numeros...')
if num2 < num1 and num2 < num3:
    num_menor = num2
if num3 < num1 and num3 < num2:
    num_menor = num3
print(f'O menor numero eh {num_menor}')

if num2 > num1 and num2 > num3:
    num_maior = num2
if num3 > num1 and num3 > num2:
    num_maior = num3
print(f'O maior numero eh {num_maior}')