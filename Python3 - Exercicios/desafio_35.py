# DESAFIO 35 do Curso de Python:
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

comp1 = float(input('Primeiro Comprimento: '))
comp2 = float(input('Segundo Comprimento: '))
comp3 = float(input('Terceiro Comprimento: '))

if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('\nAnalisando o seu Triangulo...')
    print(f'Com os valores fornecidos podemos sim fazer um Triangulo!')
else:
    print('\nAnalisando o seu Triangulo...')
    print(f'Com os valores fornecidos nao podemos fazer um Triangulo!')