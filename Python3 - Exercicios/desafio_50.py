# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma_pares = 0
contador = 0

for numero in range(1, 7):
    num = int(input(f'Digite o {numero} Valor: '))
    if num % 2 == 0:
        soma_pares += num
        contador += 1

if soma_pares <= 0:
    print(f'Parece que nenhum número par foi fornecido.')
else:
    print(f'A soma de {contador} números pares, foi de {soma_pares}')