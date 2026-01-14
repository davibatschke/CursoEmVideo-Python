# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um numero: '))
total_divisoes = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[1;35m', end=' -> ')
        total_divisoes += 1
    else:
        print('\033[0;34m', end=' ')
    print(f'{i}', end='')

if total_divisoes == 2:
    print(f'\n\033[mDepois de analisar... O número {numero} é Primo!')
else:
    print(f'\n\033[mDepois de analisar... O número {numero} Não é Primo.')
