# DESAFIO 30 do Curso de Python:
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Escolha um Numero. Vamos ver ele eh Par ou Impar: '))
calculo = numero % 2

if calculo == 0:
    print(f'Parece que o seu numero eh PAR!')
else:
    print(f'Parece que o seu numero eh IMPAR!')